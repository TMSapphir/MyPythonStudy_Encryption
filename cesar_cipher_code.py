
def cripto1(func):
	def wrapper(txt):
		if type(txt)==list:
			txt="".join(txt)

		testo=list(func(txt))
		alfabeto= list("abcdefghijklmnopqrstuvwxyz1234567890")
		risultato=[]
		for i in range(len(testo)):
			lower=testo[i].casefold()
			if lower in alfabeto:
				pos=alfabeto.index(lower)
				calc=(pos*8 + 3 + 5*6) % 36
				sost=alfabeto[calc]
				if testo[i].isupper():
					risultato.append(sost.upper())
				else:
					risultato.append(sost)
				
			else:
				risultato.append(testo[i])

		return "".join(risultato)
	return wrapper



#the code has a crittography key (calc=(pos*8 + 3 + 5*6) % 36) with a 2 iterations cicle. one criptation is equal for any even repetition, one is equal for every odd repetition


#EVEN SET: [cripted_letter] = [cript1] for all num_iteration = 2n with n in N
#ODD SET:  [cripted_letter] = [cript2] for all num_iteration = 2n+1 with n in N


@cripto1 #1 ODD SET
@cripto1 #2 EVEN SET
@cripto1 #3 ODD SET
@cripto1 #4 EVEN SET
@cripto1 #5 ODD SET
def criptazione(a):
	return str(a)
    
    
# i know that programmers like to count from 0, but in my home we count from 1. (sorry)
    
    
x="""Tradizionalmente datata al 750 a.C. circa[3], Cicerone afferma nel suo De oratore che Pisistrato ne abbia disposto la sistemazione in forma scritta nel VI secolo a.C.,



ma si tratta di questione discussa dalla critica.[4] In epoca ellenistica fu codificata da filologi alessandrini guidati da Zenodoto nella prima edizione critica, comprendente 15.696 versi divisi in 24 libri (ciascuno corrispondente a un rotolo, che ne dettava la lunghezza).[5] Ai tempi il testo era infatti estremamente oscillante, visto che la precedente tradizione orale aveva originariamente numerose varianti. Ciascun libro è contraddistinto da una lettera maiuscola dell'alfabeto greco e riporta in testa un sommario del contenuto.

Nell’Iliade, la guerra di Troia è dominata da eroi leggendari. Achille, il più grande dei guerrieri greci, si ritira dalla battaglia dopo un litigio con Agamennone, capo dell’esercito greco. Menelao, re di Sparta, lotta per riottenere sua moglie Elena, rapita da Paride, principe troiano. I Greci sono guidati anche da Ulisse, astuto re di Itaca, e Aiace, un guerriero possente.[6]

I Troiani sono guidati da Ettore, il più valoroso tra loro, mentre Priamo, re di Troia, cerca di proteggere la sua città. La morte di Patroclo, amico di Achille, spinge quest’ultimo a tornare in battaglia, uccidendo Ettore. Tra onore e vendetta, gli eroi affrontano il loro destino, intrecciando gloria e dolore."""


print(criptazione(x))