#!/usr/bin/env python3

import argparse
import json
import os
import sys
import subprocess
import tempfile
import time
from ingredient_phrase_tagger.training import utils

def safeStr(obj):
    try: return str(obj).encode('ascii', 'ignore').decode('ascii')
    except: return ""

def _exec_crf_test(input_text, model_path='/app/models/model.crfmodel'):

    try:
        with open('thefile', mode='w') as input_file:

            input_text = [safeStr(line) for line in input_text]

            input_file.write(utils.export_data(input_text))
            input_file.flush()
            return subprocess.check_output(
                ['crf_test', '--verbose=1', '--model', model_path,
                 input_file.name]).decode('utf-8')
    finally:
        try:
            os.remove('thefile')
        except:
            pass

def _convert_crf_output_to_json(crf_output):
    return utils.import_data(crf_output)


def main():
    # raw_ingredient_lines = ["1 (8 ounce) package cream cheese, softened", "3 cups salsa, divided", "4 green onions, chopped, divided", "2\u2009\u00bd cups Cheddar cheese, divided", "2\u2009\u00bd cups shredded Monterey Jack cheese, divided", "12 (8 inch) flour tortillas", "1 cup peanut butter", "1 cup white sugar", "1 egg", "1 cup butter flavored shortening", "\u00be cup white sugar", "\u00be cup brown sugar", "2 eggs", "2 teaspoons Mexican vanilla extract", "2\u2009\u00bc cups all-purpose flour", "1 teaspoon baking soda", "1 teaspoon salt", "2 cups milk chocolate chips", "3 tablespoons apricot preserves", "1 teaspoon fresh ginger paste (such as Gourmet Garden\u2122)", "\u00bd teaspoon minced fresh rosemary", "2 (8 ounce) boneless, skinless chicken breasts", "1 teaspoon vegetable oil", "salt and ground black pepper to taste", "\u00bd cup mayonnaise", "2 tablespoons Sriracha sauce", "1 pound bay scallops (about 36 small scallops)", "1 pinch coarse salt", "1 pinch freshly cracked black pepper", "12 slices bacon, cut into thirds", "1  serving olive oil cooking spray", "2 large russet potatoes, scrubbed", "1 tablespoon peanut oil", "\u00bd teaspoon coarse sea salt", "cooking spray", "\u00bd cup all-purpose flour", "\u00bc cup white sugar", "\u215b cup water", "1 large egg, separated", "1\u2009\u00bd teaspoons melted butter", "\u00bd teaspoon baking powder", "\u00bd teaspoon vanilla extract", "1 pinch salt", "2 tablespoons confectioners' sugar, or to taste", "1 red grapefruit, refrigerated", "1 tablespoon softened butter", "1 tablespoon brown sugar", "2 teaspoons brown sugar", "aluminum foil", "\u00bd teaspoon ground cinnamon", "2 tablespoons coarsely chopped pecans", "1 tablespoon brown sugar", "1 teaspoon all-purpose flour", "\u00bc teaspoon apple pie spice", "2 medium apples, cored and cut into wedges", "1 tablespoon butter, melted"]

    from folder_paths import input_folder,output_folder

    for file in os.listdir('/app/input_texts'):

        print("Processing "+file)

        with open(os.path.join(input_folder,file)) as f:
            raw_ingredient_lines = json.load(f)

        crf_output = _exec_crf_test(raw_ingredient_lines)
        crf_output = utils.import_data(crf_output.split('\n'))

        file_name = os.path.join(output_folder,file)

        with open(file_name, 'w') as f:
            json.dump(crf_output, f, ensure_ascii=False)

if __name__ == '__main__':

    main()
