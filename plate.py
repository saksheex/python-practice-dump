

import string
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

     for c in s:
         if c in string.punctuation:
             return False
         if c == " ":
             return False
     if not 2<= len(s)<=6:
            return False
     if not s[0].isalpha() or not s[1].isalpha():
             return False
         
         
     number_started = False
     for c in s:
        if c.isdigit():
            if not number_started and c == "0":
              return False
            number_started = True
        elif c.isalpha():
            if number_started:
                return False

     return True   
main()
