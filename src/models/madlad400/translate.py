def translate_to_eng(model,
                     tokenizer,
                     text: str):
    """ Translates the input sentence from Indonesian to English
    :param model: Model for translation
    :param tokenizer: Model's tokenizer
    :param text: The text to be translated
    """
    inputs = tokenizer("<2ru> {}".format(text), return_tensors="pt")
    outputs = model.generate(**inputs)
    translated_text = tokenizer.batch_decode(outputs, skip_special_tokens=True)
    return translated_text

