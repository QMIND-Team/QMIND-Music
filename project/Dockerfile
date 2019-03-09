FROM nikolaik/python-nodejs:python3.6-nodejs10

# Set up working directory
WORKDIR /app
COPY . /app

# Set up client
RUN cd client && npm install && npm run build

# Install pip packages
RUN pip3 install numpy
RUN pip3 install -r requirements.txt

# Expose port for server
EXPOSE 80
ENV PORT=80

CMD ["python3", "server.py"]