numbers= {"1":"one", 
          "2":"two",
         "3": "three",
         "4": "four",
         "5": "five",
         "6": "six",
         "7": "seven",
         "8": "eight",
         "9": "nine",
         "0": "zero" }


phone= input("enter phone number: ") #1234
output=""

for character in phone:
   output += numbers.get(character) + " "
   
print(output)