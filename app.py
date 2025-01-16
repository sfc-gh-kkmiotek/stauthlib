import streamlit as st

st.set_page_config(page_title="Auth demo", page_icon=":material/person_add:")

st.title("Auth demo!")


left, middle1, middle2, right, logout_button_column = st.columns([1, 1, 1, 1.1, 1])


with left:
    google_button = st.button("Google Login")

    if google_button:
        st.login(provider="google")


st.write(":sparkles: :rainbow[User data]")
st.write(st.experimental_user)


with logout_button_column:
    logout_button = st.button("Logout")
    if logout_button:
        st.logout()


st.header("Streamlit app code:")
st.code(
    body="""
    google_button = st.button("Google Login")
    if google_button:
        st.login(provider="google")
    
    logout_button = st.button("Logout")
    if logout_button:
        st.logout()

    st.write(st.experimental_user)
    """,
    language="python",
)

st.header("Secrets.toml file example:")
with open("./.streamlit/secrets.toml.example", "r") as f:
    st.code(f.read(), language="toml")
