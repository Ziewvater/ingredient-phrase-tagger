FROM mtlynch/crfpp

RUN apt-get update -y
RUN apt-get install -y git python3.9 python3-setuptools python3-pip
RUN rm -Rf /usr/share/doc
RUN rm -Rf /usr/share/man
RUN apt-get autoremove -y
RUN rm -rf /var/lib/apt/lists/*

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt
RUN pip3 install .

CMD python3 bin/parse-ingredients.py