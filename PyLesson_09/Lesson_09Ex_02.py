words = ("ello", "My", "Name", "Is", "Bob")

def first():
    global words
    for word in words:
        print(word[0])

first()
