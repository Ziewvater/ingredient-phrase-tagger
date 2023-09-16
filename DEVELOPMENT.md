# Parts

* `bin/train_prod_model` will train a model and place it in a given output dir
  * if no given ouput dir, new model is written to current directory
* `bin/generate_data` seems to just run the ingredient generation process, I think for tests?
* `bin/parse_ingredients.py` processes ingredients in files found in directory set with the `bin/folder_paths.py` file

## Bookmarks

* `training/tokenizer.py` is where you can put new units and tokenize them
  * May need to do this with "centiliters"
* `training/utils.py` `singluarize()` may help with plural discrete ingredients, like `mint leaves` --> `mint leaf`
