# ak-phrase.py

[![Build Status](https://api.travis-ci.com/arshadkazmi42/ak-phrase.js.svg?branch=master)](https://api.travis-ci.com/arshadkazmi42/ak-phrase.js)

This library generates all the permutations of sentences from words in a 2D array.

It follows the word orders in sentence, same as the words order in array column wise.

## Installation

```
$ pip3 install ak-phrase.py
```

## Usage

```python
import ak-phase.py
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
