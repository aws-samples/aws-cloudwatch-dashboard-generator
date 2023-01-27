# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

from io import TextIOWrapper

import click

import utils as utils
from cw_dashboard import Dashboard
from input_check import check_input_yaml_format

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])

@click.command(context_settings=CONTEXT_SETTINGS)
@click.option("-f", "--input_file", required=True, type=click.File('r'), help="Input resource .csv file")
@click.option("-o", "--output-file", required=True, type=click.File('w'), help="Output Amazon CloudWatch dashboard JSON file")
def main(input_file: TextIOWrapper, output_file: TextIOWrapper):
    """
    IEMCWD is a tool to generate an IEM CloudWatch Dashboard based on resources you provide.
    The IEM CloudWatch Dashboard contains useful predefined metrics for IEM monitoring.
    """
    file_exten = input_file.name.split(".")[-1]
    if file_exten == "yaml" or file_exten == "yml":
        input_dict = utils.yaml_to_dict(input_file)
        check_input_yaml_format(input_dict)
    elif file_exten == "csv":
        input_dict = utils.read_csv(input_file)
    else:
        input_dict = None
        error_msg = (
            "[Input file type error] Only YAML (.yaml/.yml) and CSV(.csv) are supported"
        )
        click.secho(error_msg, fg="red", err=True, bold=True)
        raise click.Abort

    dashboard = Dashboard(input_dict, output_file)
    dashboard.generate()
    click.secho(
        "\nSuccessfully generated CloudWatch dashBoard JSON file.\n", fg="green"
    )


if __name__ == "__main__":
    main()
