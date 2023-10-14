#!/usr/bin/env fish

# A helper script to process ingredient lines and ingredient names

rm -rf app/output
mkdir -p app/output
poetry run python -m ingredient_phrase_tagger.run

# Create input files for ingredient names for double-processing
for file in app/output/*
    set -l names (cat $file | jq ".[] | .name")
    set -l joined_names (string join "," $names)

    # Write the processed names in input
    set -l filename (path basename $file | path change-extension "")
    set -l new_filename (printf "app/input/%s_names.json" $filename)
    printf "[%s]" $joined_names > $new_filename

    # Record new name files to be deleted later
    set -a cleanup_files $new_filename
end

# Process ingredient names
poetry run python -m ingredient_phrase_tagger.run

# Format output files
for file in app/output/*
    # Format JSON
    poetry run python -m json.tool $file $file

    # Remove lines with "display" key
    grep -v '"display":' $file | string collect > $file
end

# Clean up created input files to avoid polluting future runs
for filename in $cleanup_files
    rm $filename
end