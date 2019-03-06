FROM nikolaik/python-nodejs:python3.6-nodejs10

# Install Dependencies
# RUN apt-get update
# RUN apt-get install -y software-properties-common vim
# RUN add-apt-repository ppa:jonathonf/python-3.6
# RUN apt-get update
# RUN apt-get install -y build-essential python3.6 python3-pip
# RUN apt install curl -y
# RUN apt-get install nodejs -y
# RUN apt-get install npm -y


# Set up pip
# RUN python3.6 -m pip install pip --upgrade
# RUN python3.6 -m pip install wheel

# RUN npm install -g react-scripts
# RUN cd $(npm root -g)/npm && npm install fs-extra && sed -i -e s/graceful-fs/fs-extra/ -e s/fs.rename/fs.move/ ./lib/utils/rename.js

WORKDIR /app
COPY . /app
RUN cd client && npm install && npm run build

RUN pip3 install numpy
RUN pip3 install -r requirements.txt
