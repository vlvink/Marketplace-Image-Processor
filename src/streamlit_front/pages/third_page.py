import streamlit as st


st.title(":orange[Step 3]: Final page. Generate result")
st.write("Here is a place, where you can generate your result.")

generate_button = st.button("Generate result!")

button3 = st.button('Step 2')

if button3:
    st.switch_page("pages/second_page.py")