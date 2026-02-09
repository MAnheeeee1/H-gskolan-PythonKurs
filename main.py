namnLista = []
while True:
    print("1. Lägg till namn\n2. Visa alla nmn\n3. Avsluta")
    userChoice = input()
    if userChoice == "3":
        break
    elif userChoice == "1":
        nyNamn = input("Ange namnet du vill lägga till: ")
        namnLista.append(nyNamn)
    elif userChoice == "2":
        print(namnLista)
