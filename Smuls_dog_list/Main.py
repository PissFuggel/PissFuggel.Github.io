import beans

loopig = True

Spitz_black = beans.Dog("Spitz", "Tiny", 10)
JackRusell_white = beans.Dog("Jack Russell", "Fat", 5)
Drever_brun = beans.Dog("Drever", "chonk", 12)
GoldenRetriever_Beige = beans.Dog("Golden Retriever", "Lagom", 1)
Dachshund_Black = beans.Dog("Dachshund", "Såssgage", 6)

Doglist = [Spitz_black,JackRusell_white,Drever_brun,GoldenRetriever_Beige,Dachshund_Black]

print("First dog = " + Doglist[0].Ras)


def loopDogs():
    i = 0

    for beans in Doglist:
        print(str(i+1) + " : "+ beans.Ras +" : "+ beans.Storlek + ", Antal färger: " + str(beans.Färg) + "st")
        i +=1

    dog_nr = input("\nMata in siffra för dog: ")
    dog_nr_int = int(dog_nr)

    #Färg_int = Doglist[dog_nr_int-1].get_Färg()
    #Färg_string = str(Färg_int)
    return dog_nr_int


def main():
    while loopig:
        print("--------------------")
        print("\n-:DogMachine:-\n")

        '''i = 0

        for beans in Doglist:
            print(str(i+1) + " : "+ beans.Ras +" : "+ beans.Storlek + ", Antal färger: " + str(beans.Färg) + "st")
            i +=1

        dog_nr = input("\nMata in siffra för dog: ")
        dog_nr_int = int(dog_nr)
        '''
        
        dog_nr_int =loopDogs()

        Färg_int = Doglist[dog_nr_int-1].get_Färg()
        Färg_string = str(Färg_int)
        
        if Färg_int > 0:
            print("\nEn " + Doglist[dog_nr_int-1].Ras + " " + Doglist[dog_nr_int-1].Storlek + "kommer här!\n")

            nytt_dogsaldo_int = Färg_int - 1
            nytt_dogsaldo_string = str(nytt_dogsaldo_int)
            Doglist[dog_nr_int-1].set_Färg(nytt_dogsaldo_int)

        else :
            print("\n Sorry, no more" + Doglist[dog_nr_int-1].Storlek + " " +Doglist[dog_nr_int-1].Ras + "\n")

            print("Dog saldo före: " + Färg_string + " st" )
            print("Dog saldo efter: " + nytt_dogsaldo_string + " st" )
            print("--------------------------------------------------------------\n")

            
        go = input("\n Vill du avsluta programmet? j/n ")
        print("\n")
            
        if (go == "j"):
            break


main()