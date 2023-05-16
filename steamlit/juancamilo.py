import json
import requests
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie



def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


image = Image.open('ruby.png')
image2 = Image.open('tabla.png')

st.title(':red[TOWN TALES]')
st.header('Por Juan Camilo y Jahir')
lottie_load = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_3vbOcw.json")
st_lottie(
    lottie_load,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", # medium ; high
     # canvas
    height=300,
    width=300,
    key=None,
)
st.image(image, caption='ruby main character')

st.image(image2, caption = 'esquema general del proyecto')