#!/usr/bin/env python3

import json
import os
import subprocess
from tqdm import tqdm
from ingredient_phrase_tagger.training import utils
from folder_paths import input_folder, output_folder


def _exec_crf_test(
    input_text: str,
    model_path: str,
):
    try:
        with open("thefile", mode="w", encoding="utf-8") as input_file:
            # input_text = [safeStr(line) for line in input_text]

            input_file.write(utils.export_data(input_text))
            input_file.flush()
            return subprocess.check_output(
                ["crf_test", "--verbose=1", "--model", model_path, input_file.name]
            ).decode("utf-8")
    finally:
        try:
            os.remove("thefile")
        except:
            pass


def _convert_crf_output_to_json(crf_output: list[str]):
    return utils.import_data(crf_output)


def process_lines(ingredient_lines: list[str], model_path: str):
    crf_output = _exec_crf_test(
        input_text=ingredient_lines,
        model_path=model_path,
    )
    return _convert_crf_output_to_json(crf_output.split("\n"))


def crf_output_from_file(
    file: str,
    model_path: str,
):
    with open(os.path.join(input_folder, file), encoding="utf-8") as f:
        raw_ingredient_lines = json.load(f)
    return process_lines(
        ingredient_lines=raw_ingredient_lines,
        model_path=model_path,
    )


def main(
    input_folder: str = input_folder,
    output_folder: str = output_folder,
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

            file_name = os.path.join(output_folder, file)

            with open(file_name, "w", encoding="utf-8") as f:
                json.dump(crf_output, f, ensure_ascii=False)

            bar.update(1)


if __name__ == "__main__":
    main()
