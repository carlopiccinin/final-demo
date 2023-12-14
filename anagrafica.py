import pandas as pd

conv_sc={
    "Nubile":1,
    "Celibe":1,
    "Sposato":3,
    "Convivente":3,
    "Separato":4,
    "Divorziato":5,
    "Vedovo":6,
    "Vedova":6,
    "Sposata":3,
    "Separata":4,
    "Divorziata":5,
    "Coppia di fatto":2,
    "Coniugata":3,
    "Coniugato":3,
}


df=pd.read_excel("Anagrafica.xlsx")

x,y=df.shape
vett_anagrafica=[]  
anagrafica = pd.read_excel("2000503 - QUESTIONARIO PF clean.xlsx")


for i in range(x):
    vett_anagrafica.append(anagrafica.copy())
    vett_anagrafica[i]["Risposta 1"][1]=df["COGNOME"][i]
    vett_anagrafica[i]["Risposta 1"][2]=df["NOME"][i]
    nome=df["NOME"][i]
    cognome=df["COGNOME"][i]
    vett_anagrafica[i]["Risposta 1"][3]=str(df["DATA DI NASCITA"][i])[0:10]
    vett_anagrafica[i]["Risposta "+str(conv_sc[df["STATO CIVILE"][i]])][5]="X-"+vett_anagrafica[i]["Risposta "+str(conv_sc[df["STATO CIVILE"][i]])][5]
    if df["N. FAMILIARI A CARICO"][i]==0:
        n_ris="1"
    elif df["N. FAMILIARI A CARICO"][i]==1:
        n_ris="2"
    elif df["N. FAMILIARI A CARICO"][i]==2:
        n_ris="2"
    elif df["N. FAMILIARI A CARICO"][i]==3:
        n_ris="3"
    elif df["N. FAMILIARI A CARICO"][i]==4:
        n_ris="3"
    else:
        n_ris="4"
        
    if df["COMPONENTI NUCLEO FAMILIARE"][i]==0 or df["COMPONENTI NUCLEO FAMILIARE"][i]==1:
        vett_anagrafica[i]["Risposta 1"][6]="X-"+vett_anagrafica[i]["Risposta 1"][6]
    elif df["COMPONENTI NUCLEO FAMILIARE"][i]==2:
        vett_anagrafica[i]["Risposta 2"][6]="X-"+str(vett_anagrafica[i]["Risposta 2"][6])
    elif df["COMPONENTI NUCLEO FAMILIARE"][i]==3:
        vett_anagrafica[i]["Risposta 3"][6]="X-"+str(vett_anagrafica[i]["Risposta 3"][6])
    elif df["COMPONENTI NUCLEO FAMILIARE"][i]==4:
        vett_anagrafica[i]["Risposta 4"][6]="X-"+vett_anagrafica[i]["Risposta 4"][6]
    else:
        vett_anagrafica[i]["Risposta 5"][6]="X-"+vett_anagrafica[i]["Risposta 5"][6]
    
    vett_anagrafica[i]["Risposta "+n_ris][41]="X-"+vett_anagrafica[i]["Risposta "+n_ris][41]
    
    
    estratto_conto=pd.read_excel("EstrattoConto "+nome+cognome+".xlsx")
    estratto_conto.columns=estratto_conto.iloc[4]
    estratto_conto=estratto_conto[5:]
    descrizione=estratto_conto["Descrizione"]
    for j in range(len(descrizione)):
        if descrizione.iloc[j].find("EMOLUMENTI")>0:
            a=j
            break
        if descrizione.iloc[j].find("Stipendio")>0:
            a=j
            break
    
    stipendio=estratto_conto["Entrate"].to_list()[a]
    if stipendio<1500:
        n_ris="1"
    elif stipendio<3500:
        n_ris="2"
    elif stipendio<6500:
        n_ris="3"
    else:
        n_ris="4"
    vett_anagrafica[i]["Risposta "+n_ris][33]="X-"+vett_anagrafica[i]["Risposta "+n_ris][33]
    a=0
    aa=0
    for j in range(len(descrizione)):
        if descrizione.iloc[j].find("Fee di consulenza")>0:
            a=j
            break
        if descrizione.iloc[j].find("Commissioni su fondi comuni")>0:
            aa=j
            break
    
    stipendio=estratto_conto["Entrate"].to_list()[a]
    if a!=0:
        n_ris="1"
    else:
        n_ris="2"
    vett_anagrafica[i]["Risposta "+n_ris][8]="X-"+vett_anagrafica[i]["Risposta "+n_ris][8]
    if aa!=0:
        n_ris="1"
    else:
        n_ris="2"
    vett_anagrafica[i]["Risposta "+n_ris][9]="X-"+vett_anagrafica[i]["Risposta "+n_ris][9]
    
    ####risposta 1.3
    ##Da non popolare
    ####risposta 1.4
    ##Clustering su personam sulla base dell età e del lavoro proveniente dal conto corrente e del numero di familiari a carico
    ####risposta 1.5
    #da verificare
    ####risposta 1.6
    #da definire regola sulla base di età, movimenti conto, lavoro ed educazione
    ####risposta 1.7
    ##da definire tramite conto corrente
    ####risposta 1.8
    ##da definire tramite conto corrente
    ####risposta 1.9
    ##da definire tramite conto corrente, da fare mining su conto corrente in base a quali sono e quanto frequenti sono le entrate
    ####risposta 2.1
    ##da definire in base al lavoro e al conto corrente
    
    ######Risposta 2.4
    ###mining sul conto corrente
    # stipendio_netto_attuale=int(stipendio)*13
    # investimento=stipendio_netto_attuale//10
    # età=df["DATA DI NASCITA"][i]
    # print(type(età))

    ######Risposta 2.5
    ###mining sul conto corrente in base a che tasse paga
    ######Risposta 2.6
    ###mining sul conto corrente in base a quante tasse paga
    
    
    vett_anagrafica[i].to_excel("2000503 - QUESTIONARIO PF "+nome+cognome+".xlsx")