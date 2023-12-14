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
    
    a=0
    aa=0
    for j in range(len(descrizione)):
        if (descrizione.iloc[j].find("Commissioni gestione patrimoniale")>0) or (descrizione.iloc[j].find("Consulenza bancaria")>0):
            a=j
            break
        if (descrizione.iloc[j].find("Commissioni fondi")>0) or (descrizione.iloc[j].find("Fidi consulenza")>0):
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
    

    ####risposta 1.4
    # Al ﬁne di diversiﬁcare il rischio degli investimenti, quale delle seguenti soluzioni ritiene più efﬁcace?
    ##Clustering su personam sulla base dell età e del lavoro proveniente dal conto corrente e del numero di familiari a carico


    
    
    ####risposta 1.5
    #Più si allunga l’orizzonte temporale dell’investimento, più risultano mitigati i rischi di perdita che caratterizzano, invece, 
    #il medesimo investimento valutato su un orizzonte temporale più breve. Concorda con questa affermazione?
    ##da definire sulla base di età, movimenti conto, lavoro ed educazione

    #tutte da definire sulla base di età, movimenti conto, lavoro ed educazione
    ##Tutte Vero/Falso
    ####risposta 1.6.1
    # Il rendimento di attività a basso rischio potrebbe signiﬁcare la perdita del potere di acquisto derivante dal mancato recupero dell’inﬂazione
   
    
    ####risposta 1.6.2
    #Strumenti Obbligazionari: Nel confronto tra un titolo obbligazionario di un Emittente a basso rischio ed un titolo obbligazionario 
    #caratterizzato da un rating peggiore, quest’ultimo dovrebbe offrire un rendimento atteso più basso perché il rischio di insolvenza è maggiore
   
    
    ####risposta 1.6.3
    #Strumenti Obbligazionari: L’acquisto di un titolo obbligazionario emesso in una valuta diversa dall’Euro comporta l’esposizione anche al rischio di cambio
  
   
    ####risposta 1.6.4
    #Strumenti Azionari: Le azioni, a causa dei cambiamenti delle condizioni generali di mercato (rischio sistemico) e/o 
    #della diffusione di informazioni relative alle singole società emittenti (rischio speciﬁco) possono subire una variazione anche signiﬁcativa e repentina dei prezzi
    
    
    ####risposta 1.6.5
    #OICVM (Fondi Armonizzati): L’investimento in OICVM consente, anche a chi dispone di importi limitati, di beneﬁciare di una diversiﬁcazione di portafoglio e di una gestione professionale
    
    
    ####risposta 1.6.6
    #OICVM (Fondi Armonizzati): Il rischio di un OICVM può differire sensibilmente in funzione della strategia di investimento 
    #adottata dal gestore (a scadenza breve o medio-lunga, denominati in Euro o in altre valute, etc.)
    
    
    ####risposta 1.6.7
    #Prodotti di Investimento Assicurativi: La polizza unit-linked si deﬁnisce tale perché il suo valore è strettamente collegato al valore delle quote dei fondi in cui investe
    
    
    ####risposta 1.6.8
    #Prodotti Alternativi di Investimento: I Fondi di Private Equity investono nel capitale di rischio di aziende normalmente non quotate per 
    # realizzare un rendimento nel medio-lungo termine tramite lo smobilizzo futuro di tali partecipazioni
    
    
    ####risposta 1.6.9
    #Prodotti Alternativi di Investimento: I Fondi di Investimento Alternativo chiusi non sono caratterizzati da limitazioni al disinvestimento durante la loro vita anagraﬁca





    ####risposta 1.7.1 Ha effettuato negli ultimi 5 anni investimenti nei seguenti prodotti/servizi Strumenti Mercato Monetario
    b=0
    for j in range(len(descrizione)):
        if descrizione.iloc[j].find("Strumenti mercato monetario")>0:
            b=j
            break
    
    stipendio=estratto_conto["Entrate"].to_list()[b]
    if b!=0:
        n_ris="1"
    else:
        n_ris="2"
    vett_anagrafica[i]["Risposta "+n_ris][24]="X-"+vett_anagrafica[i]["Risposta "+n_ris][24]


    ####risposta 1.7.2 Ha effettuato negli ultimi 5 anni investimenti nei seguenti prodotti/servizi Strumenti Obbligazionari
    c=0
    for j in range(len(descrizione)):
        if descrizione.iloc[j].find("Obbligazioni")>0:
            c=j
            break
    
    stipendio=estratto_conto["Entrate"].to_list()[c]
    if c!=0:
        n_ris="1"
    else:
        n_ris="2"
    vett_anagrafica[i]["Risposta "+n_ris][25]="X-"+vett_anagrafica[i]["Risposta "+n_ris][25]

    ####risposta 1.7.3 Ha effettuato negli ultimi 5 anni investimenti nei seguenti prodotti/servizi Strumenti Azionari
    d=0
    for j in range(len(descrizione)):
        if descrizione.iloc[j].find("Azioni")>0:
            d=j
            break
    
    stipendio=estratto_conto["Entrate"].to_list()[d]
    if d!=0:
        n_ris="1"
    else:
        n_ris="2"
    vett_anagrafica[i]["Risposta "+n_ris][26]="X-"+vett_anagrafica[i]["Risposta "+n_ris][26]

    ####risposta 1.7.4 Ha effettuato negli ultimi 5 anni investimenti nei seguenti prodotti/servizi OICVM (Fondi Armonizzati)
    e=0
    for j in range(len(descrizione)):
        if descrizione.iloc[j].find("Fondi armonizzati")>0:
            e=j
            break
    
    stipendio=estratto_conto["Entrate"].to_list()[e]
    if e!=0:
        n_ris="1"
    else:
        n_ris="2"
    vett_anagrafica[i]["Risposta "+n_ris][27]="X-"+vett_anagrafica[i]["Risposta "+n_ris][27]

    ####risposta 1.7.5 Ha effettuato negli ultimi 5 anni investimenti nei seguenti prodotti/servizi Prodotti di Investimento Assicurativi
    f=0
    for j in range(len(descrizione)):
        if descrizione.iloc[j].find("Prodotti di Investimento Assicurativi")>0:
            f=j
            break
    
    stipendio=estratto_conto["Entrate"].to_list()[f]
    if f!=0:
        n_ris="1"
    else:
        n_ris="2"
    vett_anagrafica[i]["Risposta "+n_ris][28]="X-"+vett_anagrafica[i]["Risposta "+n_ris][28]    

    ####risposta 1.7.5 Ha effettuato negli ultimi 5 anni investimenti nei seguenti prodotti/servizi Prodotti Alternativi di Investimento
    g=0
    for j in range(len(descrizione)):
        if descrizione.iloc[j].find("Prodotti Alternativi di Investimento")>0:
            g=j
            break
    
    stipendio=estratto_conto["Entrate"].to_list()[g]
    if  g!=0:
        n_ris="1"
    else:
        n_ris="2"
    vett_anagrafica[i]["Risposta "+n_ris][29]="X-"+vett_anagrafica[i]["Risposta "+n_ris][29]  

    
    ####risposta 1.8 Con quale frequenza ha effettuato operazioni negli strumenti e nei servizi di investimento negli ultimi 5 anni?
    num_op_semestre=0
    for j in range(len(descrizione)):
        if descrizione.iloc[j].find("Investimento")>0:
            num_op_semestre+1
    
    if num_op_semestre == 0:
        n_ris="4"
    elif (num_op_semestre>0) and (num_op_semestre<=5):
        n_ris="3"
    elif (num_op_semestre>5) and (num_op_semestre<=15):
        n_ris="2"
    else:
        n_ris="1"
    
    vett_anagrafica[i]["Risposta "+n_ris][30]="X-"+vett_anagrafica[i]["Risposta "+n_ris][30]

  


    ####risposta 2.1 Quali sono le Sue principali fonti di reddito? (Ammessa risposta multipla)
    ##da definire in base al lavoro e al conto corrente
    

    ####risposta 2.2 Considerando tutte le fonti di reddito, a quanto ammonta il suo reddito medio lordo annuo dichiarato negli ultimi 3 anni?
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


    ####risposta 2.3 Prevede che il suo reddito nel prossimo futuro rispetto al livello attuale sarà:
    #if df["PROFESSIONE"][i]== "Disoccupato":
    #    n_ris="1"
    #elif df["PROFESSIONE"][i]=="Barista":
    #    n_ris="2"
    #elif (df["PROFESSIONE"][i]=="Consulente") or (df["PROFESSIONE"][i]=="Consulente legale"):
    #    n_ris="3"
    #elif df["PROFESSIONE"][i]=="Consulente bancario":
    #    n_ris="4"

    #vett_anagrafica[i]["Risposta "+n_ris][36]="X-"+vett_anagrafica[i]["Risposta "+n_ris][36]


    ####risposta 2.4 In quale delle seguenti fasce rientra il suo patrimonio ﬁnanziario mobiliare complessivo, inclusa la liquidità e le partecipazioni?
    ##da definire in base al conto corrente
    # stipendio_netto_attuale=int(stipendio)*13
    # investimento=stipendio_netto_attuale//10
    # età=df["DATA DI NASCITA"][i]
    # print(type(età))

    ####risposta 2.5 I suoi investimenti immobiliari:
    ##da definire in base al lavoro e al conto corrente in base a che tasse paga
    y=0
    for j in range(len(descrizione)):
        if descrizione.iloc[j].find("Imu")>0:
            y=j
            break
    
    stipendio=estratto_conto["Uscite"].to_list()[y]
    if y!=0:
        n_ris="1"
    else:
        n_ris="2"
    vett_anagrafica[i]["Risposta "+n_ris][36]="X-"+vett_anagrafica[i]["Risposta "+n_ris][36]    


    ####risposta 2.6 Quale è il valore commerciale del suo patrimonio immobiliare?
    ##da definire in base al lavoro e al conto corrente in base a quante tasse paga


    ####risposta 2.7 Il suo patrimonio ﬁnanziario complessivo:
    ##da definire in base al conto corrente


    ####risposta 2.8 In quale fascia ricadono i suoi impegni ﬁnanziari mensili (e.g. mutui, afﬁtti)?
    ##da definire in base al conto corrente


    ####risposta 2.9 Qual è la Sua capacità di risparmio mensile al netto delle spese ricorrenti?
    ##da definire in base al conto corrente

    ####risposta 2.10 Quante persone dipendono economicamente da Lei?
    ##GIA' GESTITA
    



    
    
    vett_anagrafica[i].to_excel("2000503 - QUESTIONARIO PF "+nome+cognome+".xlsx")