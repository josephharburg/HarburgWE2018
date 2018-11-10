import whiteelephant
import pickle
with open('output2', 'rb') as fp:
    names = pickle.load(fp)
membername = input('What is your name:')
if membername == "Mom":
    print("Your assigned person is", ''.join(names[0]))
elif membername == "Dad":
    print("Your assigned person is", ''.join(names[1]))
elif membername == "Nathan":
    print("Your assigned person is", ''.join(names[2]))
elif membername == "Michelle":
    print("Your assigned person is", ''.join(names[3]))
elif membername == "Chuck":
    print("Your assigned person is", ''.join(names[4]))
elif membername == "Steph":
    print("Your assigned person is", ''.join(names[5]))
elif membername == "Clint":
    print("Your assigned person is", ''.join(names[6]))
elif membername == "Aaron":
    print("Your assigned person is", ''.join(names[7]))
elif membername == "David":
    print("Your assigned person is", ''.join(names[8]))
elif membername == "Joseph":
    print("Your assigned person is", ''.join(names[9]))
elif membername == "Maggie":
    print("Your assigned person is", ''.join(names[10]))
elif membername == "Mark":
    print("Your assigned person is", ''.join(names[11]))
elif membername == "Sage":
    print("Your assigned person is", ''.join(names[12]))
elif membername == "Sapphire":
    print("Your assigned person is", ''.join(names[13]))
else:
    print("Please make sure you use your full first name and that the first letter is capitalized!")
