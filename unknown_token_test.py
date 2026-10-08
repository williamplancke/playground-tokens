from basic_tokenizer import Tokenizer

train_text = "Natural language processing is fun."
test_text = "Natural language models are fun!"

tok = Tokenizer()
train_tok = tok.prepare_input(train_text)
train_tok_enc = tok.encode(train_tok)
tok.toggle_mode("test")
test_tok = tok.prepare_input(test_text)
test_tok_enc = tok.encode(test_tok)
test_dec = tok.decode(test_tok_enc)
test_out = tok.construct_output(test_dec)
print(f"Training tokens: {train_tok}")
print(f"Test tokens: {test_tok}")
print(f"Vocabulary: {tok.vocabulary}")
print(f"Encoded test IDs: {test_tok}")
print(f"Test encoded tokens: {test_tok_enc}")
print(f"Decoded tokens: {test_dec}")
print(f"Test output: {test_out}")