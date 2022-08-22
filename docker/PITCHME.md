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

![bg](#123)
![](#fff)
##### <!--fit--> 👉 Making your life easier:)
---
###  The name docker is used about:

1. Docker containerization technology
    - a container makes in possible to package and isolate applications with their entire runtime environment
2. The docker open source community 
3. The company docker
Also see [Redhat's post](https://www.redhat.com/en/topics/containers/what-is-docker)
---

---
# Installation
**Follow 🐋 for** 
[![For Linux h:1.5em](https://upload.wikimedia.org/wikipedia/commons/3/35/Tux.svg)](https://docs.docker.com/engine/install/ubuntu/), [![Windows h:1.5em](https://upload.wikimedia.org/wikipedia/commons/6/6d/Windows_Logo_%281992-2001%29.svg)](https://docs.p.niva.no/guides/devenv.html), [![Apple h:1.5em](https://upload.wikimedia.org/wikipedia/commons/f/fa/Apple_logo_black.svg)](https://github.com/abiosoft/colima/#installation)
**Or**
[![Docker desktop h:2em](https://i2.wp.com/ralphmcneal.com/wp-content/uploads/2018/11/docker-desk-banner1.png?fit=770%2C403&ssl=1)](https://www.docker.com/products/docker-desktop/)
**Or install** 
[![podman h:2em](https://podman.io/images/podman.svg)](https://podman.io/) 
**for your distro**

---
![bg](#123)
![](#fff)
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
![bg](#123)
![](#fff)

#  <!--fit--> Using containers 🐛

``` bash
docker run -it ubuntu:latest
#-it=interactive pseudo terminal
```

then, in a different terminal
``` bash
# shows the running container
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
![bg](#123)
![](#fff)

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
3. Run `docker run hello-docker`
4. Inspect the container 
```bash 
docker run -it --entrypoint /bin/bash hello-docker:latest
```
---
![bg](#123)
![](#fff)

# Build tips

- Order of instructions matters
- Add the files needed .i.e not `COPY . .`
- Try to build small final images, [multi-stage build](https://docs.docker.com/develop/develop-images/multistage-build/) can be helpful
- Change user to non root user
---
# Finding images

In most cases you can find images on [dockerhub](https://hub.docker.com/search). 

For internal niva images you need to follow instructions on [google cloud artifactory setup](https://cloud.google.com/artifact-registry/docs/docker/pushing-and-pulling) and go to the [artifactory](https://console.cloud.google.com/artifacts/docker/niva-cd/europe-west1/images?project=niva-cd).

---
![bg](#123)
![](#fff)

# Running an oracle Express db

```bash
docker run --name oracle-test \
            -p 1521:1521 \
            -e ORACLE_PASSWORD=oracle \
            -e ORACLE_DATABASE=NIVABPRD \
            -e APP_USER=niva \
            -e APP_USER_PASSWORD=niva \
gvenzl/oracle-xe:21
```
---
### <!--fit--> :ok_hand:
