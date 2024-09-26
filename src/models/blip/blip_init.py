from transformers import AutoProcessor, BlipForConditionalGeneration


class BLIPModel:
    def __init__(self):
        self.processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        self.model = BlipForConditionalGeneration.from_pretrained("models/params/blip")

    def get_net(self):
        return self.model

    def get_proc(self):
        return self.processor
