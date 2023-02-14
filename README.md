# AWS CloudWatch Dashboard Generator
[![License: MIT](https://img.shields.io/badge/License-MIT--0-yellow)](https://opensource.org/licenses/MIT-0)
[![AWS Provider](https://img.shields.io/badge/provider-AWS-orange?logo=amazon-aws&color=ff9900)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)

The purpose of this Python based command line tool is to generate a [CloudWatch Dashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html) which is based on a list of resources you provide and contains predefined useful CloudWatch metrics selected by AWS Support engineers for monitoring AWS resources during special events or [IEM (AWS Infrastructure Event Management)](https://aws.amazon.com/premiumsupport/programs/iem/) scenarios.

## Currently Supported AWS Resource Types
| Resource Types            | Supported?       |
| ------------------------- | ---------------- |
| Application Load Balancer | ✅                |
| Classic Load Balancer     | ✅                |
| CloudFront                | ✅                |
| EC2                       | ✅                |
| ElastiCache               | ✅                |
| Network Load Balancer     | ✅                |
| RDS                       | ✅                |
| NAT Gateway               | ✅                |
| Aurora                    | ✅                |
| Elastic Block Store       | Work in progress |
| EC2 Auto Scaling Groups   | Work in progress |

## Installation

### Prerequisites
- Python version 3.8

First install pip is the package installer for Python
```bash
$ python -m ensurepip --upgrade --user
```

```bash
If you have any issue to install pip, try using get-pip.py to install
1. Download the script, from https://bootstrap.pypa.io/get-pip.py.
2. Run get-pip.py
$ python get-pip.py

Troubleshooting

# If you run pip install but got error command not found: pip

It might indicated that your pip install path in not in env PATH, please reference WARNING message while install pip to find install path or try

$ /Users/${USER}/Library/Python/3.8/bin/pip install -r requirements.txt
Find more information at pip installation document: https://pip.pypa.io/en/stable/installation/
```

Install Dependencies
```bash
pip install -r requirements.txt
```

Then execute this tool.
```
$ python3 iemcwd.py -h
Usage: iemcwd.py [OPTIONS]

  IEMCWD is a tool to generate an IEM CloudWatch Dashboard based on
  resources you provide. The IEM CloudWatch Dashboard contains useful
  predefined metrics for IEM monitoring.

Options:
  -f, --file FILENAME         [required]
  -o, --output-file FILENAME  [required]
  -h, --help                  Show this message and exit.
```

## Usage

The tool is quite simple. It reads a CSV file to get your resource IDs, then output the dashboard JSON to the directory you specified.

### Using CSV file as an input

There is an example CSV file at `inputs/csv/example.csv` under this package for your reference. The table in CSV file must follow the format as below:

| service                | region_code   | dim1_name        | dim1_value        | dim2_name        | dim2_value        |
| ---------------------- | ------------- | ---------------- | ----------------- | ---------------- | ----------------- |
| *CloudWatch Namespace* | *region code* | *DimensionName1* | *DimensionValue1* | *DimensionName2* | *DimensionValue2* |

For the explanation of these attributes, see [below](#attribute-explaination) for more.

You may create a CSV file matching the columns and format above, or fill in `inputs/csv/fill-in.csv` with the resources you want to monitor on the dashboard. The order of entries(rows) in this table does not matter. The below is an example for the CSV input file, or refer to `inputs/csv/example.csv` in this repository. Though most of the service only requires one metric (`dim1_name` and `dim1_value` columns), please note that some services, including Elasticache, contain a second dimension entry `dim2_name` and `dim2_value`.

| service        | region_code    | dim1_name            | dim1_value                   | dim2_name   | dim2_value |
|----------------|----------------|----------------------|------------------------------|-------------|------------|
| ALB            | ap-northeast-1 | LoadBalancer         | app/my-alb1/1234567890123456 |             |            |
| NLB            | ap-northeast-1 | LoadBalancer         | net/my-nlb1/1234567890123456 |             |            |
| NAT            | ap-northeast-1 | NatGatewayId         | nat-0abcdef1234567890        |             |            |
| CloudFront     | us-east-1      | DistributionId       | EDFDVBD6EXAMPLE              |             |            |
| EC2            | ap-northeast-1 | InstanceId           | i-0abcdef1234567890          |             |            |
| RDS            | ap-northeast-1 | DBInstanceIdentifier | support-instance-1           |             |            |
| AuroraCluster  | ap-northeast-1 | DBClusterIdentifier  | cluster-001                  |             |            |
| AuroraInstance | ap-northeast-1 | DBInstanceIdentifier | instance-001                 |             |            |
| ElastiCache    | ap-northeast-1 | CacheClusterId       | support-001                  | CacheNodeId | 0001       |

Example:
```bash
python3 iemcwd.py -f inputs/csv/example.csv -o outputs/example_output.json

Successfully generated CloudWatch dashBoard JSON file.
```

After generating the dashboard JSON file, use the following AWS CLI command to create a CloudWatch based on this JSON file:

```bash
$ aws cloudwatch put-dashboard --dashboard-name your-iem-dashboard --dashboard-body file://outputs/example_output.json
```

You may also follow the below documentation to create the CloudWatch dashboard using AWS Console using the generated JSON:
- https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/add_old_metrics_to_graph.html

### Attribute explanation:

`service` should be one of the following:
- ALB
- CLB
- CloudFront
- EC2
- ElastiCache
- NLB
- RDS
- NAT
- AuroraCluster

`region_code` is the AWS region where your resource is located at. See [definitions/Regions.json](definitions/Regions.json) for a list of region code.

`dim1_name` and `dim1_value` is the dimension of a metric in Cloud Watch. A dimension is a name/value pair that is part of the identity of a metric.Take EC2 for example, the `dim1_name` is `InstanceId`, and `dim1_value` will be the instance ID. Some metrics may contain multiple dimensions, such as ElastiCache. Understanding each AWS service resource Dimension here:
https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.