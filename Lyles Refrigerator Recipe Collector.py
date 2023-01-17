import praw


blwords = ["is", "I", "made", "This", "this","I'm", "a", "attempt","me","reposted"]
recipes = {}
upperToLower = {}
CHARTHRESH = 100


#Validate Reddit Access
reddit = praw.Reddit(client_id='c0S04PHZGgx7Wg',
                     client_secret='PEUlA0ILn5OS1YbuAkd1tVNFRI8',
                     password='11365abc',
                     user_agent='pix3lbot_scrape by /u/pix3lbot2',
                     username='pix3lbot2')
subreddit = reddit.subreddit('recipes')

with open("upperToLower.txt", "r") as fp:
    for line in fp:
        line = line.split("\n")[0]
        upper,lower = line.split(" ")
        upperToLower[upper] = lower




for submission in subreddit.top(limit=20):
    nameWords = submission.title.split(" ")
    notConsidering = False
    for blword in blwords:
        if blword in nameWords:
            notConsidering = True
    if not notConsidering:
        print("-----------------------------------")
        print("considering: " + submission.title)
        recipeComment = submission.comments[0].body
        newComment = ""
        charCounter = 0
        for character in recipeComment:
            charCounter = charCounter + 1
            if character in upperToLower:
                newComment = newComment + upperToLower[character]
            else:
                newComment = newComment + character
        recipeComment = ""
        for character in newComment:
            if character != "_":
                recipeComment = recipeComment + character
        itemizedComment = recipeComment.split("\n")
        itemCounter = 0
        #for comment in itemizedComment:
        #    if " i " not in comment:
        #        itemCounter = itemCounter + 1
        #if itemCounter > 0 and charCounter > CHARTHRESH:
        #    if "ingredients" in recipeComment:
        #        recipeComment = recipeComment.split("ingredients")
        #        recipeComment = recipeComment[1:len(recipeComment)]
        #        recipe = recipeComment[0]
        #        if(len(recipeComment) > 1):
        #            for section in recipeComment[1:len(recipeComment)]:
        #                recipe = recipe + "ingredients" + section
        #    if "instructions" in recipe:
        #        recipe = recipe.split("instructions")
        #        print(len(recipe))
        #        print("->->->")
        #        print("found instructions")
        #        print("<-<-<-")
        #    elif "method" in recipe:
        #        recipe = recipe.split("method")
        #        print(len(recipe))
        #        print("->->->")
        #        print("found method")
        #        print("<-<-<-")
        #    else:
        #        print("eliminated. improper format")
        #else:
        #    print("eliminated. not a recipe")
        
        
            




        
