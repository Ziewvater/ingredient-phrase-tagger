#!/usr/bin/env python3

import argparse
from .processing import parse_ingredients
from .processing import folder_paths


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


def run():
    parser = argument_parser()
    args = parser.parse_args()
    parse_ingredients.main(
        input_folder=args.input_folder,
        output_folder=args.output_folder,
        model_path=args.model_path,
    )


if __name__ == "__main__":
    run()
