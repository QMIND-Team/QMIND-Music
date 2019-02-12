FROM ubuntu:16.04

# Install dependencies

RUN apt-get update
RUN apt-get install -y software-properties-common vim
RUN add-apt-repository ppa:jonathonf/python-3.6
RUN apt-get update
RUN apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv
RUN apt-get install -y wget
RUN apt-get install -y unzip
RUN apt-get install -y ffmpeg

# Update pip
RUN python3.6 -m pip install pip --upgrade
RUN python3.6 -m pip install wheel

RUN pip3 install numpy
RUN pip3 install vamp
RUN pip3 install librosa
RUN pip3 install scipy
RUN pip3 install midiutil

# Set up the files
WORKDIR /app
COPY . /app

RUN unzip MELODIA.zip -d /usr/local/lib/vamp
CMD ["python3.6", "create_midi_files.py"]
