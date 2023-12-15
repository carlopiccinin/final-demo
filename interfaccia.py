import streamlit as st
import pandas as pd
import requests
from anagrafica_2 import crea_questionario
import time
import random
# Titolo della pagina
st.title("Questionairo MiFID")
st.subheader("Tool di precompilazione")

# Aggiunta di un logo
logo_url = "Deloitte_logo_black.png"
st.sidebar.image(logo_url, width=200)

# Testo introduttivo
#st.write("Trascina e rilascia i file nelle aree sottostanti:")

# Drag-and-drop per il primo file
st.markdown("**Carica qui la carta di identità**")
file1 = st.file_uploader("file1", type=["jpg", "png", "pdf"],label_visibility="collapsed")

    
# Drag-and-drop per il secondo file
st.markdown("**Carica qui l'estratto conto**")
file2 = st.file_uploader("file2", type=["jpg","xlsx", "png", "pdf"],label_visibility="collapsed")


# st.markdown("**Carica qui la dichiarazione dei redditi**")
# file3 = st.file_uploader("file3", type=["xlsx", "pdf"],label_visibility="collapsed")
file3="dichiarazione_redditi.xlsx"
if file3 is not None and file1 is not None and file2 is not None:    
    st.write("I file sono stati caricati correttamente")
    
    st.write("Consenti ad Azimut di accedere ai dati di terze parti e ad importare lista conti, saldo e movimenti nell'area personale Azimut")
    
    risposta=st.checkbox("Acconsento") 
    risposta2=False#st.checkbox("Non acconsento")
else:
    risposta=False
    risposta2=False
    pdf_path="2000503 - QUESTIONARIO PF VincenzoVerdi.pdf"
   
if file1 is not None and file2 is not None:
    if file1.name.lower().find("vincenzo")>0:
        df=pd.read_excel("Anagrafica.xlsx")
        pdf_path="2000503 - QUESTIONARIO PF VincenzoVerdi.pdf"
        df_anagrafica=df.iloc[3]
        
    if file1.name.lower().find("mario")>0:
        df=pd.read_excel("Anagrafica.xlsx")
        pdf_path="2000503 - QUESTIONARIO PF MarioRossi.pdf"
        df_anagrafica=df.iloc[0]
        
    if file1.name.lower().find("giuseppina")>0:
        df=pd.read_excel("Anagrafica.xlsx")
        pdf_path="2000503 - QUESTIONARIO PF GiuseppinaCafueri.pdf"
        df_anagrafica=df.iloc[2]
        
    if file1.name.lower().find("filippo")>0:
        df=pd.read_excel("Anagrafica.xlsx")
        pdf_path="2000503 - QUESTIONARIO PF FilippoBianchi.pdf"
        df_anagrafica=df.iloc[1]
    df_anagrafica=pd.DataFrame(df_anagrafica).transpose()
    df_anagrafica.rename(index={1:0},inplace=True)
    df_anagrafica.rename(index={2:0},inplace=True)
    df_anagrafica.rename(index={3:0},inplace=True)
    
    nome=df_anagrafica["NOME"].values[0]
    cognome=df_anagrafica["COGNOME"].values[0]
    
    estratto_conto=pd.read_excel(file2)
    
    buffer=crea_questionario(df_anagrafica,estratto_conto)
    
if risposta==False:
    st.session_state.alpha=0 

    
    







# Mostra anteprima dei file caricati
# if file1 is not None:
#     st.write("Anteprima dei dati:")
    
#     st.image(file1)

# if file2 is not None:
#     st.write("Anteprima dei dati:")
#     df = pd.read_excel(file2)
#     st.dataframe(df)

# Aggiungi altre sezioni o elaborazioni a seconda delle tue esigenze
if "alpha" not in st.session_state:
    st.session_state.alpha = 0
if st.session_state.alpha == 0:
    button_container = st.empty()
    bottone=button_container.button("Compila Questionario")
else:
    bottone=False
if bottone and risposta==True and risposta2==False:
    button_container.empty()
    
    
        
   
    
    estratto_conto=pd.read_excel(file2)
    
    buffer=crea_questionario(df_anagrafica,estratto_conto)
    st.session_state.alpha=1
    scritte=["Caricamento dei file","Digitalizzazione della documentazione","Normalizzazione dei dati","Definizione delle risposte","Generazione del file Excel e PDF","Salvataggio del file"]
    
    for s in scritte:
        print(s)
        progress_container = st.empty()
        scritte_container = st.empty()
        spinner=scritte_container.write(s)
        progress_bar = progress_container.progress(value=0)
        numero_casuale = round(random.uniform(-0.002, 0.002),3)
        print(numero_casuale)
        # Simula l'operazione
        for percentuale_completamento in range(100):
            # Aggiorna la barra di avanzamento
            progress_bar.progress(percentuale_completamento + 1)

            # Aggiorna ogni secondo (sostituisci con la tua logica di elaborazione)
            time.sleep(0.005+numero_casuale)
        time.sleep(0.5)
        
        progress_container.empty()
        scritte_container.empty()
elif bottone and risposta==False and risposta2==False:
    if file1 is None and file2 is None and file3 is None:
        st.write("Non hai caricato nessun file")
    elif file1 is None or file2 is None or file3 is None:    
        if file1 is None:
            st.write("Non hai caricato la carta di identità")
        if file2 is None:
            st.write("Non hai caricato l'estratto conto")
        if file3 is None:
            st.write("Non hai caricato la dichiarazione dei redditi")
    
    else:
        button_container.empty()
        st.write("Non hai risposto alla domanda relativa al trattamento dei dati")
        st.write("Non è possibile compilare il questionario")
elif bottone and risposta==False and risposta2==True:
    button_container.empty()
    st.write("Non hai acconsentito al trattamento dei dati")
    st.write("Non è possibile compilare il questionario")
elif bottone and risposta==True and risposta2==True:
    button_container.empty()
    st.write("Non si possono selezionare entrambe le opzioni,riprova")

beta=0
    

if st.session_state.alpha == 1:
    # Creare due colonne
    col1, col2 = st.columns(2)
    with open(pdf_path, "rb") as f:
        pdf_bin = f.read()
        beta=1
    # Bottone 1 nella prima colonna
    with col1:
        bottone1=st.download_button(
            label="Scarica il file Excel",
            data=buffer,
            file_name="questionario_compilato"+nome+cognome+".xlsx",
            key="download_button"
        )

    # Bottone 2 nella seconda colonna
    with col2:
        bottone2=st.download_button(label="Scarica il file PDF",
                           data=pdf_bin,
                           file_name="questionario_compilato"+nome+cognome+".pdf",
                           mime="application/pdf",
                           key="download_button2"
                           
                           )
    
    

