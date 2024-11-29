# Data una lista di 100 elementi di numeri casuali
# tra 1 a 5, calcolare le occorrenze per ogni
# singolo numero ripetuto

import random
grandezza_lista_massima = 100
numero_massimo = 5
num_list = [random.randint(1,numero_massimo) for _ in range(0,grandezza_lista_massima)]
print(f"Lista: {num_list}")

ripetuti_list = []

for index,element in enumerate(num_list):
    num_ripetuto = num_list.count(num_list[index])
    ripetuti_list.append(num_ripetuto)

print(f"Occorrenze: {ripetuti_list}")