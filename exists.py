list = ["one", "two", "three", "four", "five"]

def exists(word):
    if (word.lower().strip()) in list:
        print "IN LIST - " + word
    else:
        print "NOT IN LIST - " + word

exists("one")
exists("ONE")
exists("TWO ")
exists("FIVE")
exists("six")
