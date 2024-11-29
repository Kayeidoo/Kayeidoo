# Media - Moda - Mediana manuale

numeri_list = [34, 67, 12, 45, 78, 23, 45, 56, 12, 89]
print(numeri_list)
# Media
'''
La media di una lista di numeri è semplicemente la somma di tutti gli elementi divisa per il numero totale di elementi. La formula è:
'''
media = sum(numeri_list)/len(numeri_list)



# Moda
'''
La moda è il numero che appare con maggiore frequenza nella lista. Se ci sono più numeri con la stessa frequenza, la lista ha più di una moda (è bimodale o multimodale). Se nessun numero si ripete, non c'è una moda. Nel nostro esempio:
'''
moda = []
frequenza_massima = 0

for element in numeri_list:
    # Conta quante volte 'element' appare nella lista
    num_ripetuto = numeri_list.count(element)
    # Se la frequenza è maggiore della frequenza massima
    if num_ripetuto > frequenza_massima:
        frequenza_massima = num_ripetuto
        moda = [element] 
    elif num_ripetuto == frequenza_massima:
        if element not in moda:  # Evitiamo duplicati
            moda.append(element)
    
    
    
# Mediana 
'''
La mediana è il numero che si trova al centro della lista quando gli elementi sono ordinati in ordine crescente (o decrescente). Se la lista ha un numero dispari di elementi, la mediana è il numero al centro. Se la lista ha un numero pari di elementi, la mediana è la media dei due numeri centrali.
'''
numeri_list.sort() 
i = int(len(numeri_list)/2) 
# print(i) - Per verificare 'i'
mediana = numeri_list[i]



# Output
print(f"Media: {media}, Moda: {moda}, Mediana: {mediana}")
