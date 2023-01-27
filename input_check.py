# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

from click import secho, Abort

import utils, get_filepath

REGION_LIST_PATH = get_filepath.ROOT_DIR + "/definitions/Regions.json"
NAMESPACE_PATH = get_filepath.ROOT_DIR + "/definitions/CwNamespaces.json"

def check_input_yaml_format(input_file: dict):
    # Check for valid regions and resource types
    region_list = utils.json_to_dict(REGION_LIST_PATH)
    namespaces = utils.json_to_dict(NAMESPACE_PATH)

    err_flag = False

    for input_resource_type in input_file:
        if input_resource_type not in namespaces:
            error_msg = "[Input file format error] Resource Type not supported: \"{}\""
            secho(error_msg.format(input_resource_type), fg="red", err=True, bold=True)
            err_flag = True
        for region in input_file[input_resource_type]["Resources"]:
            if region not in region_list:
                error_msg = "[Input file format error] No such region: \"{}\""
                secho(error_msg.format(region), fg="red", err=True, bold=True)
                err_flag = True

    if err_flag:
        raise Abort

def check_imput_csv_format(input_file: dict):
    pass # TODO: