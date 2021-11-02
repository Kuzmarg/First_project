"""
Why are we still here? Just to suffer?
"""
import random
def generate_grid():
    """
    -> list
    Generates letters list
    """
    start_list='абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    res=[]
    i=0
    while i<5::
        random_letter=random.choice(start_list)
        if random_word not in res:
            res.append(random_letter)
            i+=1
    return res

def get_words(file1,letters):
    """
    str,list -> list
    Generates a list of tuples containing words and the part of speech
    """
    res=[]
    with open(file1, 'r', decoding='utf-8') as file:
        for line in file:
            line1=line.split()
            if line1[0][0] in letters and len(line1[0])<=5:
                if 'noun' in line or '/n' in line:
                    typo='noun'
                elif 'adv' in line or '/adv' in line:
                    typo='adverb'
                elif 'adj' in line or '/adj' in line:
                    typo='adjective'
                elif 'verb' in line or '/v' in line:
                    typo='verb'
                else:
                    typo='noun'
            res.append((line1[0],typo))
    return res

def get_user_words():
    """
    -> list
    Gets words input by user. Ctrl+d to finish
    """
    try:
        res=[]
        while True:
            res.append(input())
    except EOFError:
        return res

def check_user_words(user_words,language_part,letters,dict_of_words):
    """
    list,str,list,list -> tuple
    Returns two lists - one contains correct input words, the other - all
    the words which were not got from user, but are in the dictionary.
    """
    
