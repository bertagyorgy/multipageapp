import streamlit as st

st.set_page_config(
    page_title="Multipage app",
    page_icon="👋",
)

st.title("Main page")
st.sidebar.success("Select a page above.")

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Írj ide egy szöveget", st.session_state["my_input"])
submit = st.button("Elküldés")
if submit:
    st.session_state["my_input"] = my_input
    st.write("Amit beírtál: ", my_input)
    