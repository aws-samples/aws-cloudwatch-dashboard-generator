# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

from io import TextIOWrapper

import resources, utils, get_filepath

BODY_TEMPLATE = get_filepath.ROOT_DIR + "/templates/DashboardBody.json"

class Dashboard:
    def __init__(self, input_file: dict, output_file: TextIOWrapper):
        self.dashboard_body: dict = utils.json_to_dict(BODY_TEMPLATE)
        self.input_file: dict = input_file
        self.output_file: TextIOWrapper = output_file
        self.resources: list = []
        self.flags = {
            "ALB": False,
            "CLB": False,
            "CloudFront": False,
            "EC2": False,
            "ElastiCache": False,
            "NLB": False,
            "RDS": False,
            "NAT": False,
            "AuroraCluster": False,
            "AuroraInstance": False,
            "AmazonMQ": False,
            "AmazonMSK": False,
            "S3": False,
        }

        for key in self.flags.keys():
            if key in self.input_file.keys():
                self.flags[key] = True
        self._get_provided_resource_types()

    def generate(self):
        for resource in self.resources:
            metrics_list: dict = resource.write_template()
            self.dashboard_body["widgets"] += metrics_list
        utils.write_json_file(self.output_file, self.dashboard_body)

    def _get_provided_resource_types(self):
        for key in self.flags.keys():
            if self.flags[key]:
                if key == "ALB":
                    self.resources.append(resources.Alb(self.input_file))
                elif key == "CLB":
                    self.resources.append(resources.Clb(self.input_file))
                elif key == "CloudFront":
                    self.resources.append(resources.Cloudfront(self.input_file))
                elif key == "EC2":
                    self.resources.append(resources.Ec2(self.input_file))
                elif key == "ElastiCache":
                    self.resources.append(resources.ElastiCache(self.input_file))
                elif key == "NLB":
                    self.resources.append(resources.Nlb(self.input_file))
                elif key == "RDS":
                    self.resources.append(resources.Rds(self.input_file))
                elif key == "NAT":
                    self.resources.append(resources.Nat(self.input_file))
                elif key == "AuroraCluster":
                    self.resources.append(resources.AuroraCluster(self.input_file))
                elif key == "AuroraInstance":
                    self.resources.append(resources.AuroraInstance(self.input_file))
                elif key == "AmazonMQ":
                    self.resources.append(resources.Mq(self.input_file))
                elif key == "AmazonMSK":
                    self.resources.append(resources.Msk(self.input_file))
                elif key == "S3":
                    self.resources.append(resources.S3(self.input_file))