
FROM python:3.9-slim

# we probably need build tools?
RUN apt-get update \
    && apt-get install --yes --no-install-recommends \
    build-essential

# we need the requirements.txt file from prophet to be in the root of the project
# https://github.com/facebook/prophet/blob/main/python/requirements.txt
# WORKDIR /app
WORKDIR /home/node/app2
COPY . .

# first: install all required packages for pystan
RUN pip install --no-cache-dir --upgrade cython numpy
# second: install all required packages for prophet from their requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
# third: install prophet itself
RUN pip install --no-cache-dir --upgrade prophet

RUN pip install -U Flask

RUN pip install -U flask-cors
# to use async functions
# RUN pip install aioflask

RUN pip install  --upgrade plotly
# RUN pip install prophet

# RUN pin install waitress
# to use response for get response at axios
# RUN pip install -U flask-cores
RUN pip install Flask-RESTful

# ENTRYPOINT ["tail", "-f", "/dev/null"]
ENTRYPOINT ["python", "./finally.py"]
# ENTRYPOINT ["python", "./prophetlikeKatana.py"]

