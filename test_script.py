import os

# os.system(' echo "1 milk" | docker-compose run --rm -i iparser bin/parse-ingredients.py')
os.system(' echo "1 milk" | docker run  --rm -i iparser bin/parse-ingredients.py')