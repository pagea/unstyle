## WARNING:
Unstyle is in a very early state of development. It would be unwise to rely on
it for anonymizing you against a smart adversary.

Unstyle only protects you against authorship attacks from the "Basic 9" feature
set, a simple method of authorship attribution used primarily for research
purposes. Your identity CAN be unmasked by the Writeprints feature set, which is
considerably more sophisticated. Though we will support the Writeprints feature
set in the future, it is not ready at this moment.

## About Unstyle
Unstyle is an application intended to help users publish anonymous writings.

For information on how Unstyle works, see [doc/thesis.pdf](https://github.com/pagea/unstyle/blob/master/doc/thesis.pdf).

## Running Unstyle

### Debian, Ubuntu, and other .deb based distros:
If you are using a Debian-based Linux distribution, you can install Unstyle by
performing the following steps:

1. Clone the repository.
2. `cd stylproj`
3. Install dependencies by running `./install-dependencies.sh`.
4. Run `python3 main.py`

Note that `install-dependencies.sh` has only undergone limited testing. Please
open up an issue if Step 4 fails.

### OSX and Windows
Unstyle has not been tested on either of these operating systems. Theoretically,
if you install all required dependencies yourself, it will work, but this has not been
confirmed. If you have an OSX or Windows machine available and would like to
help us port Unstyle, please request this feature in the issue tracker.

## Contributing

Pull requests are both welcome and encouraged.

Not sure where to start? We are in the process of migrating our bugtracker from
Bitbucket. In the meantime, try this in the root directory:

`grep -nr "TODO\|FIXME\|XXX" .`
