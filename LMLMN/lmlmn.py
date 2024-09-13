print("Loves me, Loves me not by Bluexyon.")
print("----------------------------------------------")
petals = int(input("Please provide the amount of Petals: "))
def loves_me(amount):
    i = 0
    while i < amount:
        if i == amount-1:
            if i%2:
                print("LOVES ME NOT")
                i+=1
            else:
                print("LOVES ME")
                i+=1
        else:
            if i%2:
                print("Loves me not", end=", ")
                i+=1
            else:
                print("Loves me", end=", ")
                i+=11
loves_me(petals)