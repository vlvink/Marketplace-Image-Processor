import cv2
import numpy as np


def apply_bg(user_image_path: str,
             bg_image_path: str,
             image_mask_path: str = 'models/predictions/u2net_masked_image.png'
             ) -> None:
    """ Applying background image to user's input image
    :param user_image_path: Path to user input image
    :param image_mask_path: Path to mask of user's input image
    :param bg_image_path: Path to background image
    :return im_with_bg:
    """
    img = cv2.imread(user_image_path)
    mask = cv2.imread(image_mask_path, 0)
    new_background = cv2.imread(bg_image_path)

    _, binary_mask = cv2.threshold(mask, 128, 255, cv2.THRESH_BINARY)  # Increase the contrast of the mask
    kernel = np.ones((3, 3), np.uint8)  # Increase the mask to improve the edges
    binary_mask = cv2.dilate(binary_mask, kernel,
                             iterations=1)
    mask_inv = cv2.bitwise_not(binary_mask)  # Invert the mask to remove the background from the object
    img_fg = cv2.bitwise_and(img, img, mask=binary_mask)  # Removing the background from the original image
    background_bg = cv2.bitwise_and(new_background, new_background,
                                    mask=mask_inv)  # Removing the object from the new background
    final_img = cv2.add(img_fg, background_bg)  # Connecting the image of the object and the new background
    cv2.imwrite('models/predictions/img_with_applied_mask.png', final_img)
