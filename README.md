# Hsincheng Chao Online Prorfolio

Simple GAE site, try whatever web tech I want here!

## Things Learned
#### 1. Setup Flask with GAE from scratch
* Start virtual environment `virtualenv venv`
* Install flask `pip install --target=./lib`
* Add .pyc ./venv ./lib to .gitignore file
* Write app.yaml and main.py
* Add ./lib to python path on appengine_config.py

#### Bower
* [Bower][1] is a FE framework package management tool
* Install bower `(sudo) npm install -g bower`
* Init bower.json: `bower init`
* Install bower package: `bower install --save jquery`

#### Materialize
* `bower install --save materialize`

# Packages

Some packages are installed through pip under venv/python2.7/sitepackages
see `requirements.txt` for more info


[1]: http://bower.io/
