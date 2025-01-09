#dictionaries are Key: Value Pairs
# It will print values for keys
#keys should be unique


dictionary = {
   "name": "siri",
   "age": 25,
   "subject": "Telugu",
   "is_clever": True,
   "grades_list": ['A','A-','A+','B+']
}

print(dictionary)

print(len(dictionary))

print (dictionary["name"])
#print(dictionary["gender"])       #error

print(dictionary.get("subject"))
print(dictionary.get("gender"))    #prints "None", no error

dictionary["gender"]= "female"  #new Key:Value Pair
print(dictionary["gender"])

dictionary["name"]="chinnu"   #reassigning new Value for Key "name"
print(dictionary["name"])   #prints new value i.e Chinnu not Siri
