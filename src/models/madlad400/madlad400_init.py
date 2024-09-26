from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


class MADLAD400:
    def __init__(self):
        self.model = AutoModelForSeq2SeqLM.from_pretrained("google/madlad400-3b-mt")
        self.tokenizer = AutoTokenizer.from_pretrained("google/madlad400-3b-mt")

    def get_net(self):
        return self.model

    def get_tokenizer(self):
        return self.tokenizer
