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

[![](https://sourcerer.io/fame/arshadkazmi42/arshadkazmi42/ak-phrase.py/images/0)](https://sourcerer.io/fame/arshadkazmi42/arshadkazmi42/ak-phrase.py/links/0)[![](https://sourcerer.io/fame/arshadkazmi42/arshadkazmi42/ak-phrase.py/images/1)](https://sourcerer.io/fame/arshadkazmi42/arshadkazmi42/ak-phrase.py/links/1)[![](https://sourcerer.io/fame/arshadkazmi42/arshadkazmi42/ak-phrase.py/images/2)](https://sourcerer.io/fame/arshadkazmi42/arshadkazmi42/ak-phrase.py/links/2)[![](https://sourcerer.io/fame/arshadkazmi42/arshadkazmi42/ak-phrase.py/images/3)](https://sourcerer.io/fame/arshadkazmi42/arshadkazmi42/ak-phrase.py/links/3)[![](https://sourcerer.io/fame/arshadkazmi42/arshadkazmi42/ak-phrase.py/images/4)](https://sourcerer.io/fame/arshadkazmi42/arshadkazmi42/ak-phrase.py/links/4)[![](https://sourcerer.io/fame/arshadkazmi42/arshadkazmi42/ak-phrase.py/images/5)](https://sourcerer.io/fame/arshadkazmi42/arshadkazmi42/ak-phrase.py/links/5)[![](https://sourcerer.io/fame/arshadkazmi42/arshadkazmi42/ak-phrase.py/images/6)](https://sourcerer.io/fame/arshadkazmi42/arshadkazmi42/ak-phrase.py/links/6)[![](https://sourcerer.io/fame/arshadkazmi42/arshadkazmi42/ak-phrase.py/images/7)](https://sourcerer.io/fame/arshadkazmi42/arshadkazmi42/ak-phrase.py/links/7)