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

# Dividir la pantalla en dos columnas
col1, col2 = st.columns(2)


image = Image.open('desempleo.JPEG')
image2 = Image.open('cambio.JPG')

with col1:
    st.title(':green[Idea principal del juego TONW TALES]')
    st.header(':blue[Tratar problematicas sociales:]')
    st.write("""TOWN TALES quiere concientizar sobre porblemtaicas 
             sociales tales como el desempleo y el cambio climatico, los 
             cuales se quieren abarcar de manera simple para no perder
             la naturaleza de un videojuego, pero siempre tratando de 
             dejar una reblexion sobre estas""")
    lottie_load = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_bqmgf5tx.json")
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

# Mostrar la descripción en la segunda columna
with col2:
    
    st.image(image, caption="""En la parte del desempleo aun no tenemos la idea bien planteada pero se espera que sea 
             un pueblo demasiado tecnologico el cual ya no necesita de 
             seres organicos para funcionar y todo ha sido remplazdo por maquinas""", width=300)
    st.divider()

    st.image(image2, caption="""En el cambio climatico tenemos una serie de mecanica la 
             cual trata de encontrar ciertos objetos para poder estabilizar el 
             poder del bosque y que todo pueda seguir""", width=300 )
    st.divider()
