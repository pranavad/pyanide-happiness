# pyanide-happiness

A simple Python script to download Cyanide and Happiness comics

#Introduction

Cyanide & Happiness is a webcomic written and illustrated by Rob DenBleyker, Kris Wilson, Dave McElfatrick and formerly Matt Melvin. It is published on their website explosm.net. This script makes the use of the Python requests and Beautiful Soup modules to download the comics.

# How to use it
1. Run the script
2. Select the comic you want to download
3. The comic will be downloaded to the directory the script is placed in

# Requirements

* [Python 3](python.org)
* Python requests module
* Python Beautiful Soup module

### How to install the required modules
1. Install Python.
2. Go to Command Line.
3. Run the following commands
<br>
```
$ py -m pip install bs4
```
and
```
$ py -m pip install requests
```
# Accepted Input

| Input         | Action                     | Example  |
| ------------- |:--------------------------:| --------:|
| number        | downloads a specific comic | ```number```|
| latest        | downloads the latest comic |  ```latest```    |
| random        | downloads a random comic   |  ```random```    |
