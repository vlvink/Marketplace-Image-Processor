from PIL import Image


def open_image(path: str) -> Image:
    """ Opens the input image in PIL format
    :param path: Path to image
    :return image: PIL formatted image
    """
    image = Image.open(path)
    return image


def resize_image(image: Image) -> Image:
    """ Resizing image to 640x640 proportionally to the input image size
    :param image: Image, opened with PIL
    :return image: Resized image
    """
    new_width = 720
    new_height = 720

    new_height = new_width * image.size[1] // image.size[0]
    new_width = new_height * image.size[1] // image.size[0]

    image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    return image

