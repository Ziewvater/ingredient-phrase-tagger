#!/usr/bin/env python3
# encoding= utf-8

import os
import argparse
import json
import sys
import subprocess
import tempfile

from ingredient_phrase_tagger.training import utils



def _exec_crf_test(input_text, model_path):
    with tempfile.NamedTemporaryFile(mode='w',encoding='utf-8') as input_file:
        input_file.write(utils.export_data(input_text))
        input_file.flush()
        return subprocess.check_output(
            ['crf_test', '--verbose=1', '--model', model_path,
             input_file.name]).decode('utf-8')


def _convert_crf_output_to_json(crf_output):
    return json.dumps(utils.import_data(crf_output), indent=2, sort_keys=True)


def main(input_lines):
    crf_output = _exec_crf_test(input_lines, '../models/model.crfmodel')
    print(_convert_crf_output_to_json(crf_output.split('\n')))

def read_input_files():

    with open('/app/input_texts/ingredients.json') as f:
        stuff = json.load(f)



    main(stuff)

if __name__ == '__main__':

    read_input_files()

