import streamlit as st
import pandas as pd
import requests

# Titolo della pagina
st.title("Compilatore di questionari")

# Aggiunta di un logo
logo_url = "logo\Deloitte_logo_black.png"
st.sidebar.image(logo_url, width=200)

# Testo introduttivo
st.write("Trascina e rilascia i file nelle aree sottostanti:")

# Drag-and-drop per il primo file
file1 = st.file_uploader("Carica il primo file qui", type=["jpg","xlsx", "png", "pdf"])

# Drag-and-drop per il secondo file
file2 = st.file_uploader("Carica il secondo file qui", type=["jpg","xlsx", "png", "pdf"])

# Mostra anteprima dei file caricati
if file1 is not None:
    st.write("Anteprima dei dati:")
    df = pd.read_excel(file1)
    st.dataframe(df)

if file2 is not None:
    st.write("Anteprima dei dati:")
    df = pd.read_excel(file2)
    st.dataframe(df)

# Aggiungi altre sezioni o elaborazioni a seconda delle tue esigenze
if st.button("Esegui Chiamata API"):
    if file1 is not None and file2 is not None:
        # Esegui la chiamata API qui usando la libreria requests
        # Sostituisci "URL_DELLA_TUA_API" con l'URL effettivo della tua API
        api_url = "URL_DELLA_TUA_API"
        # Esempio di chiamata POST, adatta il metodo e i parametri a seconda delle tue esigenze
        response = requests.post(api_url, files={'file': [file1,file2]})
        
        # Mostra il risultato della chiamata API
        st.write("Risultato della chiamata API:")
        st.json(response.json())