word = input("Please enter a word: ")
start = 0
stop = len(word)

def tree(word, start, stop):
    word = (" " * (start - stop)) + word
    if start <= stop:
        start += 1
        print("{:>10}".format(word[0:start-1])) 
        return tree(word, start, stop)
    else:
        return ""


tree(word, start, stop) 
