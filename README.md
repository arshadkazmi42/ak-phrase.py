# ak-phrase.py

This library generates all the permutations of sentences from words in a 2D array.

It follows the word orders in sentence, same as the words order in array column wise.

## Usage

```python
from sentence_generator import SentenceGenerator

word_lists = [['eat'], ['code', 'commit'], ['sleep']];

sentences = SentenceGenerator.generate_sentences(word_lists);
print(sentences);

# Output:
# [ 'eat code sleep', 'eat commit sleep' ]
```

## Contributing

Interested in contributing to this project?
You can log any issues or suggestion related to this library [here](https://github.com/arshadkazmi42/ak-phrase.py/issues/new)

Read our contributing [guide](CONTRIBUTING.md) on getting started with contributing to the codebase