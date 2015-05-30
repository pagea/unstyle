#!/bin/sh
apt-get install python3 python3-pip
pip3 install python3-scipy nltk scikit-learn numpy
python3 -m nltk.downloader punkt cmudict
