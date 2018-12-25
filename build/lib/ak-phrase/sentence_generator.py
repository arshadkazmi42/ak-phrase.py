class SentenceGenerator(object):

    # Function `generate_sentences` accepts list of lists containing words 
    # Sample input: [ ['eat'], ['code', 'commit'], ['sleep'] ]
    # Returns list of all the possible sentences which can be formed using the words
    # Sample output: [ 'eat code sleep', 'eat commit sleep' ]
    @staticmethod
    def generate_sentences(words_list):
        if not words_list:
            return []

        if len(words_list) == 0:
            return []

        sentences = [""] * len(words_list)
        generated_sentences = []

        for word_index in range(len(words_list[0])):
            SentenceGenerator.sentence_permutations(words_list, 0, word_index, sentences, generated_sentences)

        return generated_sentences

    @staticmethod
    def sentence_permutations(words_list, start_index, word_index, sentences, generated_sentences):

        sentences[start_index] = words_list[start_index][word_index]

        if start_index == len(words_list) - 1:
            generated_sentences.append(' '.join(sentences))
            return
        
        for i in range(len(words_list[start_index + 1])):
            SentenceGenerator.sentence_permutations(words_list, start_index + 1, i, sentences, generated_sentences)

