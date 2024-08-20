# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

alb_output_1 = [
    {
        "type": "text",
        "x": 0,
        "y": 800,
        "width": 18,
        "height": 2,
        "properties": {"markdown": "\n# Application Load Balancer\n"},
    },
    {
        "type": "metric",
        "x": 0,
        "y": 808,
        "width": 9,
        "height": 6,
        "properties": {
            "metrics": [
                [
                    "AWS/ApplicationELB",
                    "HTTPCode_ELB_5XX_Count",
                    "LoadBalancer",
                    "app/testALB/879c269ce5dd4542",
                    {"region": "ap-northeast-1"},
                ],
                [
                    "AWS/ApplicationELB",
                    "HTTPCode_ELB_5XX_Count",
                    "LoadBalancer",
                    "app/testALB2/e4fa21f252855f0f",
                    {"region": "ap-northeast-1"},
                ],
            ],
            "view": "timeSeries",
            "stacked": False,
            "region": "ap-northeast-1",
            "period": 60,
            "stat": "Sum",
        },
    },
    {
        "type": "metric",
        "x": 0,
        "y": 802,
        "width": 18,
        "height": 6,
        "properties": {
            "metrics": [
                [
                    "AWS/ApplicationELB",
                    "RequestCount",
                    "LoadBalancer",
                    "app/testALB/879c269ce5dd4542",
                    {"region": "ap-northeast-1"},
                ],
                [
                    "AWS/ApplicationELB",
                    "RequestCount",
                    "LoadBalancer",
                    "app/testALB2/e4fa21f252855f0f",
                    {"region": "ap-northeast-1"},
                ],
            ],
            "view": "timeSeries",
            "stacked": False,
            "region": "ap-northeast-1",
            "stat": "Sum",
            "period": 60,
        },
    },
    {
        "type": "metric",
        "x": 0,
        "y": 826,
        "width": 9,
        "height": 6,
        "properties": {
            "metrics": [
                [
                    "AWS/ApplicationELB",
                    "TargetResponseTime",
                    "LoadBalancer",
                    "app/testALB/879c269ce5dd4542",
                    {"region": "ap-northeast-1"},
                ],
                [
                    "AWS/ApplicationELB",
                    "TargetResponseTime",
                    "LoadBalancer",
                    "app/testALB2/e4fa21f252855f0f",
                    {"region": "ap-northeast-1"},
                ],
            ],
            "view": "timeSeries",
            "stacked": False,
            "region": "ap-northeast-1",
            "stat": "Average",
            "period": 60,
        },
    },
    {
        "type": "metric",
        "x": 9,
        "y": 826,
        "width": 9,
        "height": 6,
        "properties": {
            "view": "timeSeries",
            "stacked": False,
            "stat": "Sum",
            "period": 60,
            "metrics": [
                [
                    "AWS/ApplicationELB",
                    "ClientTLSNegotiationErrorCount",
                    "LoadBalancer",
                    "app/testALB/879c269ce5dd4542",
                    {"region": "ap-northeast-1"},
                ],
                [
                    "AWS/ApplicationELB",
                    "ClientTLSNegotiationErrorCount",
                    "LoadBalancer",
                    "app/testALB2/e4fa21f252855f0f",
                    {"region": "ap-northeast-1"},
                ],
            ],
            "region": "ap-northeast-1",
        },
    },
    {
        "type": "metric",
        "x": 9,
        "y": 808,
        "width": 9,
        "height": 6,
        "properties": {
            "metrics": [
                [
                    "AWS/ApplicationELB",
                    "HTTPCode_ELB_502_Count",
                    "LoadBalancer",
                    "app/testALB/879c269ce5dd4542",
                    {"region": "ap-northeast-1"},
                ],
                [
                    "AWS/ApplicationELB",
                    "HTTPCode_ELB_502_Count",
                    "LoadBalancer",
                    "app/testALB2/e4fa21f252855f0f",
                    {"region": "ap-northeast-1"},
                ],
            ],
            "view": "timeSeries",
            "stacked": False,
            "region": "ap-northeast-1",
            "period": 60,
            "stat": "Sum",
        },
    },
    {
        "type": "metric",
        "x": 9,
        "y": 814,
        "width": 9,
        "height": 6,
        "properties": {
            "metrics": [
                [
                    "AWS/ApplicationELB",
                    "HTTPCode_ELB_504_Count",
                    "LoadBalancer",
                    "app/testALB/879c269ce5dd4542",
                    {"region": "ap-northeast-1"},
                ],
                [
                    "AWS/ApplicationELB",
                    "HTTPCode_ELB_504_Count",
                    "LoadBalancer",
                    "app/testALB2/e4fa21f252855f0f",
                    {"region": "ap-northeast-1"},
                ],
            ],
            "view": "timeSeries",
            "stacked": False,
            "region": "ap-northeast-1",
            "period": 60,
            "stat": "Sum",
        },
    },
    {
        "type": "metric",
        "x": 0,
        "y": 814,
        "width": 9,
        "height": 6,
        "properties": {
            "metrics": [
                [
                    "AWS/ApplicationELB",
                    "HTTPCode_ELB_503_Count",
                    "LoadBalancer",
                    "app/testALB/879c269ce5dd4542",
                    {"region": "ap-northeast-1"},
                ],
                [
                    "AWS/ApplicationELB",
                    "HTTPCode_ELB_503_Count",
                    "LoadBalancer",
                    "app/testALB2/e4fa21f252855f0f",
                    {"region": "ap-northeast-1"},
                ],
            ],
            "view": "timeSeries",
            "stacked": False,
            "region": "ap-northeast-1",
            "period": 60,
            "stat": "Sum",
        },
    },
    {
        "type": "metric",
        "x": 9,
        "y": 820,
        "width": 9,
        "height": 6,
        "properties": {
            "metrics": [
                [
                    "AWS/ApplicationELB",
                    "UnHealthyHostCount",
                    "TargetGroup",
                    "targetgroup/http/384c8e9d1fec2487",
                    "LoadBalancer",
                    "app/testALB/879c269ce5dd4542",
                    {"region": "ap-northeast-1"},
                ],
                [
                    "AWS/ApplicationELB",
                    "UnHealthyHostCount",
                    "TargetGroup",
                    "targetgroup/http2/384c8e9d1fec2487",
                    "LoadBalancer",
                    "app/testALB/879c269ce5dd4542",
                    {"region": "ap-northeast-1"},
                ],
            ],
            "view": "timeSeries",
            "stacked": False,
            "region": "ap-northeast-1",
            "stat": "Average",
            "period": 60,
        },
    },
    {
        "type": "metric",
        "x": 0,
        "y": 820,
        "width": 9,
        "height": 6,
        "properties": {
            "metrics": [
                [
                    "AWS/ApplicationELB",
                    "HealthyHostCount",
                    "TargetGroup",
                    "targetgroup/http/384c8e9d1fec2487",
                    "LoadBalancer",
                    "app/testALB/879c269ce5dd4542",
                    {"region": "ap-northeast-1"},
                ],
                [
                    "AWS/ApplicationELB",
                    "HealthyHostCount",
                    "TargetGroup",
                    "targetgroup/http2/384c8e9d1fec2487",
                    "LoadBalancer",
                    "app/testALB/879c269ce5dd4542",
                    {"region": "ap-northeast-1"},
                ],
            ],
            "view": "timeSeries",
            "stacked": False,
            "region": "ap-northeast-1",
            "stat": "Average",
            "period": 60,
        },
    },
]

clb_output_1 = [
    {
        "type": "text",
        "x": 0,
        "y": 714,
        "width": 18,
        "height": 2,
        "properties": {"markdown": "\n# Classic Load Balancer\n"},
    },
    {
        "type": "metric",
        "x": 0,
        "y": 716,
        "width": 9,
        "height": 6,
        "properties": {
            "view": "timeSeries",
            "stacked": False,
            "metrics": [
                [
                    "AWS/ELB",
                    "HealthyHostCount",
                    "LoadBalancerName",
                    "testELB",
                    {"region": "ap-northeast-1"},
                ],
                [
                    "AWS/ELB",
                    "HealthyHostCount",
                    "LoadBalancerName",
                    "testELB2",
                    {"region": "ap-northeast-1"},
                ],
            ],
            "region": "ap-northeast-1",
        },
    },
    {
        "type": "metric",
        "x": 9,
        "y": 716,
        "width": 9,
        "height": 6,
        "properties": {
            "view": "timeSeries",
            "stacked": False,
            "metrics": [
                [
                    "AWS/ELB",
                    "UnHealthyHostCount",
                    "LoadBalancerName",
                    "testELB",
                    {"region": "ap-northeast-1"},
                ],
                [
                    "AWS/ELB",
                    "UnHealthyHostCount",
                    "LoadBalancerName",
                    "testELB2",
                    {"region": "ap-northeast-1"},
                ],
            ],
            "region": "ap-northeast-1",
        },
    },
    {
        "type": "metric",
        "x": 0,
        "y": 722,
        "width": 9,
        "height": 6,
        "properties": {
            "view": "timeSeries",
            "stacked": False,
            "metrics": [
                [
                    "AWS/ELB",
                    "RequestCount",
                    "LoadBalancerName",
                    "testELB",
                    {"region": "ap-northeast-1"},
                ],
                [
                    "AWS/ELB",
                    "RequestCount",
                    "LoadBalancerName",
                    "testELB2",
                    {"region": "ap-northeast-1"},
                ],
            ],
            "region": "ap-northeast-1",
            "stat": "Sum",
            "period": 300,
        },
    },
    {
        "type": "metric",
        "x": 9,
        "y": 722,
        "width": 9,
        "height": 6,
        "properties": {
            "metrics": [
                [
                    "AWS/ELB",
                    "Latency",
                    "LoadBalancerName",
                    "testELB",
                    {"region": "ap-northeast-1"},
                ],
                [
                    "AWS/ELB",
                    "Latency",
                    "LoadBalancerName",
                    "testELB2",
                    {"region": "ap-northeast-1"},
                ],
            ],
            "view": "timeSeries",
            "stacked": False,
            "region": "ap-northeast-1",
            "period": 300,
            "yAxis": {"left": {"showUnits": True}},
        },
    },
    {
        "type": "metric",
        "x": 0,
        "y": 728,
        "width": 9,
        "height": 6,
        "properties": {
            "view": "timeSeries",
            "stacked": False,
            "stat": "Maximum",
            "metrics": [
                [
                    "AWS/ELB",
                    "SurgeQueueLength",
                    "LoadBalancerName",
                    "testELB",
                    {"region": "ap-northeast-1"},
                ],
                [
                    "AWS/ELB",
                    "SurgeQueueLength",
                    "LoadBalancerName",
                    "testELB2",
                    {"region": "ap-northeast-1"},
                ],
            ],
            "region": "ap-northeast-1",
        },
    },
    {
        "type": "metric",
        "x": 9,
        "y": 728,
        "width": 9,
        "height": 6,
        "properties": {
            "metrics": [
                [
                    "AWS/ELB",
                    "BackendConnectionErrors",
                    "LoadBalancerName",
                    "testELB",
                    {"region": "ap-northeast-1"},
                ],
                [
                    "AWS/ELB",
                    "BackendConnectionErrors",
                    "LoadBalancerName",
                    "testELB2",
                    {"region": "ap-northeast-1"},
                ],
            ],
            "view": "timeSeries",
            "stacked": False,
            "region": "ap-northeast-1",
            "stat": "Sum",
            "period": 300,
        },
    },
    {
        "type": "metric",
        "x": 9,
        "y": 734,
        "width": 9,
        "height": 6,
        "properties": {
            "metrics": [
                [
                    "AWS/ELB",
                    "HTTPCode_Backend_5XX",
                    "LoadBalancerName",
                    "testELB",
                    {"region": "ap-northeast-1"},
                ],
                [
                    "AWS/ELB",
                    "HTTPCode_Backend_5XX",
                    "LoadBalancerName",
                    "testELB2",
                    {"region": "ap-northeast-1"},
                ],
            ],
            "view": "timeSeries",
            "stacked": False,
            "region": "ap-northeast-1",
            "stat": "Sum",
            "period": 300,
        },
    },
    {
        "type": "metric",
        "x": 0,
        "y": 734,
        "width": 9,
        "height": 6,
        "properties": {
            "metrics": [
                [
                    "AWS/ELB",
                    "HTTPCode_ELB_5XX",
                    "LoadBalancerName",
                    "testELB",
                    {"region": "ap-northeast-1"},
                ],
                [
                    "AWS/ELB",
                    "HTTPCode_ELB_5XX",
                    "LoadBalancerName",
                    "testELB2",
                    {"region": "ap-northeast-1"},
                ],
            ],
            "view": "timeSeries",
            "stacked": False,
            "region": "ap-northeast-1",
            "stat": "Sum",
            "period": 300,
        },
    },
]

cloudfront_output_1 = [
    {
        "type": "text",
        "x": 0,
        "y": 600,
        "width": 18,
        "height": 2,
        "properties": {"markdown": "\n# CloudFront\n"},
    },
    {
        "type": "metric",
        "x": 0,
        "y": 602,
        "width": 9,
        "height": 6,
        "properties": {
            "metrics": [
                [
                    "AWS/CloudFront",
                    "Requests",
                    "Region",
                    "Global",
                    "DistributionId",
                    "testDistribution1",
                    {"region": "us-east-1"},
                ],
                [
                    "AWS/CloudFront",
                    "Requests",
                    "Region",
                    "Global",
                    "DistributionId",
                    "testDistribution2",
                    {"region": "us-east-1"},
                ],
            ],
            "view": "timeSeries",
            "stacked": False,
            "region": "us-east-1",
            "stat": "Sum",
            "period": 300,
        },
    },
    {
        "type": "metric",
        "x": 9,
        "y": 602,
        "width": 9,
        "height": 6,
        "properties": {
            "view": "timeSeries",
            "stacked": False,
            "metrics": [
                [
                    "AWS/CloudFront",
                    "5xxErrorRate",
                    "Region",
                    "Global",
                    "DistributionId",
                    "testDistribution1",
                    {"region": "us-east-1"},
                ],
                [
                    "AWS/CloudFront",
                    "5xxErrorRate",
                    "Region",
                    "Global",
                    "DistributionId",
                    "testDistribution2",
                    {"region": "us-east-1"},
                ],
            ],
            "region": "us-east-1",
            "period": 300,
        },
    },
    {
        "type": "metric",
        "x": 0,
        "y": 608,
        "width": 9,
        "height": 6,
        "properties": {
            "view": "timeSeries",
            "stacked": False,
            "metrics": [
                [
                    "AWS/CloudFront",
                    "4xxErrorRate",
                    "Region",
                    "Global",
                    "DistributionId",
                    "testDistribution1",
                    {"region": "us-east-1"},
                ],
                [
                    "AWS/CloudFront",
                    "4xxErrorRate",
                    "Region",
                    "Global",
                    "DistributionId",
                    "testDistribution2",
                    {"region": "us-east-1"},
                ],
            ],
            "region": "us-east-1",
        },
    },
]

ec2_output_1 = [
        {
            "type": "metric",
            "x": 0,
            "y": 2,
            "width": 9,
            "height": 6,
            "properties": {
                "metrics": [
                    [ "AWS/EC2", "StatusCheckFailed_Instance", "InstanceId", "i-0f8f8f8f8f8f8f8f8",{"region": "us-east-1"} ],
                    [ "AWS/EC2", "StatusCheckFailed_Instance", "InstanceId", "i-9f9f9f9f9f9f9f9f9",{"region": "us-east-1"} ],
                    [ "AWS/EC2", "StatusCheckFailed_Instance", "InstanceId", "i-0a0a0a0a0a0a0a0a0",{"region": "us-east-2"} ],
                    [ "AWS/EC2", "StatusCheckFailed_Instance", "InstanceId", "i-0b0b0b0b0b0b0b0b0",{"region": "us-east-2"} ],
                ],
                "view": "timeSeries",
                "stacked": False,
                "region": "us-east-2",
                "period": 300,
                "stat": "Sum"
            }
        },
        {
            "type": "metric",
            "x": 9,
            "y": 14,
            "width": 9,
            "height": 6,
            "properties": {
                "metrics": [
                    [ "AWS/EC2", "CPUSurplusCreditBalance", "InstanceId", "i-0f8f8f8f8f8f8f8f8",{"region": "us-east-1"} ],
                    [ "AWS/EC2", "CPUSurplusCreditBalance", "InstanceId", "i-9f9f9f9f9f9f9f9f9",{"region": "us-east-1"} ],
                    [ "AWS/EC2", "CPUSurplusCreditBalance", "InstanceId", "i-0a0a0a0a0a0a0a0a0",{"region": "us-east-2"} ],
                    [ "AWS/EC2", "CPUSurplusCreditBalance", "InstanceId", "i-0b0b0b0b0b0b0b0b0",{"region": "us-east-2"} ],
                ],
                "view": "timeSeries",
                "stacked": False,
                "region": "us-east-2",
                "period": 300,
                "stat": "Maximum"
            }
        },
        {
            "type": "metric",
            "x": 9,
            "y": 20,
            "width": 9,
            "height": 6,
            "properties": {
                "metrics": [
                    [ "AWS/EC2", "NetworkOut", "InstanceId", "i-0f8f8f8f8f8f8f8f8",{"region": "us-east-1"} ],
                    [ "AWS/EC2", "NetworkOut", "InstanceId", "i-9f9f9f9f9f9f9f9f9",{"region": "us-east-1"} ],
                    [ "AWS/EC2", "NetworkOut", "InstanceId", "i-0a0a0a0a0a0a0a0a0",{"region": "us-east-2"} ],
                    [ "AWS/EC2", "NetworkOut", "InstanceId", "i-0b0b0b0b0b0b0b0b0",{"region": "us-east-2"} ],
                ],
                "view": "timeSeries",
                "stacked": False,
                "region": "us-east-2",
                "period": 300,
                "stat": "Sum"
            }
        },
        {
            "type": "text",
            "x": 0,
            "y": 0,
            "width": 18,
            "height": 2,
            "properties": {
                "markdown": "\n# EC2\n"
            }
        },
        {
            "type": "metric",
            "x": 9,
            "y": 2,
            "width": 9,
            "height": 6,
            "properties": {
                "metrics": [
                    [ "AWS/EC2", "StatusCheckFailed_System", "InstanceId", "i-0f8f8f8f8f8f8f8f8",{"region": "us-east-1"} ],
                    [ "AWS/EC2", "StatusCheckFailed_System", "InstanceId", "i-9f9f9f9f9f9f9f9f9",{"region": "us-east-1"} ],
                    [ "AWS/EC2", "StatusCheckFailed_System", "InstanceId", "i-0a0a0a0a0a0a0a0a0",{"region": "us-east-2"} ],
                    [ "AWS/EC2", "StatusCheckFailed_System", "InstanceId", "i-0b0b0b0b0b0b0b0b0",{"region": "us-east-2"} ],
                ],
                "view": "timeSeries",
                "stacked": False,
                "region": "us-east-2",
                "stat": "Sum",
                "period": 300
            }
        },
        {
            "type": "metric",
            "x": 0,
            "y": 8,
            "width": 9,
            "height": 6,
            "properties": {
                "metrics": [
                    [ "AWS/EC2", "CPUUtilization", "InstanceId", "i-0f8f8f8f8f8f8f8f8",{"region": "us-east-1"} ],
                    [ "AWS/EC2", "CPUUtilization", "InstanceId", "i-9f9f9f9f9f9f9f9f9",{"region": "us-east-1"} ],
                    [ "AWS/EC2", "CPUUtilization", "InstanceId", "i-0a0a0a0a0a0a0a0a0",{"region": "us-east-2"} ],
                    [ "AWS/EC2", "CPUUtilization", "InstanceId", "i-0b0b0b0b0b0b0b0b0",{"region": "us-east-2"} ],
                ],
                "view": "timeSeries",
                "stacked": False,
                "region": "us-east-2",
                "stat": "Maximum",
                "period": 300
            }
        },
        {
            "type": "metric",
            "x": 9,
            "y": 8,
            "width": 9,
            "height": 6,
            "properties": {
                "metrics": [
                    [ "AWS/EC2", "CPUCreditUsage", "InstanceId", "i-0f8f8f8f8f8f8f8f8",{"region": "us-east-1"} ],
                    [ "AWS/EC2", "CPUCreditUsage", "InstanceId", "i-9f9f9f9f9f9f9f9f9",{"region": "us-east-1"} ],
                    [ "AWS/EC2", "CPUCreditUsage", "InstanceId", "i-0a0a0a0a0a0a0a0a0",{"region": "us-east-2"} ],
                    [ "AWS/EC2", "CPUCreditUsage", "InstanceId", "i-0b0b0b0b0b0b0b0b0",{"region": "us-east-2"} ],
                ],
                "view": "timeSeries",
                "stacked": False,
                "region": "us-east-2",
                "period": 300,
                "stat": "Maximum"
            }
        },
        {
            "type": "metric",
            "x": 0,
            "y": 14,
            "width": 9,
            "height": 6,
            "properties": {
                "metrics": [
                    [ "AWS/EC2", "CPUCreditBalance", "InstanceId", "i-0f8f8f8f8f8f8f8f8",{"region": "us-east-1"} ],
                    [ "AWS/EC2", "CPUCreditBalance", "InstanceId", "i-9f9f9f9f9f9f9f9f9",{"region": "us-east-1"} ],
                    [ "AWS/EC2", "CPUCreditBalance", "InstanceId", "i-0a0a0a0a0a0a0a0a0",{"region": "us-east-2"} ],
                    [ "AWS/EC2", "CPUCreditBalance", "InstanceId", "i-0b0b0b0b0b0b0b0b0",{"region": "us-east-2"} ],
                ],
                "view": "timeSeries",
                "stacked": False,
                "region": "us-east-2",
                "period": 300,
                "stat": "Minimum"
            }
        },
        {
            "type": "metric",
            "x": 0,
            "y": 20,
            "width": 9,
            "height": 6,
            "properties": {
                "metrics": [
                    [ "AWS/EC2", "NetworkIn", "InstanceId", "i-0f8f8f8f8f8f8f8f8",{"region": "us-east-1"} ],
                    [ "AWS/EC2", "NetworkIn", "InstanceId", "i-9f9f9f9f9f9f9f9f9",{"region": "us-east-1"} ],
                    [ "AWS/EC2", "NetworkIn", "InstanceId", "i-0a0a0a0a0a0a0a0a0",{"region": "us-east-2"} ],
                    [ "AWS/EC2", "NetworkIn", "InstanceId", "i-0b0b0b0b0b0b0b0b0",{"region": "us-east-2"} ],
                ],
                "view": "timeSeries",
                "stacked": False,
                "region": "us-east-2",
                "period": 300,
                "stat": "Sum"
            }
        }
]

s3_output = [
    {
        "height": 6,
        "width": 6,
        "y": 1600,
        "x": 0,
        "type": "metric",
        "properties": {
            "metrics": [
                [ "AWS/S3", "4xxErrors", "BucketName", "examplebucket1-use1", "FilterId", "examplebucket1-use1", { "region": "us-east-1" } ],
                [ "AWS/S3", "4xxErrors", "BucketName", "examplebucket2-use1", "FilterId", "examplebucket2-use1", { "region": "us-east-1" } ],
                [ "AWS/S3", "4xxErrors", "BucketName", "examplebucket1-use2", "FilterId", "examplebucket1-use2", { "region": "us-east-2" } ],
            ],
            "view": "timeSeries",
            "stacked": False,
            "region": "us-east-2",
            "period": 300,
            "stat": "Sum"
        }
    },
    {
        "height": 6,
        "width": 6,
        "y": 1600,
        "x": 6,
        "type": "metric",
        "properties": {
            "metrics": [
                [ "AWS/S3", "5xxErrors", "BucketName", "examplebucket1-use1", "FilterId", "examplebucket1-use1", { "region": "us-east-1" } ],
                [ "AWS/S3", "5xxErrors", "BucketName", "examplebucket2-use1", "FilterId", "examplebucket2-use1", { "region": "us-east-1" } ],
                [ "AWS/S3", "5xxErrors", "BucketName", "examplebucket1-use2", "FilterId", "examplebucket1-use2", { "region": "us-east-2" } ],
            ],
            "view": "timeSeries",
            "stacked": False,
            "region": "us-east-2",
            "period": 300,
            "stat": "Sum"
        }
    },
    {
        "height": 6,
        "width": 6,
        "y": 1600,
        "x": 12,
        "type": "metric",
        "properties": {
            "metrics": [
                [ "AWS/S3", "AllRequests", "BucketName", "examplebucket1-use1", "FilterId", "examplebucket1-use1", { "region": "us-east-1" } ],
                [ "AWS/S3", "AllRequests", "BucketName", "examplebucket2-use1", "FilterId", "examplebucket2-use1", { "region": "us-east-1" } ],
                [ "AWS/S3", "AllRequests", "BucketName", "examplebucket1-use2", "FilterId", "examplebucket1-use2", { "region": "us-east-2" } ],
            ],
            "view": "timeSeries",
            "stacked": False,
            "region": "us-east-2",
            "period": 300,
            "stat": "Sum"
        }
    },
    {
        "height": 6,
        "width": 6,
        "y": 1600,
        "x": 18,
        "type": "metric",
        "properties": {
            "metrics": [
                [ "AWS/S3", "ListRequests", "BucketName", "examplebucket1-use1", "FilterId", "examplebucket1-use1", { "region": "us-east-1" } ],
                [ "AWS/S3", "ListRequests", "BucketName", "examplebucket2-use1", "FilterId", "examplebucket2-use1", { "region": "us-east-1" } ],
                [ "AWS/S3", "ListRequests", "BucketName", "examplebucket1-use2", "FilterId", "examplebucket1-use2", { "region": "us-east-2" } ],
            ],
            "view": "timeSeries",
            "stacked": False,
            "region": "us-east-2",
            "period": 300,
            "stat": "Sum"
        }
    },
    {
        "height": 6,
        "width": 6,
        "y": 1606,
        "x": 0,
        "type": "metric",
        "properties": {
            "metrics": [
                [ "AWS/S3", "PutRequests", "BucketName", "examplebucket1-use1", "FilterId", "examplebucket1-use1", { "region": "us-east-1" } ],
                [ "AWS/S3", "PutRequests", "BucketName", "examplebucket2-use1", "FilterId", "examplebucket2-use1", { "region": "us-east-1" } ],
                [ "AWS/S3", "PutRequests", "BucketName", "examplebucket1-use2", "FilterId", "examplebucket1-use2", { "region": "us-east-2" } ],
            ],
            "view": "timeSeries",
            "stacked": False,
            "region": "us-east-2",
            "period": 300,
            "stat": "Average"
        }
    },
    {
        "height": 6,
        "width": 6,
        "y": 1606,
        "x": 6,
        "type": "metric",
        "properties": {
            "metrics": [
                [ "AWS/S3", "HeadRequests", "BucketName", "examplebucket1-use1", "FilterId", "examplebucket1-use1", { "region": "us-east-1" } ],
                [ "AWS/S3", "HeadRequests", "BucketName", "examplebucket2-use1", "FilterId", "examplebucket2-use1", { "region": "us-east-1" } ],
                [ "AWS/S3", "HeadRequests", "BucketName", "examplebucket1-use2", "FilterId", "examplebucket1-use2", { "region": "us-east-2" } ],
            ],
            "view": "timeSeries",
            "stacked": False,
            "region": "us-east-2",
            "stat": "Sum",
            "period": 300
        }
    },
    {
        "height": 6,
        "width": 6,
        "y": 1606,
        "x": 12,
        "type": "metric",
        "properties": {
            "metrics": [
                [ "AWS/S3", "DeleteRequests", "BucketName", "examplebucket1-use1", "FilterId", "examplebucket1-use1", { "region": "us-east-1" } ],
                [ "AWS/S3", "DeleteRequests", "BucketName", "examplebucket2-use1", "FilterId", "examplebucket2-use1", { "region": "us-east-1" } ],
                [ "AWS/S3", "DeleteRequests", "BucketName", "examplebucket1-use2", "FilterId", "examplebucket1-use2", { "region": "us-east-2" } ],
            ],
            "view": "timeSeries",
            "stacked": False,
            "region": "us-east-2",
            "period": 300,
            "stat": "Sum"
        }
    },
    {
        "height": 6,
        "width": 6,
        "y": 1606,
        "x": 18,
        "type": "metric",
        "properties": {
            "metrics": [
                [ "AWS/S3", "HeadRequests", "BucketName", "examplebucket1-use1", "FilterId", "examplebucket1-use1", { "region": "us-east-1" } ],
                [ "AWS/S3", "HeadRequests", "BucketName", "examplebucket2-use1", "FilterId", "examplebucket2-use1", { "region": "us-east-1" } ],
                [ "AWS/S3", "HeadRequests", "BucketName", "examplebucket1-use2", "FilterId", "examplebucket1-use2", { "region": "us-east-2" } ],
            ],
            "view": "timeSeries",
            "stacked": False,
            "region": "us-east-2",
            "period": 300,
            "stat": "Sum"
        }
    },
    {
        "height": 6,
        "width": 6,
        "y": 1618,
        "x": 0,
        "type": "metric",
        "properties": {
            "metrics": [
                [ "AWS/S3", "BytesUploaded", "BucketName", "examplebucket1-use1", "FilterId", "examplebucket1-use1", { "region": "us-east-1" } ],
                [ "AWS/S3", "BytesUploaded", "BucketName", "examplebucket2-use1", "FilterId", "examplebucket2-use1", { "region": "us-east-1" } ],
                [ "AWS/S3", "BytesUploaded", "BucketName", "examplebucket1-use2", "FilterId", "examplebucket1-use2", { "region": "us-east-2" } ],
            ],
            "view": "timeSeries",
            "stacked": False,
            "region": "us-east-2",
            "stat": "Sum",
            "period": 300
        }
    },
    {
        "height": 6,
        "width": 6,
        "y": 1612,
        "x": 6,
        "type": "metric",
        "properties": {
            "metrics": [
                [ "AWS/S3", "BytesDownloaded", "BucketName", "examplebucket1-use1", "FilterId", "examplebucket1-use1", { "region": "us-east-1" } ],
                [ "AWS/S3", "BytesDownloaded", "BucketName", "examplebucket2-use1", "FilterId", "examplebucket2-use1", { "region": "us-east-1" } ],
                [ "AWS/S3", "BytesDownloaded", "BucketName", "examplebucket1-use2", "FilterId", "examplebucket1-use2", { "region": "us-east-2" } ],
            ],
            "view": "timeSeries",
            "stacked": False,
            "region": "us-east-2",
            "stat": "Sum",
            "period": 300
        }
    },
    {
        "height": 6,
        "width": 6,
        "y": 1612,
        "x": 12,
        "type": "metric",
        "properties": {
            "view": "timeSeries",
            "stacked": False,
            "metrics": [
                [ "AWS/S3", "FirstByteLatency", "BucketName", "examplebucket1-use1", "FilterId", "examplebucket1-use1", { "region": "us-east-1" } ],
                [ "AWS/S3", "FirstByteLatency", "BucketName", "examplebucket2-use1", "FilterId", "examplebucket2-use1", { "region": "us-east-1" } ],
                [ "AWS/S3", "FirstByteLatency", "BucketName", "examplebucket1-use2", "FilterId", "examplebucket1-use2", { "region": "us-east-2" } ],
            ],
            "region": "us-east-2",
            "period": 300
        }
    },
    {
        "height": 6,
        "width": 6,
        "y": 1612,
        "x": 18,
        "type": "metric",
        "properties": {
            "view": "timeSeries",
            "stacked": False,
            "metrics": [
                [ "AWS/S3", "TotalRequestLatency", "BucketName", "examplebucket1-use1", "FilterId", "examplebucket1-use1", { "region": "us-east-1" } ],
                [ "AWS/S3", "TotalRequestLatency", "BucketName", "examplebucket2-use1", "FilterId", "examplebucket2-use1", { "region": "us-east-1" } ],
                [ "AWS/S3", "TotalRequestLatency", "BucketName", "examplebucket1-use2", "FilterId", "examplebucket1-use2", { "region": "us-east-2" } ],
            ],
            "region": "us-east-2",
            "period": 300
        }
    },
    {
        "height": 6,
        "width": 6,
        "y": 1612,
        "x": 0,
        "type": "metric",
        "properties": {
            "view": "timeSeries",
            "stacked": False,
            "metrics": [
                [ "AWS/S3", "PostRequests", "BucketName", "examplebucket1-use1", "FilterId", "examplebucket1-use1", { "region": "us-east-1" } ],
                [ "AWS/S3", "PostRequests", "BucketName", "examplebucket2-use1", "FilterId", "examplebucket2-use1", { "region": "us-east-1" } ],
                [ "AWS/S3", "PostRequests", "BucketName", "examplebucket1-use2", "FilterId", "examplebucket1-use2", { "region": "us-east-2" } ],
            ],
            "region": "us-east-2",
            "period": 300
        }
    }
]