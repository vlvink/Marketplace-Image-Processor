from .blip_init import BLIPModel
from PIL import Image
import torch


def generate_caption(model,
                     processor,
                     image: Image) -> str:
    """ Generates text caption for input image
    :param image: Created by user image with background
    :param model: Model for image captioning
    :param processor: Model's processor for image captioning
    :return generated_caption: Text caption for image
    """
    model.eval()

    inputs = processor(images=image, return_tensors="pt")
    pixel_values = inputs.pixel_values

    generated_ids = model.generate(pixel_values=pixel_values, max_length=200)
    generated_caption = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

    return generated_caption


