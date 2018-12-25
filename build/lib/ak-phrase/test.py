import unittest
from sentence_generator import SentenceGenerator


class TestSum(unittest.TestCase):

    def test_generated_sentence(self):
        words_list = [['eat'], ['code', 'commit'], ['sleep']]
        sentences = SentenceGenerator.generate_sentences(words_list)
        self.assertEqual(sentences, ['eat code sleep', 'eat commit sleep'], "Should return all generated sentences")

    def test_empty_words_list(self):
        words_list = []
        sentences = SentenceGenerator.generate_sentences(words_list)
        self.assertEqual(sentences, [], "Should return all generated sentences")


if __name__ == '__main__':
    unittest.main()

