# Vittorio Mussin v.mussin@studenti.unipi.it 3319473310
import sys
import nltk
import string
import math

def nlp(frasi):
    """Restituisce l'insieme dei token 
    e delle coppie token-POS"""
    
    tokens=[]
    POS=[]
    NER_P=[]
    for frase in frasi:
        token=nltk.word_tokenize(frase)
        pos=nltk.pos_tag(token)

        analisi=nltk.ne_chunk(pos)
        
        for nodo in analisi:
            NE=""
            if hasattr(nodo, "label"):
                if nodo.label()in ["PERSON"]:
                    for partNE in nodo.leaves():
                        NE+=" "+partNE[0]
                    NER_P.append(NE)

        tokens.append(token)
        POS+=pos
    return tokens, POS, NER_P


def removedpunctuation(POS,tokens):
    """Genera una lista di token suddivisi in frasi
    e una lista di coppie token-POS, entrambe senza 
    la punteggiatura"""
    
    T=[]
    P=[]
    p=string.punctuation #insieme dei simboli di punteggiatura
    i=0
    for frase in tokens:
        ifrase=0 #ifrase serve per accedere all'indice delle parole per ogni "frase" in "tokens"
        F=[]
        while ifrase<len(frase):
            if not POS[i][1] in p:
                P+=(POS[i][0],POS[i][1]),
                F.append(frase[ifrase])
            ifrase+=1
            i+=1
        T.append(F)
            
    return P,T

def bi_tri(files,POS_depunct):
    """Restituisce liste di bigrammi e trigrammi"""
    
    bigrammi=[]
    trigrammi=[]
    for n in range(len(files)):
        b=list(nltk.bigrams(POS_depunct[n]))
        t=list(nltk.trigrams(POS_depunct[n]))
        bigrammi.append(b)
        trigrammi.append(t)
    return bigrammi,trigrammi

def primotask(files,POS, bigrammi, trigrammi):
    """Funzione del primo compito del Programma 2"""
    
    formato="|{:<15}| {:<15}| {:<15}| {:<15}|"
    l=[] #lista che conterrà le due distribuzioni di frequenza delle POS dei due file
    p=[] #lista che conterrà le due liste dell'insieme delle POS dei due file
    d="-------------------------------------------------------------------------------------"
    
    #--------------------------Creazione di "l" e "p"---------------------------------------
    for n in range(len(files)):
        listapos=[i[1] for i in POS[n]]
        pos_freq={i:listapos.count(i) for i in set(listapos)}
        pos_freq_sorted=sorted(pos_freq.items(),key=lambda item:item[1], reverse=True)
        l.append(pos_freq_sorted)
        p.append(listapos)

    #---------------------------10 POS più frequenti--------------------------------------
    print(formato.format(nome_file(files[0], grassetto=False), "", nome_file(files[1], grassetto=False), "")) #
    #print(d)
    print(formato.format("--------------", "--------------", "--------------", "--------------"))
    print(formato.format("POS", "Frequency", "POS", "Frequency"))
    for i in range(10):
        p_0=l[0][i][0] #iesima POS più frequente del primo file
        f_0=l[0][i][1] #frequenza dell'iesima POS più frequente del primo file 
        p_1=l[1][i][0] #iesima POS più frequente del secondo file 
        f_1=l[1][i][1] #frequenza dell'iesima POS più frequente del secondo file 
        print(formato.format(p_0, f_0, p_1, f_1))
    print()
    
    #--------------------Estrazione delle sole POS dai bigrammi e trigrammi-------------------
    bigrammi_POS=[]#lista che conterrà le due liste dell'insieme dei bigrammi delle POS dei due file
    trigrammi_POS=[]#lista che conterrà le due liste dell'insieme dei trigrammi delle POS dei due file
    for n in range(len(files)):
        bigramma_POS=[(i[0][1],i[1][1]) for i in bigrammi[n]] #lista dei soli bigrammi delle POS
        bigrammi_POS.append(bigramma_POS)
        trigramma_POS=[(i[0][1],i[1][1],i[2][1]) for i in trigrammi[n]]#lista dei soli trigrammi delle POS
        trigrammi_POS.append(trigramma_POS)
    
    #--------------------------10 bigrammi POS più frequenti-------------------------------
    b=[] #lista che conterrà le due distribuzioni di frequenza dei bigrammi delle POS dei due file
    for n in range(len(files)):
        b_freq_sorted=sorted(
            {i:bigrammi_POS[n].count(i) for i in set(bigrammi_POS[n])}.items(),
            key=lambda item:item[1],
            reverse=True)
        b.append(b_freq_sorted)
    print(formato.format(nome_file(files[0], grassetto=False), "", nome_file(files[1], grassetto=False), ""))
    #print(d)
    print(formato.format("--------------", "--------------", "--------------", "--------------"))
    print(formato.format("POS Bigram", "Frequency", "POS Bigram", "Frequency"))
    for i in range (10):
        bi_0=b[0][i][0][0]+" "+b[0][i][0][1] #b[0/1][i] ha come struttura ((<POS>,<POS>),<frequenza>)
        f_0=b[0][i][1]
        bi_1=b[1][i][0][0]+" "+b[1][i][0][1] #b[0/1][i] ha come struttura ((<POS>,<POS>),<frequenza>)
        f_1=b[1][i][1]
        print(formato.format(bi_0, f_0, bi_1, f_1))
    print()
    #--------------------------10 trigrammi POS più frequenti-------------------------------
    t=[] #lista che conterrà le due distribuzioni di frequenza dei trigrammi delle POS dei due file
    for n in range(len(files)):
        t_freq_sorted=sorted(
            {i:trigrammi_POS[n].count(i) for i in set(trigrammi_POS[n])}.items(),
            key=lambda item:item[1],
            reverse=True)
        t.append(t_freq_sorted)
    print(formato.format(nome_file(files[0], grassetto=False), "", nome_file(files[1], grassetto=False), ""))
    #print(d)
    print(formato.format("--------------", "--------------", "--------------", "--------------"))
    print(formato.format("POS Trigram","Frequency","POS Trigram","Frequency"))
    for i in range(10):
        tri_0=t[0][i][0][0]+" "+t[0][i][0][1]+" "+t[0][i][0][2] #t[0/1][i] ha come struttura ((<POS>,<POS>,<POS>),<frequenza>)
        f_0=t[0][i][1]
        tri_1=t[1][i][0][0]+" "+t[1][i][0][1]+" "+t[1][i][0][2] #t[0/1][i] ha come struttura ((<POS>,<POS>,<POS>),<frequenza>)
        f_1=t[1][i][1]
        print(formato.format(tri_0,f_0,tri_1,f_1))
    print()


    #---------------------------20 Aggettivi e Avverbi più frequenti--------------------------
    Ag=[] #lista che conterrà le distribuzioni di frequenza degli aggettivi per i due file
    Av=[] #lista che conterrà le distribuzioni di frequenza degli avverbi per i due file

    for n in range(len(files)):
        pos_ag=[i for i in POS[n] if i[1] in "JJ JJR JJS"]
        pos_av=[i for i in POS[n] if i[1] in "RB RBR RBS"]
        ag_freq={i:pos_ag.count(i) for i in set(pos_ag)}
        av_freq={i:pos_av.count(i) for i in set(pos_av)}

        ag_freq_sorted=sorted(ag_freq.items(),key=lambda item:item[1], reverse=True)
        av_freq_sorted=sorted(av_freq.items(),key=lambda item:item[1], reverse=True)
        
        Ag.append(ag_freq_sorted)
        Av.append(av_freq_sorted)
    for n in range(len(files)):
        print(nome_file(files[n], grassetto=True))
        #print(d)
        print(formato.format("Adjective","Frequency","Adverb","Frequency"))
        print(formato.format("--------------", "--------------", "--------------", "--------------"))
        for i in range(20):
            print(formato.format(Ag[n][i][0][0], Ag[n][i][1], Av[n][i][0][0],Av[n][i][1]))
            #Ag/Av[n][i] ha come struttura ((<token>,<POS>),<frequenza>)
        print()


def secondotask(files, bigrammi, tokens_POS):
    """Estrae i 20 bigrammi Aggettivo e Sostantivo 
    dove ogni token ha una frequenza maggiore di tre"""

    formato="|{:<30}| {:<20} |{:<30} |{:<20}| {:<30} |{:<20}|"
    nomi="NN NNS NNP NNPS"
    agg="JJ JJR JJS"
    
    #-----------------------------estrazione dei bigrammi----------------------------------------
    Stampa=[] #lista che conterrà le due distrubuzioni di frequenza di bigrammi di nomi e aggettivi con frequenza>3 dei due file
    for n in range(len(files)):
        coppie={}
        for bigramma in set(bigrammi[n]):
            #condizione per bigramma aggettivo-nome/nome-aggettivo
            if (bigramma[0][1]in agg and bigramma[1][1] in nomi) or (bigramma[0][1]in nomi and bigramma[1][1] in agg):
                #condizione per la frequenza di ciascun elemento del bigramma con frequenza>3
                freq_b_0=tokens_POS[n].count(bigramma[0])
                freq_b_1=tokens_POS[n].count(bigramma[1])
                if freq_b_0>3 and freq_b_1>3:
                    freq=bigrammi[n].count(bigramma)
                    C=len(tokens_POS[n])
                    V=len(set(tokens_POS[n]))
                    prob_cond=(freq+1)/(freq_b_0+V) #aggiunto add-one smoothing
                    LMI=freq*math.log(((freq+1)*(C+V))/((freq_b_0+1)*(freq_b_1+1)),2) #aggiunto add-one smoothing
                    coppie[bigramma]=(freq,round(prob_cond,5),round(LMI,2))
                    #elemento di "coppie" ha come struttura <bigramma>:(<frequenza>,<probabilità condizionata>,<LMI>)
        Stampa.append(coppie)
        
    #--------------------------------------------ordinamento dei bigrammi-----------------------------
    Ordinate=[] #lista che conterrà le tre liste dei primi 20 bigrammi ordinate per frequenza, prob. condizionata e LMI; ognuna di queste tre liste per ognuno dei due file
    for d in Stampa: #d è il dizionario delle distribuzioni di frequenza dei bigrammi
        FREQ=sorted(d.items(),key=lambda item:item[1][0], reverse=True)[:20] #primi venti bigrammi ordinati per frequenza
        PROB_COND=sorted(d.items(),key=lambda item:item[1][1], reverse=True)[:20]#primi venti bigrammi ordinati per prob. condizionata
        LMILIST=sorted(d.items(),key=lambda item:item[1][2], reverse=True)[:20]#primi venti bigrammi ordinati per LMI
        Ordinate+=[[FREQ]+[PROB_COND]+[LMILIST]] #"Ordinate" contiene due liste, ciascuna delle quali contiene [FREQ]+[PROB_COND]+[LMILIST] per ogni "d"
    fa=0 #indice della lista ordinata secondo frequenza assoluta in "Ordinate"
    pc=1 #indice della lista ordinata secondo la prob. condizionata in "Ordinate"
    lmi=2 #indice della lista ordinata secondo LMI in "Ordinate"
    for n in range(len(files)):
        print(nome_file(files[n], grassetto=True))
        #print("--------------------------------------------------------------------------------------------------------------------------")
        print(formato.format("Bigram", "Frequency","Bigram","ConditionalProb","Bigram", "LMI"))
        print(formato.format("--------------", "--------------","--------------","--------------","--------------", "--------------"))
        for i in range(20):
            #Ordinate[n][fa/pc/lmi][i] ha come struttura (((<token>,<POS>),(<token>,<POS>)),(<frequenza>,<prob. condizionata>,<LMI>))
            bigrammafa=Ordinate[n][fa][i][0][0][0]+" " + Ordinate[n][fa][i][0][1][0] 
            bigrammapc=Ordinate[n][pc][i][0][0][0]+ " " + Ordinate[n][pc][i][0][1][0]
            bigrammalmi=Ordinate[n][lmi][i][0][0][0]+ " " + Ordinate[n][lmi][i][0][1][0]
            print(formato.format(
                  bigrammafa,str(Ordinate[n][fa][i][1][fa])
                  ,bigrammapc,str(Ordinate[n][pc][i][1][pc])
                  ,bigrammalmi,str(Ordinate[n][lmi][i][1][lmi])))
        print()

def terzotask(files,tokens,POS, bigrammi, trigrammi):
    """Estrae le frasi con almeno 6 token e più 
    corte di 25 token, dove ogni token ricorre 
    almeno 2 volte nel corpus"""
    
    formato="|{:<165} |{:<10}|"
    for n in range(len(files)):
        print(nome_file(files[n], grassetto=True))
        #print("--------------------------------------------------------------------------------------------------------------------------")
        listatoken=[i[0] for i in POS[n]]
        listafrasi=[] #lista che conterrà le frasi selezionate e la frequenza media dei loro token
        for frase in tokens[n]:
            condition=True
            #--------condizione di frequenza dei token----------
            for token in frase:
                if listatoken.count(token)<2:
                    condition=False
            #----condizione di lunghezza della frase-------------
            if len(frase)<6 or len(frase)>24:
                condition=False
            #-----------ottenimento delle frasi selezionate---------
            if condition==True:
                somma_freq_token=0
                for token in frase:
                    somma_freq_token+=listatoken.count(token)
                media_freq_token=round(somma_freq_token/len(frase),2)
                frase_media_freq=(frase,media_freq_token)
                listafrasi.append(frase_media_freq)

        #-----------ordinamento delle frasi per frequenza media dei token decrescente-------------------
        print(formato.format("Sentence", "Mean Frequency"))
        print(formato.format("--------------", "--------------"))
        for frase in sorted(listafrasi,key=lambda item:item[1], reverse=True)[:5]:
            frase_str=""
            for token in frase[0]:
                frase_str+=str(token)+" "
            print(formato.format(frase_str,frase[1]))
        print()
        
        #-----------ordinamento delle frasi per frequenza media dei token crescente-------------------
        print(formato.format("Sentence", "Mean Frequency"))
        print(formato.format("--------------", "--------------"))
        for frase in sorted(listafrasi, key=lambda item: item[1], reverse=False)[:5]:
            frase_str = ""
            for token in frase[0]:
                frase_str += str(token) + " "
            print(formato.format(frase_str, frase[1]))
        print()

        #---------------calcolo della prob. di occorrenza delle frasi selezionate-------------------
        C=len(listatoken)
        listafrasi_new=[i[0] for i in listafrasi]
        listafrasi_ = [] #lista che conterrà le frasi selezionate e la loro prob. di occorrenza
        for frase in listafrasi_new:
            bi=list(nltk.bigrams(frase))
            tri=list(nltk.trigrams(frase))
            V=len(set(listatoken))
            prob1 = (listatoken.count(frase[0]) +1)/ (C + V)#aggiunto add-one smoothing
            prob2 = (bigrammi[n].count(bi[0])+1)/ (listatoken.count(frase[0])+V)#aggiunto add-one smoothing
            prob=prob1*prob2
            i=0
            while i <len(tri):
                freq_tri=trigrammi[n].count(tri[i])
                freq_bi=bigrammi[n].count(bi[i])
                prob=prob*((freq_tri+1)/(freq_bi+V))#aggiunto add-one smoothing
                i+=1
            frase_prob=(frase,prob)
            listafrasi_.append(frase_prob)
        
        print(formato.format("Sentence", "Probability"))
        print(formato.format("--------------", "--------------"))
        #--------------ordinamento delle frasi per probabilità------------
        for frase in sorted(listafrasi_, key=lambda item: item[1], reverse=True)[:5]:
            frase_str = ""
            for token in frase[0]:
                frase_str += str(token) + " "
            print(formato.format(frase_str, frase[1]))
        print()

def quartotask(files, NER):
    """Stampa i primi 15 nomi di persona più frequenti"""
    
    formato="|{:<20} |{:<20} |{:<20}| {:<20}|"
    PERSON=[] #lista che conterrà, per ogni file, la lista ordinata dei 15 nomi di persona più frequenti con relativa frequenza
    for n in range(len(files)):
        person_freq={person:NER[n].count(person) for person in set(NER[n])}
        PERSON.append(sorted(person_freq.items(), key=lambda item: item[1], reverse=True)[:15])
    print(formato.format(nome_file(files[0], grassetto=False), "", nome_file(files[1], grassetto=False), ""))
    print(formato.format("--------------", "--------------", "--------------", "--------------"))
    #print("--------------------------------------------------------------------------------------")
    print(formato.format("Person", "Frequency","Person", "Frequency"))
    
    for i in range(15):
        #PERSON[0/1][i] ha come struttura (<Persona>,<frequenza>)
        print(formato.format(PERSON[0][i][0], PERSON[0][i][1], PERSON[1][i][0], PERSON[1][i][1]))
    print()

def nome_file(file, grassetto=False):
    nome=file.replace(".txt","")
    if grassetto:
        nomefile="**" + nome+"**"
    else:
        nomefile=nome
    return nomefile

def main(file1, file2):
    fileInput1=open(file1, "r", encoding="utf-8")
    fileInput2=open(file2, "r", encoding="utf-8")
    raw1=fileInput1.read()
    raw2=fileInput2.read()
    sent_tokenizer=nltk.data.load("tokenizers/punkt/english.pickle")
    frasi1=sent_tokenizer.tokenize(raw1)
    frasi2=sent_tokenizer.tokenize(raw2)
    tokens1, token_POS1,NER_P1 = nlp(frasi1)
    tokens2, token_POS2,NER_P2 = nlp(frasi2)
    NER=[NER_P1,NER_P2]
    files=[file1,file2]
    tokens=[tokens1,tokens2]
    POS=[token_POS1,token_POS2]
    POS1_depunct,T1=removedpunctuation(POS[0], tokens[0])
    POS2_depunct,T2=removedpunctuation(POS[1], tokens[1])
    tokens_depunct=[T1,T2]
    POS_depunct=[POS1_depunct,POS2_depunct]
    bigrammi,trigrammi=bi_tri(files,POS_depunct)
    primotask(files,POS_depunct,bigrammi,trigrammi)
    secondotask(files,bigrammi,POS_depunct)
    terzotask(files,tokens_depunct,POS_depunct, bigrammi, trigrammi)
    quartotask(files, NER)

#main(sys.argv[1],sys.argv[2])

