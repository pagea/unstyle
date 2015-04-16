#!/bin/sh
apt-get install python3 pip3
pip3 install nltk scikit-learn numpy
python3 -m nltk.download(punkt)
python3 -m nltk.download(pickle)
