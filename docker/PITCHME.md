---
marp: true
title: Docker playground
description: Docker stuff
theme: uncover
paginate: true
_paginate: false
---

![Marp bg 60%](https://www.docker.com/wp-content/uploads/2022/03/vertical-logo-monochromatic.png)

---

<!-- _backgroundColor: "#123" -->
<!-- _color: "#fff" -->
##### <!--fit--> 👉 Making your life easier:)
---
###  The name docker is used about:

1. Docker containerization technology
    - a container makes in possible to package and isolate applications with their entire runtime environment
2. The docker open source community 
3. The company docker
Also see [Redhat's post](https://www.redhat.com/en/topics/containers/what-is-docker)
---
# Installation
**Follow 🐋 for** 
[![For Linux h:1.5em](https://upload.wikimedia.org/wikipedia/commons/3/35/Tux.svg)](https://docs.docker.com/engine/install/ubuntu/), [![Windows h:1.5em](https://upload.wikimedia.org/wikipedia/commons/6/6d/Windows_Logo_%281992-2001%29.svg)](https://docs.p.niva.no/guides/devenv.html), [![Apple h:1.5em](https://upload.wikimedia.org/wikipedia/commons/f/fa/Apple_logo_black.svg)](https://github.com/abiosoft/colima/#installation)
**Or**
[![Docker desktop h:2em](https://i2.wp.com/ralphmcneal.com/wp-content/uploads/2018/11/docker-desk-banner1.png?fit=770%2C403&ssl=1)](https://www.docker.com/products/docker-desktop/)
**Or install** 
[![podman h:2em](https://raw.githubusercontent.com/containers/common/main/logos/podman-logo-full-vert.png)](https://podman.io/) 
**for your distro**

---
<!-- _backgroundColor: "#123" -->
<!-- _color: "#fff" -->
# Getting started

``` bash
docker run hello-world
```
``` bash
docker --help
```
###### A lot of options! The most important commands are 
###### **build**, **images**, **pull**, **run**, **exec**, **ps** and **stop**
---
# Getting started

###### IMPORTANT❗❗

## Install  [docker autocomplete](https://docs.docker.com/compose/completion/)
---
<!-- _backgroundColor: "#123" -->
<!-- _color: "#fff" -->

#  <!--fit--> Using containers 🐛

``` bash
docker run -it ubuntu:latest
#-it=interactive pseudo terminal
```

then, in a different terminal
``` bash
# shows the running containers
docker ps
```

finally attach on more shell

```bash
docker exec --it <CONTAINER ID OR NAME> /bin/bash
```

---
# 🏗️ Building Images

Making it easy for others to use your code❗
## and 
shipping code 🚢

---
<!-- _backgroundColor: "#123" -->
<!-- _color: "#fff" -->

# <!--fit--> 🏗️ The Dockerfile


``` docker
FROM python:3.8-slim

RUN pip install emoji

WORKDIR /app

COPY hello-docker.py ./

RUN useradd -u 999 non-root-user
USER non-root-user

ENTRYPOINT ["python"]
CMD ["hello-docker.py"]
```
---
# Building and running the image

1. Clone this [presentation](https://github.com/knl88/presentations) and go to the [./docker](./docker) folder
2. Run `docker build . -t hello-docker:latest`

---
<!-- _backgroundColor: "#123" -->
<!-- _color: "#fff" -->

# Build tips

- Order of instructions matters
- Add the files needed .i.e not `COPY . .`
- Try to build small final images, [multi-stage build](https://docs.docker.com/develop/develop-images/multistage-build/) can be helpful

---
# Build args & secrets

These are used during build:) but be careful with what you pass in, args are stored in the image history

```bash
docker history hello-docker:latest
```

instead use buildx secrets if needed

---
# Finding images

In most cases you can find images on [dockerhub](https://hub.docker.com/search). 

For internal niva images you need to follow instructions on [google cloud artifactory setup](https://cloud.google.com/artifact-registry/docs/docker/pushing-and-pulling) and go to the [artifactory](https://console.cloud.google.com/artifacts/docker/niva-cd/europe-west1/images?project=niva-cd).

---
#  Running containers

- *default* `docker run hello-docker`
- *cmd* `docker run -it hello-docker:latest :yarn:`
-  *entrypoint*
```bash 
docker run -it --entrypoint /bin/python hello-docker:latest
```

---
<!-- _backgroundColor: "#123" -->
<!-- _color: "#fff" -->
# Configure the container

Config as **ENV** variables

1. Using --env or -e 
`docker run -e NIVA_ENV=1 hello-docker`
2. Using --env-file 
`docker run --env-file .env hello-docker`

---
# Configure the container
mount file
```bash
docker run  -e FAVOURITE_PATH=/app/favorite.emojis \
--mount type=bind,source="$(pwd)"/favorite.emojis,target=/app/favorite.emojis,readonly \
hello-docker
```

---
### docker compose 
`docker-compose` -> `docker compose`

docker-compose has been rewritten to a Golang plugin for docker 

---
<!-- _backgroundColor: "#123" -->
<!-- _color: "#fff" -->

# docker compose install 
* Already installed if using Docker Desktop
* For linux distro's see [compose install](https://docs.docker.com/compose/install/)
* For thumbleweed 😎
```bash
zypper in docker-compose
```
---
# <!--fit--> Commands 🏗️

* `docker compose build`
* `docker compose up`
* `docker compose down --volumes`

---
# The compose file


``` yaml
version: '3.5'
services:
  app:
    build: .
    entrypoint: ["shiny", "run", "--host", "0.0.0.0", "--port", "5000", "app.py"]
    environment:
      - SERVER=https://thredds.niva.no
      - DATASET=msource-inlet.nc
    ports:
      - "5000:5000"
```
---
# Python shiny ☀️ app

Still in the [./docker](./docker) folder run

`docker compose up`

and go to 

http://localhost:5000/

---
<!-- _backgroundColor: "#123" -->
<!-- _color: "#fff" -->
# Dockerbasen

compose [example](https://github.com/NIVANorge/nivabase/tree/docker)

---
### <!--fit--> :ok_hand:
