grocery={}
while True:
    try:
        grocery_items = input().lower()
        grocery[grocery_items]= grocery.get(grocery_items,0)+1

    except EOFError:
     break
for item in sorted(grocery):
    print(grocery[item], item.upper())