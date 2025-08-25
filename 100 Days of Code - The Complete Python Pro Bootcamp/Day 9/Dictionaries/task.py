programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."}

#accessing the dictionary thr its key

print(programming_dictionary["Function"])
programming_dictionary["Loop"] = "The repetitive action"
print(programming_dictionary)

#Wipe the dictionary

programming_dictionary = {}

#edit the item
programming_dictionary["Bug"] = "The small insect"
print(programming_dictionary)

#Loop thr dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

