#!/usr/bin/env python3

import argparse
import parse_ingredients

from folder_paths import input_folder, output_folder


def argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Parses ingredients",
    )

    parser.add_argument(
        "--input_folder",
        "-i",
        default=input_folder,
        help="Path to a directory containing the input files to be processed",
    )
    parser.add_argument(
        "--output_folder",
        "-o",
        default=output_folder,
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
