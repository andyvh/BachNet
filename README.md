# BachNet
## Getting Started!
This is gonna be a bit of a doozy, please bear with me.

First, grab Anaconda (for Python 3.6) here: https://www.anaconda.com/download/#linux
Follow the instructions below the download links to install it!

Then, check https://www.tensorflow.org/install/ for instructions on how to get Tensorflow working:
this is the least approachable part, and depending on whether you want to use GPU acceleration,
you might have a whole new gamut of steps to run through.

In addition to Tensorflow, you're going to need tflearn, scipy, and h5py (all of which
can be installed using ```pip install ____```), as well as python3-midi, which you can find
here: https://github.com/louisabraham/python3-midi

In terms of training data, the repo comes with all the MIDIs we've found of Bach's
chorales. When you run ```python main.py``` , it should generate a network model
and go through a certain number of iterations (determined, for the moment, by the
iterations variable on line ~82 of network_model.py).
