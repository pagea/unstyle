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

## Running Unstyle
1. Clone the repository.
3. Install dependencies listed in `DEPENDENCIES`. In the near future, this will
   be done by a setup script.
2. Run `python3 main.py`

## Contributing

Pull requests are both welcome and encouraged.

Not sure where to start? We are in the process of migrating our bugtracker from
Bitbucket. In the meantime, try this in the root directory:

`grep -nr "TODO\|FIXME\|XXX" .`
