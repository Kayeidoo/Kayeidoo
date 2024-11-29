# Media. moda e Mediana con modulo: STATISTICS
import statistics

numeri_list = [34, 67, 12, 45, 78, 23, 45, 56, 12, 89]
print(numeri_list)

media = statistics.mean(numeri_list)

moda = statistics.mode(numeri_list)

mediana = statistics.median(numeri_list)
print(f"Media: {media}, Moda: {moda}, Mediana: {mediana}")