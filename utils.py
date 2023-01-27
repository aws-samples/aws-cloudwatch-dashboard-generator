# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

from io import TextIOWrapper
from json import dump as json_dump
from json import load as json_load

from numpy import in1d as np_in1d
from numpy import ndarray as np_ndarray
from pandas import isnull as pd_isnull
from pandas import read_csv as pd_read_csv
from pandas.core.frame import DataFrame
from yaml import safe_load as yaml_safe_load

import get_filepath

FIRST_DIM_NAME = "dim1_name"
FIRST_DIM_VALUE = "dim1_value"
SECOND_DIM_NAME = "dim2_name"
SECOND_DIM_VALUE = "dim2_value"


def yaml_to_dict(input_file: TextIOWrapper) -> dict:
    input_file = yaml_safe_load(input_file)
    return input_file


def json_to_dict(input_file_path: str) -> dict:
    with open(input_file_path, "r") as stream:
        input_file = json_load(stream)
    return input_file


def read_csv(input_file: TextIOWrapper) -> DataFrame:
    df = pd_read_csv(input_file, dtype=object, skipinitialspace=True)
    input_file = _csv_resources_to_dict(df)
    return input_file


def write_json_file(output_file: TextIOWrapper, payload: dict):
    json_dump(payload, output_file)


def has_key(target: dict, key: str) -> bool:
    if key in target.keys():
        return True
    return False


def _csv_resources_to_dict(df: DataFrame) -> dict:
    '''
    Converts a CSV file to a dictionary.
    args:
        df: DataFrame, the CSV file to convert.
    '''
    region_list = json_to_dict(get_filepath.ROOT_DIR + "/definitions/Regions.json")

    input_file = {}
    services: list = df["service"].unique()
    for service in services:
        input_file[service] = {"Resources": {}}

        unique_regions: np_ndarray = (
            df.groupby("service").get_group(service)["region_code"].unique()
        )
        contained_regions = unique_regions[np_in1d(unique_regions, region_list)]
        for region in contained_regions:
            input_file[service]["Resources"][region] = []

            resources_in_region = (
                df.groupby("service")
                .get_group(service)
                .groupby("region_code")
                .get_group(region)
                .iloc()
            )
            for resource in resources_in_region:
                res_dict = {}
                res_dict[resource[FIRST_DIM_NAME]] = resource[FIRST_DIM_VALUE]
                if not pd_isnull(resource[SECOND_DIM_NAME]):
                    # If the second dimension is not null, add it to the dict
                    res_dict.setdefault(resource[SECOND_DIM_NAME], []).extend([resource[SECOND_DIM_VALUE]])
                input_file[service]["Resources"][region].append(res_dict)

    return input_file
