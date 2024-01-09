FROM nvcr.io/nvidia/pytorch:23.12-py3

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN python -m pip install --upgrade pip
RUN git clone https://github.com/TimDettmers/bitsandbytes.git
WORKDIR /app/bitsandbytes
RUN CUDA_VERSION=123 make cuda12x
RUN python setup.py install
RUN python -m bitsandbytes
WORKDIR /app
RUN pip install -r requirements.txt --no-build-isolation