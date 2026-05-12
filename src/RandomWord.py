import random
ps = random.randint(0,16)
rs = random.randint(0,18)
ss = random.randint(0,14)
prefixes = ["Anti", "De", "Dis", "En","Fore", "In", "Inter", "Mid", "Mis", "non", "over", "pre", "semi", "sub", "super", "trans", "un"]
root = ["ambi", "aqua", "aud", "anthropo", "auto", "bio", "cent", "circum", "contra", "dict", "fac", "chron", "dyna", "dys", "gram", "graph", "hetero", "homo", "hydr"]
suffixes = ["able", "al", "ed", "en", "er", "est", "ful", "ic", "ing","tion", "ity", "less", "ness", "ous", "y"]
preDef = ["being against ", "opposite of ", "not ", "the cause to ", "in front of ","in ", "between ", "middle of ", "wongly", "not", "too much or over ", "before ", "partial ", "under ", "above and beyond ", "across ", "the opposite of " ]
rootDef = ["both ", "water ", "hearing ", "being human ", "self ", "life ", "one hundred ", "around ", "against ", "saying things ", "to do or to make ", "time ", "power ", "being bad, hard or unlucky ", "a thing being written ", "writing ", "being different ", "beign the same ", "water "]
suffDef = ["Can be, or the ability of ", "Having characteristics of ", "Already ", "Made of ", "One who, or a person connected with ", "The most ", "Full of ", "Having characteristics of ", "What is happening now:", "Act or process of ", "State of ", "Without ", "Condition of ", "Having qualities of", "Characterized by"]
response1 = input("If you would like to make a random word type yes: ")
if response1 == "yes":
    ps = random.randint(0, len(prefixes)-1)
    rs = random.randint(0, len(root)-1)
    ss = random.randint(0, len(suffixes)-1)
    print(prefixes[ps] + root[rs] + suffixes[ss])
    print("The definitions are as follows:")
    print(suffDef[ss] + preDef[ps] + rootDef[rs])
