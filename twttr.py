

user = input("Input: ")
vowels = ["a","e","i","o","u"]
for l in vowels: 
   user =  user.replace(l,"")
   user =  user.replace(l.upper(),"")
print("Output:",user) 