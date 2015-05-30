#!/bin/sh
apt-get -y install python3 python3-pip python3-numpy python3-scipy python3-pyqt5
pip3 install nltk scikit-learn numpy
python3 -m nltk.downloader punkt cmudict
