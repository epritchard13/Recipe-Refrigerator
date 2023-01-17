from datetime import datetime
import uuid

contents = {}
recipes = {}
possibleMeals = {}
today = datetime.now()
EXPOKAYPREF = 86400


#keep track of what we got
with open("contents.txt", "r") as fp:
    for line in fp:
        line = line.split("\n")[0]
        name,quantity,exp = line.split(",")
        contents[name] = quantity,exp


#create recipes
with open("recipes.txt", "r") as fp:
    for line in fp:
        line = line.split("\n")[0]
        name,ingredients = line.split("->")
        recipes[name] = ingredients



print(contents)

canMake = False
for recipeName in recipes:
    print("trying to make: " + recipeName + "-----------")
    ingredients = recipes[recipeName]
    ingredients = ingredients.split(",")
    for ingredient in ingredients:
        ingredientName,needQuantity = ingredient.split(":")

        #checking things:
        if ingredientName in contents:
            #yuh we got it but has it expired yet?
            haveQuantity, exp = contents[ingredientName]
            exp = datetime.strptime(exp, "%m/%d/%Y %H:%M:%S")
            secondsTillExpired = (exp - today).total_seconds()
            foodGood = (EXPOKAYPREF + secondsTillExpired) > 0
            if not foodGood:
                #yes u nasty mf
                print("we have " + ingredientName + " but that shi gon bad")
                canMake = False
                break
            #food is good! we got enough???
            haveNum,haveType = haveQuantity.split(" ")
            needNum,needType = needQuantity.split(" ")
            if haveType != needType:
                print("Data Entry ERROR 0: unmatched type " + ingredientName)
                exit()
            if haveNum < needNum:
                print("we have " + ingredientName + " but insufficient quantity")
                canMake = False
                break
            
            print("we have " + ingredientName + "!")
            canMake = True
        else:
            #naw we aint got dat
            print("we dont have " + ingredientName)
            canMake = False
            break






        
    if canMake:      
        possibleMeals[recipeName] = "wecanmakeit"




print("\n")
print("possible meals: ")
print(possibleMeals)
