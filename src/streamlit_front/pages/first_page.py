import streamlit as st


st.title(":orange[Step 1]: Browse your image")
st.write("Here you can browse an image from the product card on the marketplace")

uploaded_file = st.file_uploader("Upload an image")
display_im_button = st.button("Display image")

if uploaded_file is not None and display_im_button:
    st.image(uploaded_file)

col1, col2, col3 = st.columns(3)
with col1:
    button_hp = st.button('Homepage')

with col3:
    button2 = st.button('Step 2')

if button_hp:
    st.switch_page("start_page.py")
if button2:
    st.switch_page("pages/second_page.py")
