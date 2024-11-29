# Data una lista di stringhe (nomi), fornire in ingresso uno degli elementi
# quindi fornire in uscita quante volte si ripete l'elemento (SE ESISTE).
name_list = ["Marco", "Davide", "Franco", "Emma", "Franco", "Marco"]

print(name_list)
while True:
    try:
        name = input("Inserisci uno degli elementi: ")
    except ValueError as error:
        print(f"Valore inserito non conforme. [Tipo: STRING]")
        continue
    else:
        if name not in name_list:
            print(f"L'elemento inserito non esiste nella lista!")
            continue
        # Manderà in output il NOME inserito e IL NUMERO DELLE VOLTE che si ripete
        verifica = name_list.count(name)
        print(f"{name} è presente: {verifica} volte/a")
        break
        '''
        # Manderà in output ogni NOME e IL NUMERO DELLE VOLTE che si ripetono
        for index,element in enumerate(name_list):
            print(f"{element} , {name_list.count(name_list[index])}")
        break
        '''
    
    
