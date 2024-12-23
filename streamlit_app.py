import streamlit as st

st.title("🎈 My nueva app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

cantidad = st.slider('Selecciona la cantidad')
st.write(f'La Cantidad Seleccionada es: {cantidad}')