word1 = input("Please enter a word: ")
word2 = input("Please enter another word: ")
word3 = input("Please enter another word: ")

def makeCenter(word):
    if len(word) >= 20:
        return word
    else:
        word = " " + word + " "
        return makeCenter(word)  
        
        
print(makeCenter(word1))         
print(makeCenter(word2))
print(makeCenter(word3))  
