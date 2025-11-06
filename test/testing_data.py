# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

alb_input_1 = {
    "AWS/ApplicationELB": {
        "Resources": {
            "ap-northeast-1": [
                {
                    "account_id": "123456789012",
                    "LoadBalancer": "app/testALB/879c269ce5dd4542",
                    "TargetGroup": [
                        "targetgroup/http/384c8e9d1fec2487",
                        "targetgroup/http2/384c8e9d1fec2487",
                    ],
                },
                {
                    "account_id": "123456789012",
                    "LoadBalancer": "app/testALB2/e4fa21f252855f0f",
                },
            ]
        }
    }
}

clb_input_1 = {
    "AWS/ELB": {
        "Resources": {
            "ap-northeast-1": [
                {
                    "account_id": "123456789012",
                    "LoadBalancer": "testELB"
                },
                {
                    "account_id": "123456789012",
                    "LoadBalancer": "testELB2"
                },
            ]
        }
    }
}

cloudfront_input_1 = {
    "AWS/CloudFront": {
        "Resources": {
            "us-east-1": [
                {
                    "account_id": "123456789012",
                    "DistributionId": "testDistribution1"
                },
                {
                    "account_id": "123456789012",
                    "DistributionId": "testDistribution2"
                },
            ]
        }
    }
}

ec2_input_1 = {
    "AWS/EC2": {
        "Resources": {
            "us-east-1": [
                {
                    "account_id": "123456789012",
                    "InstanceId": "i-0f8f8f8f8f8f8f8f8"
                },
                {
                    "account_id": "123456789012",
                    "InstanceId": "i-9f9f9f9f9f9f9f9f9"
                },
            ],
            "us-east-2": [
                {
                    "account_id": "123456789012",
                    "InstanceId": "i-0a0a0a0a0a0a0a0a0"
                },
                {
                    "account_id": "123456789012",
                    "InstanceId": "i-0b0b0b0b0b0b0b0b0"
                },
            ],
        }
    }
}

s3_input = {
    "AWS/S3": {
        "Resources": {
            "us-east-1": [
                {
                    "account_id": "123456789012",
                    "BucketName": "examplebucket1-use1"
                },
                {
                    "account_id": "123456789012",
                    "BucketName": "examplebucket2-use1"
                },
            ],
            "us-east-2": [
                {
                    "account_id": "123456789012",
                    "BucketName": "examplebucket1-use2"
                },
            ],
        }
    }
}