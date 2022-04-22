print("Python has three numeric types: int, float, and complex")
#Int
myValue=1
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))
#Float
myValue=3.14
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))
#Complex Data
myValue=5j
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))
#Boolean
myValue=True
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))
myValue=False
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))

#Lab Working with String
myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))
#String Concatenation
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)
Working with input strings
name = input("What is your name? ")
print(name)
Formatting output strings
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}!".format(name,color,animal))

#Lab Working with Lists, Tuples, and Dictionaries
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))
#Acessing by position
print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])
#Changing the values in a list
myFruitList[2] = "orange"
print(myFruitList)
#Introducing the tuple data type
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])
#Introducing the dictionary data type
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])
