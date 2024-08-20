# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import unittest

import utils, get_filepath
from resources import *
from .testing_data import *
from .testing_output import *

# Test the resources module
class TestResources(unittest.TestCase):
    maxDiff = None
    

    def test_alb(self):
        alb = Alb(alb_input_1)
        alb.template = utils.json_to_dict("templates/ALB.json")
        alb._data_processing(
            "AWS/ApplicationELB", "LoadBalancer"
        )

        self.assertEqual(len(alb.template), len(alb_output_1), msg="total number of CloudWatch widgets are different")
        # assertDictEqual to see any difference between two dictionaries
        for i in range(len(alb.template)):
            self.assertDictEqual(alb.template[i], alb_output_1[i])

    def test_clb(self):
        clb = Clb(clb_input_1)
        clb.template = utils.json_to_dict("templates/CLB.json")
        clb._data_processing(
            "AWS/ELB", "LoadBalancer"
        )

        self.assertEqual(len(clb.template), len(clb_output_1), msg="total number of CloudWatch widgets are different")
        # assertDictEqual to see any difference between two dictionaries
        for i in range(len(clb.template)):
            self.assertDictEqual(clb.template[i], clb_output_1[i])

    def test_cloudfront(self):
        cloudfront = Cloudfront(cloudfront_input_1)
        cloudfront.template = utils.json_to_dict("templates/CloudFront.json")
        cloudfront._data_processing(
            "AWS/CloudFront", "DistributionId"
        )

        self.assertEqual(len(cloudfront.template), len(cloudfront_output_1), msg="total number of CloudWatch widgets are different")
        # assertDictEqual to see any difference between two dictionaries
        for i in range(len(cloudfront.template)):
            self.assertDictEqual(cloudfront.template[i], cloudfront_output_1[i])

    def test_ec2(self):
        ec2 = Ec2(ec2_input_1)
        ec2.template = utils.json_to_dict("templates/EC2.json")
        ec2._data_processing(
            "AWS/EC2", "InstanceId"
        )

        self.assertEqual(len(ec2.template), len(ec2_output_1), msg="total number of CloudWatch widgets are different")
        # assertDictEqual to see any difference between two dictionaries
        for i in range(len(ec2.template)):
            self.assertDictEqual(ec2.template[i], ec2_output_1[i])

    def test_s3(self):
        s3 = S3(s3_input)
        s3.template = utils.json_to_dict("templates/S3.json")
        s3._data_processing(
            "AWS/S3", "BucketName"
        )
        s3._s3_template_preprocessing()

        self.assertEqual(len(s3.template), len(s3_output), msg="total number of CloudWatch widgets are different")
        # assertDictEqual to see any difference between two dictionaries
        for i in range(len(s3.template)):
            self.assertDictEqual(s3.template[i], s3_output[i], msg="Template does not match")