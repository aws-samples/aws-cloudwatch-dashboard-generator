# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

from abc import ABC, abstractmethod
from itertools import filterfalse


class Resource(ABC):
    def __init__(self, input_file: dict):
        self.template = list()
        self.input_file: dict = input_file
        self.is_elbv2 = False
        self.is_cf = False
        self.is_elastic_cache = False

    @abstractmethod
    def write_template(self) -> list:
        pass

    @abstractmethod
    def _read_template(self):
        pass

    def _data_processing(self, namespace: str, dimension_value: str):
        for widgets in self.template:
            if widgets["type"] == "metric":
                metric = widgets["properties"]["metrics"][0]
                widgets["properties"]["metrics"] = []
                resources = self.input_file[namespace]["Resources"]
                for region in resources:
                    for resource in resources[region]:
                        if self.is_elbv2:
                            if (
                                metric[1] in ("UnHealthyHostCount", "HealthyHostCount")
                                and "TargetGroup" not in resource
                            ):
                                continue  # There is not target group in the input, skip it
                            else:
                                new_widget_list = self._get_lb_metric(
                                    metric, resource, region
                                )
                                widgets["properties"]["metrics"] += new_widget_list
                        elif self.is_cf:
                            new_widget = self._get_cf_metric(metric, resource)
                            widgets["properties"]["metrics"].append(new_widget)
                        elif self.is_elastic_cache:
                            new_widget = self._get_elastic_cache_metric(
                                metric, resource, region
                            )
                            widgets["properties"]["metrics"].append(new_widget)
                        else:
                            widgets["properties"]["metrics"].append(
                                [
                                    metric[0],  # Namespace
                                    metric[1],  # MetricName
                                    metric[2],  # DimensionName
                                    resource[dimension_value],  # DimensionValue
                                    {"region": region},
                                ]
                            )
                        # We specify regions under the scope of a metric instead of a widget
                        # widgets["properties"].pop("region", None)

                        # Fix Bug as CW still need region field at properties level to save dashboard
                        widgets["properties"]["region"] = region

                        # widgets["properties"]["title"] += " ({})".format(region)

        # we have to iterate the filled template again to check for empty metrics, and remove widgets if metrics are empty.
        for widgets in self.template[:]:
            if widgets["type"] == "metric":
                if len(widgets["properties"]["metrics"]) == 0:
                    self.template.remove(widgets)

    # ALB/NLB has different dimensions between different metrics
    def _get_lb_metric(self, metric_attr: list, resource: dict, region: str) -> list:
        if metric_attr[1] in ("UnHealthyHostCount", "HealthyHostCount"):
            TargetGroupList = []
            for tg in resource["TargetGroup"]:
                TargetGroupList.append(
                    [
                        metric_attr[0],  # Namespace
                        metric_attr[1],  # MetricName
                        metric_attr[2],  # TargetGroup
                        tg,  # TargetGroup ID
                        metric_attr[4],  # LoadBalancer
                        resource["LoadBalancer"],  # LoadBalancer ID
                        {"region": region},
                    ]
                )
            return TargetGroupList
        elif metric_attr[1] == "RequestCount":
            return [
                [
                    metric_attr[0],  # Namespace
                    metric_attr[1],  # MetricName
                    metric_attr[2],  # TargetGroup
                    resource["LoadBalancer"],  # TargetGroup ID,
                    {"region": region},
                ]
            ]
        else:
            return [
                [
                    metric_attr[0],  # Namespace
                    metric_attr[1],  # MetricName
                    metric_attr[2],  # TargetGroup
                    resource["LoadBalancer"],  # LoadBalancer ID
                    {"region": region},
                ]
            ]

    # CloudFront has multiple Dimensions
    def _get_cf_metric(self, metric_attr: list, resource: dict) -> list:
        return [
            metric_attr[0],  # Namespace
            metric_attr[1],  # MetricName
            metric_attr[2],  # DimensionName1
            metric_attr[3],  # DimensionValue1
            metric_attr[4],  # DimensionName2
            resource["DistributionId"],  # DimensionValue2
            {"region": "us-east-1"}, # CloudFront metric only has one region "us-east-1"
        ]

    def _get_elastic_cache_metric(
        self, metric_attr: list, resource: dict, region: str
    ) -> list:
        if metric_attr[1] in (
            "FreeableMemory",
            "NetworkBytesOut",
            "CurrConnections",
            "ReplicationLag",
        ):
            return [
                metric_attr[0],  # Namespace
                metric_attr[1],  # MetricName
                metric_attr[2],  # CacheClusterId
                resource["CacheClusterId"],  # LoadBalancer ID
                {"region": region},
            ]
        else:
            return [
                metric_attr[0],  # Namespace
                metric_attr[1],  # MetricName
                metric_attr[2],  # DimensionName1
                resource["CacheClusterId"],  # DimensionValue1
                metric_attr[4],  # DimensionName2
                resource["CacheNodeId"][0],  # DimensionValue2
                {"region": region},
            ]
