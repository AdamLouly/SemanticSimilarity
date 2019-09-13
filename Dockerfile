FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3 python3-dev python3-pip
WORKDIR /src
COPY ./requirements.txt /src
RUN pip3 install -r requirements.txt
COPY . /src
RUN python3 starter.py
ENTRYPOINT ["python3"]
CMD ["index.py"]
