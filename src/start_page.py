import streamlit as st
from data.image_preprocessing import open_image
from models.u2net.u2net_model_utils import make_u2net_dataloader

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
        user_input_image_dataloader = make_u2net_dataloader(uploaded_file)
        user_input_image = open_image(uploaded_file)
        st.image(user_input_image)

with st.container(border=True):
    st.title(":orange[Step 2]: Choose your background image")
    st.write("Here you can browse or choose an image for the background of card")

    mode = st.selectbox("Background mode",
                        ("Light background", "Room background", "Custom background"))

    if mode is not None and mode == "Light background":
        display_light_bg_button = st.button("Preview light background")
        if display_light_bg_button:
            st.image("data/bg_themes/light_bg_theme.jpg")
        apply_bg = st.button("Apply background!")
        if apply_bg:
            pass

    if mode is not None and mode == "Room background":
        display_room_bg_button = st.button("Preview room background")
        if display_room_bg_button:
            st.image("data/bg_themes/room_bg_theme.jpg")

    if mode is not None and mode == "Custom background":
        uploaded_bg_file = st.file_uploader("Upload background image")
        display_custom_bg_button = st.button("Preview custom background")
        if display_custom_bg_button:
            st.image(uploaded_bg_file)

with st.container(border=True):
    st.title(":orange[Step 3]: Final page. Generate result")
    st.write("Here is a place, where you can generate your result.")

    generate_button = st.button("Generate result!")
