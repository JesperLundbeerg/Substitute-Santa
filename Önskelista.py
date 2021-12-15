# Jesper Lundberg
# 14/12-2021
# Önskelista

def create_list(namn_på_lista):
    with open(namn_på_lista, "w", encoding="utf8") as x:
        namn = input("Vad heter barnet?: ")
        x.write(namn+"\n")

        while True:
            sak = input("Vad vill du lägga till i önskelistan? Skriv # när du är klar: ")
            if "#" in sak : break
            else: x.write(f"{sak}\n")

def import_list(öppna_lista):
    with open(öppna_lista, "r", encoding="utf8") as f:
        return [int(entry) for entry in f.readlines()]


def menu():
    filnamn = input("Vad vill du döpa filen till?: ")
    create_list(filnamn)
    openfile = input("Vilken önskelista vill du öppna?: ")
    open_file(openfile)

def open_file(öppna_fil):
    with open(öppna_fil, "r", encoding="utf8") as f:
        filestream = f.readlines()
        for line in filestream:
            print(line, end="")

def main():

    menu()

if __name__ == "__main__":
    main()