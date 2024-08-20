# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import utils, get_filepath
from aws_resource import Resource

TEMPLATE_DIR_PATH = get_filepath.ROOT_DIR + "/templates/"

ALB_TEMPLATE_PATH = TEMPLATE_DIR_PATH + "ALB.json"
CLB_TEMPLATE_PATH = TEMPLATE_DIR_PATH + "CLB.json"
CF_TEMPLATE_PATH = TEMPLATE_DIR_PATH + "CloudFront.json"
EC2_TEMPLATE_PATH = TEMPLATE_DIR_PATH + "EC2.json"
ELASCACHE_TEMPLATE_PATH = TEMPLATE_DIR_PATH + "ElastiCache.json"
NLB_TEMPLATE_PATH = TEMPLATE_DIR_PATH + "NLB.json"
RDS_TEMPLATE_PATH = TEMPLATE_DIR_PATH + "RDS.json"
AURORA_CLUSTER_TEMPLATE_PATH = TEMPLATE_DIR_PATH + "AuroraCluster.json"
AURORA_INSTANCE_TEMPLATE_PATH = TEMPLATE_DIR_PATH + "AuroraInstance.json"
NAT_TEMPLATE_PATH = TEMPLATE_DIR_PATH + "NAT.json"
MQ_TEMPLATE_PATH = TEMPLATE_DIR_PATH + "MQ.json"
MSK_TEMPLATE_PATH = TEMPLATE_DIR_PATH + "MSK.json"
S3_TEMPLATE_PATH = TEMPLATE_DIR_PATH + "S3.json"

class Alb(Resource):
    def __init__(self, input_file: dict):
        super().__init__(input_file)
        self.is_elbv2 = True

    def _read_template(self):
        self.template = utils.json_to_dict(ALB_TEMPLATE_PATH)

    def write_template(self) -> dict:
        self._read_template()
        self._data_processing(
            "ALB", "LoadBalancer"
        )
        return self.template


class Clb(Resource):
    def _read_template(self):
        self.template = utils.json_to_dict(CLB_TEMPLATE_PATH)

    def write_template(self) -> dict:
        self._read_template()
        self._data_processing("CLB", "LoadBalancer")
        return self.template


class Cloudfront(Resource):
    def __init__(self, input_file: dict):
        super().__init__(input_file)
        self.is_cf = True

    def _read_template(self):
        self.template = utils.json_to_dict(CF_TEMPLATE_PATH)

    def write_template(self) -> dict:
        self._read_template()
        self._data_processing("CloudFront", "DistributionId")
        return self.template


class Ec2(Resource):
    def _read_template(self):
        self.template = utils.json_to_dict(EC2_TEMPLATE_PATH)

    def write_template(self) -> dict:
        self._read_template()
        self._data_processing("EC2", "InstanceId")
        return self.template


class ElastiCache(Resource):
    def __init__(self, input_file: dict):
        super().__init__(input_file)
        self.is_elastic_cache = True

    def _read_template(self):
        self.template = utils.json_to_dict(ELASCACHE_TEMPLATE_PATH)

    def write_template(self) -> dict:
        self._read_template()
        self._data_processing("ElastiCache", "CacheClusterId")
        return self.template


class Nlb(Resource):
    def __init__(self, input_file: dict):
        super().__init__(input_file)
        self.is_elbv2 = True

    def _read_template(self):
        self.template = utils.json_to_dict(NLB_TEMPLATE_PATH)

    def write_template(self) -> dict:
        self._read_template()
        self._data_processing(
            "NLB", "LoadBalancer"
        )
        return self.template


class Rds(Resource):
    def _read_template(self):
        self.template = utils.json_to_dict(RDS_TEMPLATE_PATH)

    def write_template(self) -> dict:
        self._read_template()
        self._data_processing("RDS", "DBInstanceIdentifier")
        return self.template

class AuroraCluster(Resource):
    def _read_template(self):
        self.template = utils.json_to_dict(AURORA_CLUSTER_TEMPLATE_PATH)

    def write_template(self) -> dict:
        self._read_template()
        self._data_processing("AuroraCluster", "DBClusterIdentifier")
        return self.template

class AuroraInstance(Resource):
    def _read_template(self):
        self.template = utils.json_to_dict(AURORA_INSTANCE_TEMPLATE_PATH)

    def write_template(self) -> dict:
        self._read_template()
        self._data_processing("AuroraInstance", "DBInstanceIdentifier")
        return self.template

class Nat(Resource):
    def _read_template(self):
        self.template = utils.json_to_dict(NAT_TEMPLATE_PATH)

    def write_template(self) -> dict:
        self._read_template()
        self._data_processing("NAT", "NatGatewayId")
        return self.template

class Mq(Resource):
    def _read_template(self):
        self.template = utils.json_to_dict(MQ_TEMPLATE_PATH)

    def write_template(self) -> dict:
        self._read_template()
        self._data_processing("AmazonMQ", "Broker")
        return self.template
    
class Msk(Resource):
    def _read_template(self):
        self.template = utils.json_to_dict(MSK_TEMPLATE_PATH)

    def write_template(self) -> dict:
        self._read_template()
        self._data_processing("AmazonMSK", "Cluster Name")
        return self.template

class S3(Resource):
    def __init__(self, input_file: dict):
        super().__init__(input_file)
        self.S3_Y_AXIS = 1600 # https://quip-amazon.com/OtgHAamF64Ab/Event-Monitoring-Generator-for-IEM#CcI9CABLhc5
        self.is_s3 = True

    def _read_template(self):
        self.template = utils.json_to_dict(S3_TEMPLATE_PATH)

    def _s3_template_preprocessing(self) -> None:
        for widgets in self.template:
            widgets['y'] += self.S3_Y_AXIS

    def write_template(self) -> dict:
        self._read_template()
        self._s3_template_preprocessing()
        self._data_processing("S3", "BucketName")
        return self.template