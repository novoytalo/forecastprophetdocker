# FROM continuumio/anaconda3

# RUN python setup.py install
# RUN conda update --all --yes
# RUN conda create -n myenv
# RUN conda install -c anaconda python
# RUN conda install gcc_linux-64
# RUN conda install -c conda-forge fbprophet

# colocar o -y ? para dar sim direto
# conda create --name myenv 

#conda activate myenv


# RUN apt-get -y install libc-dev

# RUN pip install pip==19.1.1

# COPY python/requirements.txt .
# RUN pip install -r requirements.txt
# RUN pip install ipython==7.5.0

# COPY . .

# WORKDIR python

# RUN python setup.py install

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

RUN pip install  --upgrade plotly
# RUN pip install prophet



# WORKDIR /home/node/app2

RUN python finally.py
ENTRYPOINT ["tail", "-f", "/dev/null"]


