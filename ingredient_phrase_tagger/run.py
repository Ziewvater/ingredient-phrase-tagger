#!/usr/bin/env python3

import argparse
import os
from .processing.parse_ingredients import crf_output_from_file, write_crf_output
from .processing import folder_paths
from tqdm import tqdm


def argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Parses ingredients",
    )

    parser.add_argument(
        "--input_folder",
        "-i",
        default=folder_paths.input_folder,
        help="Path to a directory containing the input files to be processed",
    )
    parser.add_argument(
        "--output_folder",
        "-o",
        default=folder_paths.output_folder,
        help="Path to a directory where parsed ingredients are written",
    )
    parser.add_argument(
        "--model_path",
        "-m",
        default="bin/model/model.crfmodel",
        help="Path to the trained model to be used",
    )
    return parser


def parse_ingredients(
    input_folder: str = folder_paths.input_folder,
    output_folder: str = folder_paths.output_folder,
    model_path: str = "bin/model/model.crfmodel",
):
    """Read all the files in inputs folder, place a parsed file in with the same name in the output folder"""
    files = os.listdir(input_folder)
    files_in_output_folder = os.listdir(output_folder)

    with tqdm(total=len(files)) as bar:
        for file in files:
            # skip completed files
            if file in files_in_output_folder:
                continue

            crf_output = crf_output_from_file(
                file=file,
                model_path=model_path,
            )

            write_crf_output(
                crf_output=crf_output,
                output_folder=output_folder,
                filename=file,
            )

            bar.update(1)


def run():
    parser = argument_parser()
    args = parser.parse_args()
    parse_ingredients(
        input_folder=args.input_folder,
        output_folder=args.output_folder,
        model_path=args.model_path,
    )


if __name__ == "__main__":
    run()
