import streamlit as st
from data.image_preprocessing import open_image
from models.u2net.u2net_model_utils import make_u2net_dataloader, generate_mask
from applications.apply_bg import apply_bg
from models.u2net.u2net_init import U2NetModel
from models.blip.blip_init import BLIPModel
from models.blip.blip_model_utils import generate_caption
from models.madlad400.madlad400_init import MADLAD400
from models.madlad400.translate import translate_to_eng

u2net_class = U2NetModel()
model_u2net = u2net_class.get_net()

blip_class = BLIPModel()
model_blip = blip_class.get_net()
processor_blip = blip_class.get_proc()

madlad400_class = MADLAD400()
model_madlad400 = madlad400_class.get_net()
tokenizer_madlad400 = madlad400_class.get_tokenizer()

uploaded_file = None
uploaded_bg_file = None

with st.container(border=True):
    st.title(":orange[Market image processor App]")
    st.write(
        "The project is a solution to an e-commerce problem: developing a system for processing photos from product "
        "cards on marketplaces, which performs the following actions:")
    st.markdown("- Removing the background")
    st.markdown("- Replacing the background")
    st.markdown("- Description generation")

with st.container(border=True):
    st.title(":orange[Step 1]: Browse your image")
    st.write("Here you can browse an image from the product card on the marketplace")

    uploaded_file = st.file_uploader("Upload an image")
    display_im_button = st.button("Display image")

    if uploaded_file is not None and display_im_button:
        save_path = f"data/{uploaded_file.name}"
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        user_input_image_dataloader = make_u2net_dataloader(uploaded_file)
        generate_mask(model_u2net, user_input_image_dataloader, uploaded_file)
        user_input_image = open_image(uploaded_file)
        st.image(user_input_image)

with st.container(border=True):
    st.title(":orange[Step 2]: Choose your background image")
    st.write("Here you can browse or choose an image for the background of card")

    mode = st.selectbox("Background mode",
                        ("Light background", "Dark background", "Custom background"))

    if mode is not None and mode == "Light background":
        display_light_bg_button = st.button("Preview light background")
        if display_light_bg_button:
            st.image("data/bg_themes/light_bg_theme.jpg")
        apply_background = st.button("Apply background!")
        if apply_background:
            apply_bg(f"data/{uploaded_file.name}", "data/bg_themes/light_bg_theme.jpg", 'models/predictions/u2net_masked_image.png')

    if mode is not None and mode == "Dark background":
        display_dark_bg_button = st.button("Preview dark background")
        if display_dark_bg_button:
            st.image("data/bg_themes/dark_bg_theme.JPG")
        apply_background = st.button("Apply background!")
        if apply_background:
            apply_bg(f"data/{uploaded_file.name}", "data/bg_themes/dark_bg_theme.JPG", 'models/predictions/u2net_masked_image.png')

    if mode is not None and mode == "Custom background":
        uploaded_bg_file = st.file_uploader("Upload background image")
        display_custom_bg_button = st.button("Preview custom background")
        if uploaded_bg_file is not None and display_custom_bg_button:
            save_path = f"data/{uploaded_bg_file.name}"
            with open(save_path, "wb") as f:
                f.write(uploaded_bg_file.getbuffer())

            bg_image = open_image(uploaded_bg_file)
            st.image(bg_image)
        apply_background = st.button("Apply background!")
        if apply_background and uploaded_bg_file is not None:
            apply_bg(f"data/{uploaded_file.name}", f"data/{uploaded_bg_file.name}", 'models/predictions/u2net_masked_image.png')

with st.container(border=True):
    st.title(":orange[Step 3]: Final page. Generate result")
    st.write("Here is a place, where you can generate your result.")

    generate_button = st.button("Generate result!")
    if generate_button:
        ind_caption = generate_caption(model_blip, processor_blip, open_image('models/predictions/img_with_applied_mask.png'))
        translated_text = translate_to_eng(model_madlad400, tokenizer_madlad400, ind_caption)

        with st.container(border=True):
            st.image('models/predictions/img_with_applied_mask.png', caption=translated_text)
