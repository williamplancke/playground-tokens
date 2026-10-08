from basic_tokenizer import Tokenizer

train_text = "Natural language processing is fun."
test_text = "Natural language models are fun!"

tok = Tokenizer()
train_tok = tok.encode(train_text)
tok.toggle_mode("test")
test_tok = tok.encode(test_text)
test_decoded = tok.decode(test_tok)

print(f"Training tokens: {train_tok}")
print(f"Test tokens: {test_tok}")
print(f"Vocabulary: {tok.vocabulary}")
print(f"Encoded test IDs: {test_tok}")
print(f"Decoded tokens: {test_decoded}")