import streamlit as st


st.title(":orange[Step 2]: Choose your background image")
st.write("Here you can browse or choose an image for the background of card")

mode = st.selectbox("Background mode",
                    ("Light background", "Room background", "Custom background"))

if mode is not None and mode == "Light background":
    display_light_bg_button = st.button("Preview light background")
    if display_light_bg_button:
        st.image("data/bg_themes/light_bg_theme.jpg")

if mode is not None and mode == "Room background":
    display_room_bg_button = st.button("Preview room background")
    if display_room_bg_button:
        st.image("data/bg_themes/room_bg_theme.jpg")

if mode is not None and mode == "Custom background":
    uploaded_bg_file = st.file_uploader("Upload background image")
    display_custom_bg_button = st.button("Preview custom background")
    if display_custom_bg_button:
        st.image(uploaded_bg_file)

col1, col2, col3 = st.columns(3)
with col1:
    button1 = st.button('Step 1')

with col3:
    button3 = st.button('Step 3')

if button1:
    st.switch_page("pages/first_page.py")
if button3:
    st.switch_page("pages/third_page.py")