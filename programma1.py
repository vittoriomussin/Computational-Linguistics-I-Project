# Vittorio Mussin v.mussin@studenti.unipi.it 3319473310
import sys
import nltk
import string

def nlp(frasi):
    """Restituisce l'insieme dei token 
    e delle coppie token-POS"""
    
    tokens=[]
    POS=[]
    for frase in frasi:
        token=nltk.word_tokenize(frase)
        pos=nltk.pos_tag(token)
        tokens.append(token)
        POS+=pos
    return tokens, POS



def primotask(files,tokens,POS):
    """Stampa il numero di frasi e il 
    numero di token"""
    
    formato="|{:<20} |{:<20} |{:<20}|"
    print(formato.format("", nome_file(files[0], grassetto=False), nome_file(files[1], grassetto=False)))
    print(formato.format("---------------", "---------------", "---------------"))
    print(formato.format("Sentences:", len(tokens[0]), len(tokens[1])))
    print(formato.format("Tokens:", len(POS[0]), len(POS[1])))
    print()

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
            if not POS[i][1] in p and not POS[i][0]in "``":
                P.append(POS[i][0])
                F.append(frase[ifrase])
            ifrase+=1
            i+=1
        T.append(F)
            
    return P,T

def secondotask(files,tokens, POS):
    """Stampa la lunghezza media delle frasi 
    in termini di token e dei token (escludendo 
    la punteggiatura) in termini di caratteri"""

    formato = "|{:<30} |{:<20} |{:<20}|"
    Mfrasi=[]#lista che conterrà le medie della lunghezza delle frasi per il primo file e per il secondo
    Mtokens=[]#lista che conterrà le medie della lunghezza delle parole per il primo file e per il secondo
    for n in range(len(files)):
        P,T=removedpunctuation(POS[n],tokens[n])
        sumtoken=0
        sumfrasi=0
        for token in P:
            sumtoken+=len(token)
        for frase in T:
            sumfrasi+=len(frase)
        meanlfrasi=sumfrasi/len(T)
        meanltokens=sumtoken/len(P)
        Mfrasi.append(round(meanlfrasi,2))
        Mtokens.append(round(meanltokens,2))
        #la media è stata arrotondata
        #in entrambi i casi alle prime due cifre decimali
    print(formato.format("",nome_file(files[0], grassetto=False),nome_file(files[1], grassetto=False)))
    print(formato.format("---------------", "---------------", "---------------"))
    print(formato.format("Mean sentence lenght:", Mfrasi[0], Mfrasi[1]))
    print(formato.format("Mean token lenght:", Mtokens[0], Mtokens[1]))
    print()

def terzotask(files, POS):
    """Stampa il numero di hapax sui primi 1000 token"""
    H=[]#lista che conterrà il numero di hapax sui primi 1000 token  per il primo file e per il secondo
    formato = "|{:<40}| {:<20} |{:<20}|"
    for i in range(len(files)):
        mille=[]#lista che conterrà i primi 1000 token
        for t in POS[i][:1000]:
            mille.append(t[0])#t[0] è il token nella coppia (<token>,<POS>)
        n=[mille.count(i) for i in set(mille)]#frequenze dei tipi di token per i primi 1000 token
        h=0#h è un contatore per la frequenza degli hapax
        for i in n:
            if i ==1:
                h+=1
        H.append(h)
    print(formato.format("", nome_file(files[0], grassetto=False),nome_file(files[1], grassetto=False)))
    print(formato.format("---------------", "---------------", "---------------"))
    print(formato.format("Hapax in the firsts 1000 tokens:", H[0], H[1]))
    print()


def quartotask(file, POS):
    """Stampa la grandezza del vocabolario e 
    la Type Token Ratio per porzioni incrementali 
    di 500 token"""
    c=500#contatore delle "porzioni di token"
    C=len(POS)
    formato = "|{:<15}| {:<15} |{:<15}|"
    print(nome_file(file, grassetto=True))
    print(formato.format("Tokens:","Dictionary (unique words) size:","TypeTokenRatio:"))
    print(formato.format("---------------", "---------------", "---------------"))
    while c < C:
        v= len(set(POS[:c]))#grandezza del vocaboliario per i primi "c" token
        print(formato.format(c,v,round(v/c,2)))#la TTR è stata approssimata alle prime 2 cifre decimali
        c+=500
    print()


def quintotask(files,POS):
    """Stampa la distribuzione in termini 
    di percecntuale dell'insieme delle 
    parole piene e delle parole funzionali """
    PIENE=[]#lista che conterrà le percentuali delle parole piene per i due file
    VUOTE=[]#lista che conterrà le percentuali delle parole vuote per i due file
    for n in range(len(files)):
        listapos=[i[1]for i in POS[n]]
        D={i:listapos.count(i)for i in set(listapos)}#distribuzione di frequenza delle POS
        #aggettivi, sostantivi, verbi, avverbi
        Piene="JJ JJR JJS NN NNS NNP NNPS RB RBR RP WRB VB VBD VBG VBN VBP VBZ MD"
        #articoli, preposizioni, congiunzioni, pronomi
        Vuote="CC DT EX IN PDT POS PRP PRP$ TO WDT WP WP$"
        p=0#contatore delle parole piene
        v=0#contatore delle parole vuote
        for i in D:
            if i in Piene:
                p+=D[i]
            if i in Vuote:
                v+=D[i]
        PIENE.append(str(round(p/len(POS[n])*100,2)) + "%\t")
        VUOTE.append(str(round(v/len(POS[n])*100,2)) + "%\t")
    formato = "|{:<30} |{:<20} |{:<20}|"
    print(formato.format("",nome_file(files[0], grassetto=False),nome_file(files[1], grassetto=False)))
    print(formato.format("---------------", "---------------", "---------------"))
    print(formato.format("Lexical words:", PIENE[0], PIENE[1]))
    print(formato.format("Functional words:", VUOTE[0], VUOTE[1]))
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
    tokens1, token_POS1 = nlp(frasi1)
    tokens2, token_POS2 = nlp(frasi2)
    files=[file1,file2]
    tokens=[tokens1,tokens2]
    POS=[token_POS1,token_POS2]
    primotask(files,tokens, POS)
    secondotask(files,tokens, POS)
    terzotask(files,POS)
    for n in range(len(files)):
        quartotask(files[n],POS[n])
    quintotask(files,POS)

#main(sys.argv[1],sys.argv[2])
