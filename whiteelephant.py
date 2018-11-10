import random
import pickle
family_members = ['Mom', 'Dad', 'Nathan','Michelle','Chuck','Steph','Clint','Aaron','David','Joseph','Maggie','Mark','Sage','Sapphire']
dict = {}
stepone = [[i] for i in family_members]
def whiteelephant():
    random.shuffle(stepone) #shuffles the names in the list
    with open("output2", "wb") as fp:
        pickle.dump(stepone, fp)
if __name__ == '__main__':
    whiteelephant()
