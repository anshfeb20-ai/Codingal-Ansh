word=str(input("Enter a word: "))
character=str(input("Enter the character you want the program to find: "))

count=0
for i in range(len(word)):
    if word[i]==character:
        count+=1
        print("The character", character, "is found at index", i)