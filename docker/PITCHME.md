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
# Installation
**Follow 🐋 for** 
[![For Linux h:1.5em](https://upload.wikimedia.org/wikipedia/commons/3/35/Tux.svg)](https://docs.docker.com/engine/install/), [![Windows h:1.5em](https://upload.wikimedia.org/wikipedia/commons/6/6d/Windows_Logo_%281992-2001%29.svg)](https://docs.p.niva.no/guides/devenv.html), [![Apple h:1.5em](https://upload.wikimedia.org/wikipedia/commons/f/fa/Apple_logo_black.svg)](https://github.com/abiosoft/colima/#installation)

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
# <!--fit--> 🏗️ The Dockerfile

``` docker
FROM ubuntu:18.04
ADD ssh /root/.ssh
```
---
### <!--fit--> :ok_hand:

---