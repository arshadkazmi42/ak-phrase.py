# ak-phrase.py

[![Build Status](https://api.travis-ci.com/arshadkazmi42/ak-phrase.py.svg?branch=master)](https://api.travis-ci.com/arshadkazmi42/ak-phrase.py)
[![Repo Size](https://img.shields.io/github/languages/code-size/arshadkazmi42/ak-phrase.py.svg)](https://github.com/arshadkazmi42/ak-phrase.py)
[![Downloads](https://img.shields.io/pypi/dm/ak-phrase.py.svg)](https://pypi.org/project/ak-phrase.py/)
[![LICENSE](https://img.shields.io/pypi/l/ak-phrase.py.svg)](https://pypi.org/project/ak-phrase.py/)
[![Version](https://img.shields.io/pypi/v/ak-phrase.py.svg)](https://pypi.org/project/ak-phrase.py/)
[![Last Commit](https://img.shields.io/github/last-commit/arshadkazmi42/ak-phrase.py.svg)](https://github.com/arshadkazmi42/ak-phrase.py)

This library generates all the permutations of sentences from words in a 2D array.

It follows the word orders in sentence, same as the words order in array column wise.

## Installation

```
$ pip3 install ak-phrase.py
```

## Usage

```python
from ak-phase.py import SentenceGenerator

word_lists = [['eat'], ['code', 'commit'], ['sleep']]

sentences = SentenceGenerator.generate_sentences(word_lists)
print(sentences)

# Output:
# [ 'eat code sleep', 'eat commit sleep' ]
```

## Contributing

Interested in contributing to this project?
You can log any issues or suggestion related to this library [here](https://github.com/arshadkazmi42/ak-phrase.py/issues/new)

Read our contributing [guide](https://github.com/arshadkazmi42/ak-phrase.py/blob/master/CONTRIBUTING.md) on getting started with contributing to the codebase

## Contributors

Thank you to all the contributors who have helped us in making this project better :raised_hands:

<a href="https://github.com/arshadkazmi42"><img src="https://github.com/arshadkazmi42.png" width="30" /></a><a href="https://github.com/meshack-mbuvi"><img src="https://github.com/meshack-mbuvi.png" width="30" /></a><a href="https://github.com/Saloni-prsd"><img src="https://github.com/Saloni-prsd.png" width="30" /></a><a href="https://github.com/quar17esma"><img src="https://github.com/quar17esma.png" width="30" /></a
