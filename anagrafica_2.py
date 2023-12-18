import pandas as pd
import numpy as np
import io
from dizionari import *

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


def crea_questionario(df,estratto_conto):
    doc_dict = {
    '0.1': 'Carta d\'identita\'',
    '0.2': 'Carta d\'identita\'',
    '0.3': 'Carta d\'identita\'',
    '0.5': 'Carta d\'identita\'',
    '0.6': 'Modello 730',
    '1.1': 'Estratto conto',
    '1.2': 'Estratto conto',
    '1.4': 'Istruzione e Impiego',
    '1.5': 'Estratto conto',
    '1.6.1': 'Estratto conto',
    '1.6.2': 'Estratto conto',
    '1.6.3': 'Estratto conto',
    '1.6.4': 'Estratto conto',
    '1.6.5': 'Estratto conto',
    "1.6.6": 'Estratto conto',
    '1.6.7': 'Estratto conto',
    '1.6.8': 'Estratto conto',
    '1.6.9': 'Estratto conto',
    '1.7.1': 'Estratto conto',
    '1.7.2': 'Estratto conto',
    '1.7.3': 'Estratto conto',
    '1.7.4': 'Estratto conto',
    '1.7.5': 'Estratto conto',
    '1.7.6': 'Estratto conto',
    '1.8': 'Estratto conto',
    '2.1': 'Estratto conto',
    '2.2': 'Estratto conto',
    '2.3': 'Estratto conto',
    '2.4': 'Estratto conto',
    '2.5': 'Estratto conto',
    '2.6': 'Estratto conto',
    '2.7': 'Estratto conto',
    '2.8': 'Estratto conto',
    '2.9': 'Estratto conto',
    '2.10': 'Modello 730',
}

    x,y=df.shape
    vett_anagrafica=[]  
    anagrafica = pd.read_excel("2000503 - QUESTIONARIO PF clean.xlsx")
    confidence=[100,100,100,10,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,40,10,10,60,60,60,10]
    gamma=0

    for i in range(x):
        vett_anagrafica.append(anagrafica.copy())
        vett_anagrafica[i]["Unnamed: 0"]=vett_anagrafica[i]["Unnamed: 0"].astype(str)
        vett_anagrafica[i].rename(columns={"Unnamed: 8":"Livello di Confidence"},inplace=True)
        vett_anagrafica[i].rename(columns={"Unnamed: 0":"Sezione"},inplace=True)
        vett_anagrafica[i].rename(columns={"Unnamed: 1":"Domanda"},inplace=True)
        vett_anagrafica[i]["Sezione"]=vett_anagrafica[i]["Sezione"].astype(str)
        vett_anagrafica[i].insert(loc=len(vett_anagrafica[i].columns), column='Origine', value=None)
        
        vett_anagrafica[i].insert(loc=len(vett_anagrafica[i].columns), column='Record Origine', value=None)
        vett_anagrafica[i].to_excel("prova.xlsx")
        
        vett_anagrafica[i]["Risposta 1"][1]=df["COGNOME"][i]
        vett_anagrafica[i]["Livello di Confidence"][1]=confidence[gamma]
        gamma+=1
        vett_anagrafica[i]["Risposta 1"][2]=df["NOME"][i]
        vett_anagrafica[i]["Livello di Confidence"][2]=confidence[gamma]
        gamma+=1
        nome=df["NOME"][i]
        cognome=df["COGNOME"][i]
        vett_anagrafica[i]["Risposta 1"][3]=str(df["DATA DI NASCITA"][i])[0:10]
        vett_anagrafica[i]["Livello di Confidence"][3]=confidence[gamma]
        gamma+=1
        vett_anagrafica[i]["Risposta "+str(conv_sc[df["STATO CIVILE"][i]])][5]="X-"+vett_anagrafica[i]["Risposta "+str(conv_sc[df["STATO CIVILE"][i]])][5]
        vett_anagrafica[i]["Livello di Confidence"][5]=confidence[gamma]
        gamma+=1
        
            
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
        vett_anagrafica[i]["Livello di Confidence"][6]=confidence[gamma]
        gamma+=1
        
        
        
        
        estratto_conto.columns=estratto_conto.iloc[4]
        estratto_conto=estratto_conto[5:]
        descrizione=estratto_conto["Descrizione"]
        
        a=0
        aa=0
        for j in range(len(descrizione)):
            if (descrizione.iloc[j].lower().find("commissione consulenza")>0) or (descrizione.iloc[j].find("commisione e spesa per consulenza")>0):
                a=j
                break
            if (descrizione.iloc[j].lower().find("sottoscrizione fondo")>0) or (descrizione.iloc[j].find("cedola trimestrale fondo")>0):
                aa=j
                break
        
        
        if a!=0:
            
            
            vett_anagrafica[i]["Origine"][8]=doc_dict[str(vett_anagrafica[i]["Sezione"][8])]+" a riga "+str(a+1)
            vett_anagrafica[i]["Record Origine"][8]="Descrizione: "+descrizione.iloc[a]+" Importo: "+str(estratto_conto["Uscite"].to_list()[a])
            n_ris="1"
        else:
            vett_anagrafica[i]["Origine"][8]=doc_dict[vett_anagrafica[i]["Sezione"][8]]
            n_ris="2"
        doc_dict.pop(vett_anagrafica[i]["Sezione"][8])
        vett_anagrafica[i]["Risposta "+n_ris][8]="X-"+vett_anagrafica[i]["Risposta "+n_ris][8]
        vett_anagrafica[i]["Livello di Confidence"][8]=confidence[gamma]
        gamma+=1
        stipendio=estratto_conto["Entrate"].to_list()[a]
        if aa!=0:
            vett_anagrafica[i]["Origine"][9]=doc_dict[vett_anagrafica[i]["Sezione"][9]]+" a riga "+str(aa+1)
            vett_anagrafica[i]["Record Origine"][9]="Descrizione: "+descrizione.iloc[aa]+" Importo: "+str(estratto_conto["Uscite"].to_list()[aa])
            n_ris="1"
        else:
            vett_anagrafica[i]["Origine"][9]=doc_dict[vett_anagrafica[i]["Sezione"][9]]
            n_ris="2"
        doc_dict.pop(vett_anagrafica[i]["Sezione"][9])
        vett_anagrafica[i]["Risposta "+n_ris][9]="X-"+vett_anagrafica[i]["Risposta "+n_ris][9]
        vett_anagrafica[i]["Livello di Confidence"][9]=confidence[gamma]
        gamma+=1
        

        ####risposta 1.4
        # Al ﬁne di diversiﬁcare il rischio degli investimenti, quale delle seguenti soluzioni ritiene più efﬁcace?
        ##Clustering su personam sulla base dell età e del lavoro proveniente dal conto corrente e del numero di familiari a carico
        if df["N. FAMILIARI A CARICO"][i]==0 and df["TITOLO DI STUDIO"][i].find("Laurea") and (df["PROFESSIONE"][i].find("Consulente") or df["PROFESSIONE"][i].find("Direttore")):
            n_ris="1"
        else:
            n_ris="2"
        vett_anagrafica[i]["Risposta "+n_ris][11]="X-"+vett_anagrafica[i]["Risposta "+n_ris][11]
        vett_anagrafica[i]["Livello di Confidence"][11]=confidence[gamma]
        gamma+=1
        
        ####risposta 1.5
        #Più si allunga l’orizzonte temporale dell’investimento, più risultano mitigati i rischi di perdita che caratterizzano, invece, 
        #il medesimo investimento valutato su un orizzonte temporale più breve. Concorda con questa affermazione?
        ##da definire sulla base di età, movimenti conto, lavoro ed educazione
        a=0
        aa=0
        for j in range(len(descrizione)):
            
            if (descrizione.iloc[j].lower().find("piano di accumulo")>=0):
                
                a=j+1
                break
        if a!=0:
            vett_anagrafica[i]["Origine"][12]=doc_dict[vett_anagrafica[i]["Sezione"][12]]+" a riga "+str(a+1)
            vett_anagrafica[i]["Record Origine"][12]="Descrizione: "+descrizione.iloc[a]+" Importo: "+str(estratto_conto["Uscite"].to_list()[a])
            n_ris="1"
        else:
            vett_anagrafica[i]["Origine"][12]=doc_dict[vett_anagrafica[i]["Sezione"][12]]
            n_ris="2"
        doc_dict.pop(vett_anagrafica[i]["Sezione"][12])
        vett_anagrafica[i]["Risposta "+n_ris][12]="X-"+vett_anagrafica[i]["Risposta "+n_ris][12]
        vett_anagrafica[i]["Livello di Confidence"][12]=confidence[gamma]
        gamma+=1
        
        #tutte da definire sulla base di età, movimenti conto, lavoro ed educazione
        ##Tutte Vero/Falso
        ####risposta 1.6.1
        # Il rendimento di attività a basso rischio potrebbe signiﬁcare la perdita del potere di acquisto derivante dal mancato recupero dell’inﬂazione
        a=0
        for j in range(len(descrizione)):
                
                if (descrizione.iloc[j].lower().find("fondo monetario")>=0):
                    
                    a=j+1
                    break
        
        if df["TITOLO DI STUDIO"][i].find("Laurea")>=0 and a!=0:
            vett_anagrafica[i]["Origine"][14]=doc_dict[vett_anagrafica[i]["Sezione"][14]]+" a riga "+str(a+1)
            vett_anagrafica[i]["Record Origine"][14]="Descrizione: "+descrizione.iloc[a]+" Importo: "+str(estratto_conto["Uscite"].to_list()[a])
           
            n_ris="1"
            
        else:
            vett_anagrafica[i]["Origine"][14]=doc_dict[vett_anagrafica[i]["Sezione"][14]]
            n_ris = "2"
        vett_anagrafica[i]["Risposta "+n_ris][14]="X-"+vett_anagrafica[i]["Risposta "+n_ris][14] 
        vett_anagrafica[i]["Livello di Confidence"][14]=confidence[gamma]
        gamma+=1
        doc_dict.pop(vett_anagrafica[i]["Sezione"][14])
        
        ####risposta 1.6.2
        #Strumenti Obbligazionari: Nel confronto tra un titolo obbligazionario di un Emittente a basso rischio ed un titolo obbligazionario 
        #caratterizzato da un rating peggiore, quest’ultimo dovrebbe offrire un rendimento atteso più basso perché il rischio di insolvenza è maggiore
        
        ####risposta 1.6.3
        #Strumenti Obbligazionari: L’acquisto di un titolo obbligazionario emesso in una valuta diversa dall’Euro comporta l’esposizione anche al rischio di cambio
        a=0
        for j in range(len(descrizione)):
                
                if (descrizione.iloc[j].lower().find("obbligazioni")>=0 or descrizione.iloc[j].lower().find("btp")>=0):
                    
                    a=j
                    break
        if a!=0:
            vett_anagrafica[i]["Origine"][15]=doc_dict[vett_anagrafica[i]["Sezione"][15]]+" a riga "+str(a+1)
            vett_anagrafica[i]["Record Origine"][15]="Descrizione: "+descrizione.iloc[a]+" Importo: "+str(estratto_conto["Uscite"].to_list()[a])
            vett_anagrafica[i]["Origine"][16]=doc_dict[vett_anagrafica[i]["Sezione"][16]]+" a riga "+str(a+1)
            vett_anagrafica[i]["Record Origine"][16]="Descrizione: "+descrizione.iloc[a]+" Importo: "+str(estratto_conto["Uscite"].to_list()[a])
            n_ris="1"
        else:
            vett_anagrafica[i]["Origine"][15]=doc_dict[vett_anagrafica[i]["Sezione"][15]]
            vett_anagrafica[i]["Origine"][16]=doc_dict[vett_anagrafica[i]["Sezione"][16]]
            n_ris="2"
        vett_anagrafica[i]["Risposta "+n_ris][15]="X-"+vett_anagrafica[i]["Risposta "+n_ris][15]
        vett_anagrafica[i]["Livello di Confidence"][15]=confidence[gamma]
        gamma+=1
        vett_anagrafica[i]["Risposta "+n_ris][16]="X-"+vett_anagrafica[i]["Risposta "+n_ris][16]
        vett_anagrafica[i]["Livello di Confidence"][16]=confidence[gamma]
        gamma+=1
        doc_dict.pop(vett_anagrafica[i]["Sezione"][15])
        doc_dict.pop(vett_anagrafica[i]["Sezione"][16])
        ####risposta 1.6.4
        #Strumenti Azionari: Le azioni, a causa dei cambiamenti delle condizioni generali di mercato (rischio sistemico) e/o 
        #della diffusione di informazioni relative alle singole società emittenti (rischio speciﬁco) possono subire una variazione anche signiﬁcativa e repentina dei prezzi
        a=0
        for j in range(len(descrizione)):
                
                if (descrizione.iloc[j].lower().find("azioni")>=0):
                    
                    a=j+1
                    break
        if a!=0:
            vett_anagrafica[i]["Origine"][17]=doc_dict[vett_anagrafica[i]["Sezione"][17]]+" a riga "+str(a+1)
            vett_anagrafica[i]["Record Origine"][17]="Descrizione: "+descrizione.iloc[a]+" Importo: "+str(estratto_conto["Uscite"].to_list()[a])
            n_ris="1"
        else:
            vett_anagrafica[i]["Origine"][17]=doc_dict[vett_anagrafica[i]["Sezione"][17]]
            n_ris="2"
        vett_anagrafica[i]["Risposta "+n_ris][17]="X-"+vett_anagrafica[i]["Risposta "+n_ris][17]
        vett_anagrafica[i]["Livello di Confidence"][17]=confidence[gamma] 
        gamma+=1
        doc_dict.pop(vett_anagrafica[i]["Sezione"][17])
        # vett_anagrafica[i]["Risposta "+n_ris][17]="X-"+vett_anagrafica[i]["Risposta "+n_ris][17]
    
        
        ####risposta 1.6.5
        #OICVM (Fondi Armonizzati): L’investimento in OICVM consente, anche a chi dispone di importi limitati, di beneﬁciare di una diversiﬁcazione di portafoglio e di una gestione professionale
        a=0
        for j in range(len(descrizione)):
                
                if (descrizione.iloc[j].lower().find("fidelity")>=0):
                    
                    a=j
                    break
        if a!=0:
            vett_anagrafica[i]["Origine"][18]=doc_dict[vett_anagrafica[i]["Sezione"][18]]+" a riga "+str(a+1)
            vett_anagrafica[i]["Record Origine"][18]="Descrizione: "+descrizione.iloc[a]+" Importo: "+str(estratto_conto["Uscite"].to_list()[a])
            vett_anagrafica[i]["Origine"][19]=doc_dict[vett_anagrafica[i]["Sezione"][19]]+" a riga "+str(a+1)
            vett_anagrafica[i]["Record Origine"][19]="Descrizione: "+descrizione.iloc[a]+" Importo: "+str(estratto_conto["Uscite"].to_list()[a])
            
            n_ris="1"
        else:
            vett_anagrafica[i]["Origine"][18]=doc_dict[vett_anagrafica[i]["Sezione"][18]]
            vett_anagrafica[i]["Origine"][19]=doc_dict[vett_anagrafica[i]["Sezione"][19]]
            n_ris="2"
        vett_anagrafica[i]["Risposta "+n_ris][18]="X-"+vett_anagrafica[i]["Risposta "+n_ris][18]
        vett_anagrafica[i]["Livello di Confidence"][18]=confidence[gamma]
        gamma+=1
        vett_anagrafica[i]["Risposta "+n_ris][19]="X-"+vett_anagrafica[i]["Risposta "+n_ris][19]
        vett_anagrafica[i]["Livello di Confidence"][19]=confidence[gamma]
        gamma+=1
        doc_dict.pop(vett_anagrafica[i]["Sezione"][18])
        doc_dict.pop(vett_anagrafica[i]["Sezione"][19])  
        ####risposta 1.6.6
        #OICVM (Fondi Armonizzati): Il rischio di un OICVM può differire sensibilmente in funzione della strategia di investimento 
        #adottata dal gestore (a scadenza breve o medio-lunga, denominati in Euro o in altre valute, etc.)
        
        
        ####risposta 1.6.7
        #Prodotti di Investimento Assicurativi: La polizza unit-linked si deﬁnisce tale perché il suo valore è strettamente collegato al valore delle quote dei fondi in cui investe
        a=0
        for j in range(len(descrizione)):
                
                if (descrizione.iloc[j].lower().find("polizza")>=0):
                    
                    a=j+1
                    break
        if a!=0:
            vett_anagrafica[i]["Origine"][20]=doc_dict[vett_anagrafica[i]["Sezione"][20]]+" a riga "+str(a+1)
            vett_anagrafica[i]["Record Origine"][20]="Descrizione: "+descrizione.iloc[a]+" Importo: "+str(estratto_conto["Uscite"].to_list()[a])
            n_ris="1"
        else:
            vett_anagrafica[i]["Origine"][20]=doc_dict[vett_anagrafica[i]["Sezione"][20]]
            n_ris="2"
        vett_anagrafica[i]["Risposta "+n_ris][20]="X-"+vett_anagrafica[i]["Risposta "+n_ris][20]
        vett_anagrafica[i]["Livello di Confidence"][20]=confidence[gamma]
        gamma+=1
        doc_dict.pop(vett_anagrafica[i]["Sezione"][20])
        
        ####risposta 1.6.8
        #Prodotti Alternativi di Investimento: I Fondi di Private Equity investono nel capitale di rischio di aziende normalmente non quotate per 
        # realizzare un rendimento nel medio-lungo termine tramite lo smobilizzo futuro di tali partecipazioni
        if df["PROFESSIONE"][i]=="Contabile" or df["PROFESSIONE"][i]=="Imprenditore settore investimenti":
            n_ris="1"
        else:
            n_ris="2"
            
        vett_anagrafica[i]["Risposta "+n_ris][21]="X-"+vett_anagrafica[i]["Risposta "+n_ris][21]
        vett_anagrafica[i]["Livello di Confidence"][21]=confidence[gamma]
        gamma+=1
        vett_anagrafica[i]["Risposta "+n_ris][22]="X-"+vett_anagrafica[i]["Risposta "+n_ris][22]
        vett_anagrafica[i]["Livello di Confidence"][22]=confidence[gamma]
        gamma+=1
        ####risposta 1.6.9
        #Prodotti Alternativi di Investimento: I Fondi di Investimento Alternativo chiusi non sono caratterizzati da limitazioni al disinvestimento durante la loro vita anagraﬁca





        ####risposta 1.7.1 Ha effettuato negli ultimi 5 anni investimenti nei seguenti prodotti/servizi Strumenti Mercato Monetario
        b=0
        for j in range(len(descrizione)):
            if descrizione.iloc[j].lower().find("fondo monetario")>0:
                b=j
                break
        
        
        if b!=0:
            vett_anagrafica[i]["Origine"][24]=doc_dict[vett_anagrafica[i]["Sezione"][24]]+" a riga "+str(b+1)
            vett_anagrafica[i]["Record Origine"][24]="Descrizione: "+descrizione.iloc[b]+" Importo: "+str(estratto_conto["Uscite"].to_list()[b])
            n_ris="1"
        else:
            vett_anagrafica[i]["Origine"][24]=doc_dict[vett_anagrafica[i]["Sezione"][24]]
            n_ris="2"
        vett_anagrafica[i]["Risposta "+n_ris][24]="X-"+vett_anagrafica[i]["Risposta "+n_ris][24]
        vett_anagrafica[i]["Livello di Confidence"][24]=confidence[gamma]
        gamma+=1
        doc_dict.pop(vett_anagrafica[i]["Sezione"][24])


        ####risposta 1.7.2 Ha effettuato negli ultimi 5 anni investimenti nei seguenti prodotti/servizi Strumenti Obbligazionari
        c=0
        for j in range(len(descrizione)):
            if descrizione.iloc[j].lower().find("obbligazioni")>0:
                c=j
                break
        
        
        if c!=0:
            vett_anagrafica[i]["Origine"][25]=doc_dict[vett_anagrafica[i]["Sezione"][25]]+" a riga "+str(c+1)
            vett_anagrafica[i]["Record Origine"][25]="Descrizione: "+descrizione.iloc[c]+" Importo: "+str(estratto_conto["Uscite"].to_list()[c])
            n_ris="1"
        else:
            vett_anagrafica[i]["Origine"][25]=doc_dict[vett_anagrafica[i]["Sezione"][25]]
            n_ris="2"
        vett_anagrafica[i]["Risposta "+n_ris][25]="X-"+vett_anagrafica[i]["Risposta "+n_ris][25]
        vett_anagrafica[i]["Livello di Confidence"][25]=confidence[gamma]
        gamma+=1
        doc_dict.pop(vett_anagrafica[i]["Sezione"][25])
        ####risposta 1.7.3 Ha effettuato negli ultimi 5 anni investimenti nei seguenti prodotti/servizi Strumenti Azionari
        d=0
        for j in range(len(descrizione)):
            if descrizione.iloc[j].lower().find("azioni")>0:
                d=j
                break
        
        stipendio=estratto_conto["Entrate"].to_list()[d]
        if d!=0:
            vett_anagrafica[i]["Origine"][26]=doc_dict[vett_anagrafica[i]["Sezione"][26]]+" a riga "+str(d+1)
            vett_anagrafica[i]["Record Origine"][26]="Descrizione: "+descrizione.iloc[d]+" Importo: "+str(estratto_conto["Uscite"].to_list()[d])
            n_ris="1"
        else:
            vett_anagrafica[i]["Origine"][26]=doc_dict[vett_anagrafica[i]["Sezione"][26]]
            n_ris="2"
        vett_anagrafica[i]["Risposta "+n_ris][26]="X-"+vett_anagrafica[i]["Risposta "+n_ris][26]
        vett_anagrafica[i]["Livello di Confidence"][26]=confidence[gamma]
        gamma+=1
        doc_dict.pop(vett_anagrafica[i]["Sezione"][26])
        

        ####risposta 1.7.4 Ha effettuato negli ultimi 5 anni investimenti nei seguenti prodotti/servizi OICVM (Fondi Armonizzati)
        e=0
        for j in range(len(descrizione)):
            if descrizione.iloc[j].lower().find("fondo")>0:
                e=j
                break
        
        stipendio=estratto_conto["Entrate"].to_list()[e]
        if e!=0:
            vett_anagrafica[i]["Origine"][27]=doc_dict[vett_anagrafica[i]["Sezione"][27]]+" a riga "+str(e+1)
            vett_anagrafica[i]["Record Origine"][27]="Descrizione: "+descrizione.iloc[e]+" Importo: "+str(estratto_conto["Uscite"].to_list()[e])
            n_ris="1"
        else:
            vett_anagrafica[i]["Origine"][27]=doc_dict[vett_anagrafica[i]["Sezione"][27]]
            n_ris="2"
        vett_anagrafica[i]["Risposta "+n_ris][27]="X-"+vett_anagrafica[i]["Risposta "+n_ris][27]
        vett_anagrafica[i]["Livello di Confidence"][27]=confidence[gamma]
        gamma+=1
        doc_dict.pop(vett_anagrafica[i]["Sezione"][27])

        ####risposta 1.7.5 Ha effettuato negli ultimi 5 anni investimenti nei seguenti prodotti/servizi Prodotti di Investimento Assicurativi
        f=0
        for j in range(len(descrizione)):
            if descrizione.iloc[j].lower().find("polizza")>0:
                f=j
                break
        
        stipendio=estratto_conto["Entrate"].to_list()[f]
       
        if f!=0:
            vett_anagrafica[i]["Origine"][28]=doc_dict[vett_anagrafica[i]["Sezione"][28]]+" a riga "+str(f+1)
            vett_anagrafica[i]["Record Origine"][28]="Descrizione: "+descrizione.iloc[f]+" Importo: "+str(estratto_conto["Uscite"].to_list()[f])
            doc_dict.pop(vett_anagrafica[i]["Sezione"][28])
            n_ris="1"
        else:
            vett_anagrafica[i]["Origine"][28]=doc_dict[vett_anagrafica[i]["Sezione"][28]]
            n_ris="2"
        print(n_ris)
        vett_anagrafica[i]["Risposta "+n_ris][28]="X-"+vett_anagrafica[i]["Risposta "+n_ris][28]
        vett_anagrafica[i]["Livello di Confidence"][28]=confidence[gamma]
        gamma+=1  
    ####risposta 1.7.6 Ha effettuato negli ultimi 5 anni investimenti nei seguenti prodotti/servizi Prodotti Alternativi di Investimento
        g=0
        for j in range(len(descrizione)):
            if descrizione.iloc[j].lower().find("fondo private equity")>0:
                g=j
                break
        
        stipendio=estratto_conto["Entrate"].to_list()[g]
        if  g!=0:
            vett_anagrafica[i]["Origine"][29]=doc_dict[vett_anagrafica[i]["Sezione"][29]]+" a riga "+str(g+1)
            vett_anagrafica[i]["Record Origine"][29]="Descrizione: "+descrizione.iloc[g]+" Importo: "+str(estratto_conto["Uscite"].to_list()[g])
            doc_dict.pop(vett_anagrafica[i]["Sezione"][29])
            n_ris="1"
        else:
            vett_anagrafica[i]["Origine"][29]=doc_dict[vett_anagrafica[i]["Sezione"][29]]
            n_ris="2"
        vett_anagrafica[i]["Risposta "+n_ris][29]="X-"+vett_anagrafica[i]["Risposta "+n_ris][29]
        vett_anagrafica[i]["Livello di Confidence"][29]=confidence[gamma]
        gamma+=1
        

        vett=["fondo","azioni","btp","obbligazioni","fondo monetario","polizza","fondo private equity"]
        ####risposta 1.8 Con quale frequenza ha effettuato operazioni negli strumenti e nei servizi di investimento negli ultimi 5 anni?
        num_op_semestre=0
        for j in range(len(descrizione)):
            for k in vett:
                if descrizione.iloc[j].find(k)>0:
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
        vett_anagrafica[i]["Livello di Confidence"][30]=confidence[gamma]
        gamma+=1

    


        ####risposta 2.1 Quali sono le Sue principali fonti di reddito? (Ammessa risposta multipla)
        #come gestisco risposta multipla?
        ##se non è disoccupato, -> risposta 1
        if df["PROFESSIONE"][i]!= "Disoccupato" or df["PROFESSIONE"][i]!= "Imprenditore settore investimenti":
            n_ris="1"
        vett_anagrafica[i]["Risposta "+n_ris][32]="X-"+vett_anagrafica[i]["Risposta "+n_ris][32]  
        vett_anagrafica[i]["Livello di Confidence"][32]=confidence[gamma]
        gamma+=1

        #se tra entrate è presente 'partita iva' -> risposta 2
        #ax= 0
        #for j in range(len(descrizione)):
        #    if descrizione.iloc[j].find("Partita iva")>0:
        #        ax=j
        #        break

        #entrate = estratto_conto["Entrate"].to_list()[ax]
        #if ax!=0:
        # n_ris="2"
        # vett_anagrafica[i]["Risposta "+n_ris][28]="X-"+vett_anagrafica[i]["Risposta "+n_ris][28] 
        
        #se tra entrate è presente 'impresa' -> risposta 3
        #se tra entrate è presente 'azioni finanziarie' -> risposta 4
        #se tra entrate è presente 'rendita immobiliare' -> risposta 5
        

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
        
        if a!=0 and pd.notna(a):
            vett_anagrafica[i]["Risposta "+n_ris][33]="X-"+vett_anagrafica[i]["Risposta "+n_ris][33]
            vett_anagrafica[i]["Origine"][33]=doc_dict[vett_anagrafica[i]["Sezione"][33]]+" a riga "+str(a+1)
            doc_dict.pop(vett_anagrafica[i]["Sezione"][33])
            vett_anagrafica[i]["Record Origine"][33]="Descrizione: "+descrizione.iloc[a]+" Importo: "+str(estratto_conto["Entrate"].to_list()[a])
        else:
            vett_anagrafica[i]["Risposta "+n_ris][33]="X-"+vett_anagrafica[i]["Risposta "+n_ris][33]
        vett_anagrafica[i]["Livello di Confidence"][33]=confidence[gamma]
        gamma+=1


        ####risposta 2.3 Prevede che il suo reddito nel prossimo futuro rispetto al livello attuale sarà:
        if df["PROFESSIONE"][i]== "Disoccupato":
            n_ris="1"
        elif df["PROFESSIONE"][i]=="Insegnante":
            n_ris="2"
        elif (df["PROFESSIONE"][i]=="Medico") or (df["PROFESSIONE"][i]=="Contabile"):
            n_ris="3"
        elif df["PROFESSIONE"][i]=="Imprenditore settore investimenti":
            n_ris="4"

        vett_anagrafica[i]["Risposta "+n_ris][34]="X-"+vett_anagrafica[i]["Risposta "+n_ris][34]
        vett_anagrafica[i]["Livello di Confidence"][34]=confidence[gamma]
        gamma+=1


        ####risposta 2.4 In quale delle seguenti fasce rientra il suo patrimonio ﬁnanziario mobiliare complessivo, inclusa la liquidità e le partecipazioni?
        ##da definire in base al conto corrente
        # stipendio_netto_attuale=int(stipendio)*13
        # investimento=stipendio_netto_attuale//10
        # età=df["DATA DI NASCITA"][i]
        # print(type(età))
        somm=["accredito cedole","acquisto fondo monetario"]
        alpha=0
        for j in range(len(descrizione)):
            for k in somm:
                    if descrizione.iloc[j].lower().find(k)>0:
                        alpha+=estratto_conto["Entrate"].to_list()[j]
        alpha=alpha*4
        
        if alpha<50000:
            n_ris="1"
        elif alpha<150000:
            n_ris="2"
        elif alpha<500000:
            n_ris="3"
        elif alpha<1000000:
            n_ris="4"
        else:
            n_ris="5"
        vett_anagrafica[i]["Risposta "+n_ris][35]="X-"+vett_anagrafica[i]["Risposta "+n_ris][35]
        vett_anagrafica[i]["Livello di Confidence"][35]=confidence[gamma]
        gamma+=1
        ####risposta 2.5 I suoi investimenti immobiliari:
        ##da definire in base al lavoro e al conto corrente in base a che tasse paga
        y=-1
        for j in range(len(descrizione)):
            if descrizione.iloc[j].lower().find("imu")>0 or descrizione.iloc[j].lower().find("mutuo")>0:
                y=j
                break
        
        stipendio=estratto_conto["Uscite"].to_list()[y]
        if y!=-1:
            vett_anagrafica[i]["Origine"][36]=doc_dict[vett_anagrafica[i]["Sezione"][36]]+" a riga "+str(y+1)
            vett_anagrafica[i]["Record Origine"][36]="Descrizione: "+descrizione.iloc[y]+" Importo: "+str(estratto_conto["Uscite"].to_list()[y])
            n_ris="1"
        else:
            vett_anagrafica[i]["Origine"][36]=doc_dict[vett_anagrafica[i]["Sezione"][36]]
            n_ris="2"
        vett_anagrafica[i]["Risposta "+n_ris][36]="X-"+vett_anagrafica[i]["Risposta "+n_ris][36]
        vett_anagrafica[i]["Livello di Confidence"][36]=confidence[gamma]
        gamma+=1   
        doc_dict.pop(vett_anagrafica[i]["Sezione"][36]) 


        ####risposta 2.6 Quale è il valore commerciale del suo patrimonio immobiliare?
        ##da definire in base al lavoro e al conto corrente in base a quante tasse paga
        y=0
        for j in range(len(descrizione)):
            if descrizione.iloc[j].lower().find("imu")>0 or descrizione.iloc[j].lower().find("mutuo")>0:
                y=j
                break
        
        p_imm=estratto_conto["Uscite"].to_list()[y]
        
        if p_imm<5000 or pd.notna(p_imm)==False:
            n_ris="1"
        elif p_imm<10000:
            n_ris="2"
        else:
            n_ris="3"
     
        
        vett_anagrafica[i]["Risposta "+n_ris][37]="X-"+vett_anagrafica[i]["Risposta "+n_ris][37]
        vett_anagrafica[i]["Livello di Confidence"][37]=confidence[gamma]
        gamma+=1

        ####risposta 2.7 Il suo patrimonio ﬁnanziario complessivo:
        ##da definire in base al conto corrente
        if df["PROFESSIONE"][i]== "Disoccupato":
            n_ris="1"
        elif df["PROFESSIONE"][i]=="Insegnante":
            n_ris="1"
        elif (df["PROFESSIONE"][i]=="Medico") or (df["PROFESSIONE"][i]=="Contabile"):
            n_ris="2"
        elif df["PROFESSIONE"][i]=="Imprenditore settore investimenti":
            n_ris="3"

        vett_anagrafica[i]["Risposta "+n_ris][38]="X-"+vett_anagrafica[i]["Risposta "+n_ris][38]
        vett_anagrafica[i]["Livello di Confidence"][38]=confidence[gamma]
        gamma+=1

        ####risposta 2.8 In quale fascia ricadono i suoi impegni ﬁnanziari mensili (e.g. mutui, afﬁtti)?
        ##da definire in base al conto corrente
        for j in range(len(descrizione)):
            if descrizione.iloc[j].lower().find("imu")>0 or descrizione.iloc[j].lower().find("mutuo")>0:
                y=j
                break
        
        stipendio=estratto_conto["Uscite"].to_list()[y]
        if stipendio==0 or pd.notna(stipendio)==False:
            n_ris="1"
        elif stipendio<1000:
            n_ris="2"
        elif stipendio<2500:
            n_ris="3"
        else:
            n_ris="4"
        vett_anagrafica[i]["Risposta "+n_ris][39]="X-"+vett_anagrafica[i]["Risposta "+n_ris][39]
        vett_anagrafica[i]["Livello di Confidence"][39]=confidence[gamma]
        gamma+=1

        ####risposta 2.9 Qual è la Sua capacità di risparmio mensile al netto delle spese ricorrenti?
        ##da definire in base al conto corrente
        if df["PROFESSIONE"][i]== "Disoccupato":
            n_ris="1"
        elif df["PROFESSIONE"][i]=="Insegnante" or (df["PROFESSIONE"][i]=="Contabile"):
            n_ris="1"
        elif (df["PROFESSIONE"][i]=="Medico") :
            n_ris="2"
        elif df["PROFESSIONE"][i]=="Imprenditore settore investimenti":
            n_ris="3"

        vett_anagrafica[i]["Risposta "+n_ris][40]="X-"+vett_anagrafica[i]["Risposta "+n_ris][40]
        vett_anagrafica[i]["Livello di Confidence"][40]=confidence[gamma]
        gamma+=1
        ####risposta 2.10 Quante persone dipendono economicamente da Lei?
        ##GIA' GESTITA
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
        
        vett_anagrafica[i]["Risposta "+n_ris][41]="X-"+vett_anagrafica[i]["Risposta "+n_ris][41]
        vett_anagrafica[i]["Livello di Confidence"][41]=confidence[gamma]
        
        
        indice_da_inizio_rimozione = 42  
        vett_anagrafica[i] = vett_anagrafica[i].drop(index=range(indice_da_inizio_rimozione, len(vett_anagrafica[i])))
        vett_anagrafica[i].set_index('Sezione', inplace=True)
        for k in doc_dict.keys():
            vett_anagrafica[i]["Origine"][k]=doc_dict[k]
        
        buffer=io.BytesIO()
        
        vett_anagrafica[i].to_excel("2000503 - QUESTIONARIO PF "+nome+cognome+".xlsx")
        vett_anagrafica[i].to_excel(buffer,index=False)
        buffer.seek(0)
        return buffer
    
    
    
df=pd.read_excel("Anagrafica.xlsx")
pdf_path="2000503 - QUESTIONARIO PF MarioRossi.pdf"
df_anagrafica=df.iloc[0]
estratto_conto=pd.read_excel("EstrattoConto MarioRossi.xlsx")
df_anagrafica=pd.DataFrame(df_anagrafica).transpose()
crea_questionario(df_anagrafica,estratto_conto)