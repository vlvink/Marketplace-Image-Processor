import streamlit as st

st.title("Market image processor App")
st.write("The project is a solution to an e-commerce problem: developing a system for processing photos from product "
         "cards on marketplaces, which performs the following actions:")
st.markdown("- Removing the background")
st.markdown("- Replacing the background")
st.markdown("- Description generation")

button1 = st.button('Step 1')

if button1:
    st.switch_page("pages/first_page.py")
