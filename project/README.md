# Project

The main project for the 2018-2019 QMIND Music Team! This year, we created a neural network with the ability to generate a song given an image. There are many facets to this project, if you want to skip to how to run it locally click [here](#Usage). Otherwise keep reading!

# Background

## The Network

At the core of the project is an LSTM neural network. This network took much inspiration from an [article](https://towardsdatascience.com/how-to-generate-music-using-a-lstm-neural-network-in-keras-68786834d4c5) in [Towards Data Science](https://towardsdatascience.com/), however many modifications were made to make it fit our use case.

The network is trained with [data](./data) collected from [Spotify's Web API](https://developer.spotify.com/documentation/web-api/reference/) and stored in CSV format. As it stands currently, our dataset consists of 100 songs from the following [playlist](https://open.spotify.com/playlist/01nf53t2d5BaEYQyz2hnT6). From there, the cover artwork is downloaded in JPG format and the 30 second previews are downloaded in MP3 format for each song. The cover artwork is converted into an array using the [KAZE Algorithm](https://www.doc.ic.ac.uk/~ajd/Publications/alcantarilla_etal_eccv2012.pdf) and the songs are converted into MIDI format using the [Melodia algorithm](http://www.justinsalamon.com/melody-extraction.html). To see how this was implemented in Python, check out the [Library](./lib) folder.

## The Web App

To provide an interface for using our neural network, we made a web app. The web app allows users to upload photos from their phone or computer and receive a generated song from the neural network as output. All the song and image pairs are also displayed in a gallery for visitors to enjoy.

The back end of the application is a [Flask](http://flask.pocoo.org/) server. The server accepts requests through A REST API and is also connected to a Google Cloud Storage Bucket for storing image and audio files. The front end of the application is a [ReactJS](https://reactjs.org/) client.

# Usage

## Requirements

Before running our project locally, make sure your device has the following requirements:

- Python 3.6.x
- Pip
- [NodeJS & NPM](https://nodejs.org/en/) (for web app)
- [Docker](https://www.docker.com/) (optional, for web app)

To train the network, run

```bash
  $ python3 train.py
```

> Note: all bash commands should be run from the `project` folder and not the root of this repo

To run the web app, you will first need to create your own [Google Cloud Storage Bucket](https://cloud.google.com/storage/docs/creating-buckets) called `qmusicbucket`. Once you have done this, obtain a [service account key](https://cloud.google.com/iam/docs/creating-managing-service-account-keys) for your project. Create a JSON file at the root of this folder called `google-config.json` and paste the contents of the service account key in this file.

To run the app in development mode, run

```bash
  $ make dev
```

This will run the client with the [Webpack Development Server](https://webpack.js.org/configuration/dev-server/) which allows for hot reloading and easy debugging.

To run the app in production mode, run

```bash
  $ python3 server.py
```

The default port will be 4000, however this can be configured with the `PORT` environment variable.

# Contributing

If you wish to contribute to the project (and are not a member of the QMIND Music Team), follow the following steps:

1. Fork this repo 🍴
2. Clone it 👽
3. Execute the following commands and make a PR 🚀

```bash
  $ git checkout -b feature/add-new-stuff
  $ # Make some changes now
  $ # .
  $ # .
  $ # .
  $ git commit -am "Some changes"
  $ git push -u origin feature/add-new-stuff
```
