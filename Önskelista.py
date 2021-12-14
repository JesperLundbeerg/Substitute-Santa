# Jesper Lundberg
# 14/12-2021
# Önskelista

#def menu():
#    print("[1] Skapa önskelista")
#    print("[2] Läs upp önskelista")
#    print("[0] Stäng programmet")

#menu()
#option = int(input("Ange ditt val: "))

#while option != 0:
#    if option == 1:


def create_list(namn_på_lista):
    with open(namn_på_lista, "w", encoding="utf8") as x:
        namn = input("Vad heter barnet?: ")
        x.write(namn+"\n")

        while True:
            sak = input("Vad vill du lägga till i listan? Skriv # om du vill avbryta: ")
            if "#" in sak : break
            else: x.write(f"{sak}\n")

def import_list(öppna_lista):
    with open(öppna_lista, "r", encoding="utf8") as f:
        return [int(entry) for entry in f.readlines()]


def menu():
    filnamn = input("Vad heter filen?: ")
    create_list(filnamn)

def main():

    menu()

if __name__ == "__main__":
    main()