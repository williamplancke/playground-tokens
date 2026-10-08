class Tokenizer():
    def __init__(self, vocabulary = None):
        if vocabulary == None:
            self.vocabulary = []
            self.vocabulary.append("<PAD>")
            self.vocabulary.append("<UNK>")
        else:
            self.vocabulary = vocabulary
        self.punctuation = [".", "!", "?", ","]
        self.mode = "train"
    def toggle_mode(self, mode):
        mode = mode.lower()
        assert(mode == "train" or mode == "test")
        self.mode = mode
        return
    def obtain_token(self, input):
        if input not in self.vocabulary:
            if self.mode == "train":
                self.vocabulary.append(input)
            else:
                input = "<UNK>"
        return self.vocabulary.index(input)
    def obtain_word(self, input):
        if input > len(self.vocabulary) - 1:
            return "<UNK>"
        else:
            return self.vocabulary[input]
    def encode(self, input):
        assert(type(input) == str)
        lowercase = input.lower()
        space_padded = lowercase
        for char in self.punctuation:
            space_padded = space_padded.replace(char, " " + char)
        split_words = space_padded.split()
        output = []
        for word in split_words:
            output.append(self.obtain_token(word))
        return output
    def decode(self, token_ids):
        assert(type(token_ids) == list)
        tokens = token_ids
        for i, token in enumerate(tokens):
            tokens[i] = self.obtain_word(token)
        return tokens
    def prepare_input(self, input)
        return tokens:
    def construct_output(self, tokens):
        sentence_start = True
        output = ''
        for token in tokens:
            if sentence_start:
                token = token.capitalize()
                sentence_start = False
            if token in self.punctuation:
                sentence_start = True
                output = output.rstrip(' ')
            output += token
            output += ' '
        return output
def main():
    text = "Natural language processing is fun. Natural language models use tokens!"
    tok = Tokenizer()
    tokens = tok.encode(text)
    output_text = tok.decode(tokens)
    print(f"Token list: {len(tok.vocabulary)}")
    print(f"Vocabulary: {tok.vocabulary}")
    print(f"Encoded id's list: {tokens}")
    print(f"Decoded text: {output_text}")

if __name__ == '__main__':
    main()