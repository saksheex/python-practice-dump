Amount_Due = 50
Inserted_coin = 0

while Inserted_coin<50:

    print("Amount Due:",50-Inserted_coin)
    coin= int (input("Insert coin: "))

    if  coin not in [25,10,5]:
      continue
    else:
        coin in[25,10,5]
        Inserted_coin= Inserted_coin+coin

print("Change owed:", Inserted_coin-Amount_Due)
   