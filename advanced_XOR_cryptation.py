
#cryptation function
def data_sanitizer(func):
    #verify that func is str
    if type(func)==list:
        func="".join(func)
    
    #cryptation function
    def xor_cipher(txt,key):
        
        testo=list(txt)
        len_chiave=len(key)
        risultato=[]
        
        for i in range(len(txt)):
            #rotation of the key array
            chiave=key[i % len_chiave]
            
            
            #XOR cicle
            criz=testo[i]
            criz=ord(criz)
            criz=criz ^ ord(chiave)
            
            #add the value to risultato
            risultato.append(chr(criz))
            
        #convert risultato in str
        return "".join(risultato)
        
    return xor_cipher
    
    
    
@data_sanitizer
def stringario(stringa,key):
    return str(stringa)
    
    
    
    
    
    
    
#cripted test    
x="""Tradizionalmente datata al 750 a.C. circa[3], Cicerone afferma nel suo De oratore che Pisistrato ne abbia disposto la sistemazione in forma scritta nel VI secolo a.C.,



ma si tratta di questione discussa dalla critica.[4] In epoca ellenistica fu codificata da filologi alessandrini guidati da Zenodoto nella prima edizione critica, comprendente 15.696 versi divisi in 24 libri (ciascuno corrispondente a un rotolo, che ne dettava la lunghezza).[5] Ai tempi il testo era infatti estremamente oscillante, visto che la precedente tradizione orale aveva originariamente numerose varianti. Ciascun libro è contraddistinto da una lettera maiuscola dell'alfabeto greco e riporta in testa un sommario del contenuto.

Nell’Iliade, la guerra di Troia è dominata da eroi leggendari. Achille, il più grande dei guerrieri greci, si ritira dalla battaglia dopo un litigio con Agamennone, capo dell’esercito greco. Menelao, re di Sparta, lotta per riottenere sua moglie Elena, rapita da Paride, principe troiano. I Greci sono guidati anche da Ulisse, astuto re di Itaca, e Aiace, un guerriero possente.[6]

I Troiani sono guidati da Ettore, il più valoroso tra loro, mentre Priamo, re di Troia, cerca di proteggere la sua città. La morte di Patroclo, amico di Achille, spinge quest’ultimo a tornare in battaglia, uccidendo Ettore. Tra onore e vendetta, gli eroi affrontano il loro destino, intrecciando gloria e dolore.
"""


#cryptation key
k="""Il nome dei cazzilli deriva indiscutibilmente dalla forma: il chiamarli crocchette potrebbe addirittura offendere i palermitani, ma per far capire di che si tratta anche a chi non è nativo della Sicilia possiamo usare questa definizione; o forse meglio crocchè, che è la parola usata al sud per intendere le polpettine fritte il cui impasto è a base di patate.
I cazzilli palermitani sono una pietanza gustosa e semplice. Nel pieno rispetto della tradizione culinaria palermitana, sono associati alle più antiche panelle, tipiche frittelle schiacciate a base di farina di ceci. Il nome, dunque, perché dalla forma tondeggiante e allungata e più o meno delle dimensioni di un dito medio.

Cazzilli e panelle
Un tempo preparati nelle friggitorie e dai panellari ambulanti, sono oggi fritti e venduti in più moderne Ape car, adattate per la preparazione di questi sfiziosi cibi.

La preparazione di una tale prelibatezza della tradizione gastronomica popolare siciliana sembra quanto mai semplice. Le varianti sono minime, ma l’ingrediente di base, le patate, fa la differenza. Si debbono usare patate farinose e non troppo fresche, che non assorbano troppa acqua in cottura. Un trucco è lasciar “invecchiare” un paio di settimane delle patate a pasta gialla.

Preparazione
Dopo averle fatte bollire in acqua salata con tutta la buccia si debbono lasciar raffreddare e meglio ancora riposare, anche per una giornata. Le patate vengono poi passate per ottenerne una purea fine ed omogenea, si aggiustano di sale e di pepe, si insaporiscono con un battuto fine di prezzemolo e, piacendo, un pizzico di mentuccia fresca tritata. A questo punto l’impasto per i cazzilli è pronto per dargli la forma: ci si ungono leggermente le mani con dell’olio di oliva e si procede. È consigliato da chi se ne intende lasciar riposare in frigo i cazzilli per un paio d’ore, prima di passare alla frittura.

I cazzilli vanno dunque fritti, pochi alla volta perché non si attacchino tra loro, in abbondante olio bollente (di semi per un sapore più delicato) a 180/190 °C, fino a che assumono un aspetto dorato e una crosticina croccante. Si fanno poi asciugare dall’olio in eccesso su della carta da cucina.

Un consiglio per chi si cimentasse per la prima volta con la ricetta dei cazzilli, è di friggerne un paio prima di procedere alla formatura di tutto l’impasto: potreste scoprire che i cazzilli si disfano nell’olio o ne assorbono troppo; generalmente dipende dalla qualità delle patate, fattore su cui gli esperti palermitani non sbaglierebbero mai! In tal caso, per ovviare, potete aggiungere un pochino di farina all’impasto o appena un pizzico di fecola di patate, anche se questo non è previsto nella ricetta tradizionale dei cazzilli.

Una spruzzata di limone o ulteriore pepe sui cazzilli fritti è facoltativa.

Un modo per gustare i cazzilli, oltre che mangiarli così come sono, magari nel “cuoppo” di carta, è usarli per farcire dei panini morbidi; tradizionalmente le cosiddette Mafalde siciliane, di grano duro, dall’impasto arricchito di olio e miele e dalla caratteristica forma a serpentina, ricoperte di semi di sesamo."""




#print txt
print(stringario(x,k))