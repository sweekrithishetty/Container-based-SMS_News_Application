FROM ubuntu:18.04
RUN apt update; apt install -y gnupg2
COPY . /app
WORKDIR /app
RUN apt install -y python3-pip
RUN pip3 install -r requirements.txt
CMD ["python3", "app.py"]
