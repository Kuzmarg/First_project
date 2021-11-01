"""
My lab file
"""
from typing import List
import random
import string

def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    return [[random.choice(string.ascii_uppercase) for i in range(3)]for j in range(3)]

def get_words(file1: str, letters: List[str]) -> List[str]:
    """
    Reads the file file1. Checks the words with rules and returns a list of words.
    """
    res=[]
    with open(file1, 'r', encoding='utf-8') as file:
        file.readline()
        file.readline()
        file.readline()
        for line in file:
            lst1=letters+[]
            line=line.strip()
            bool1=True
            if lst1[4] not in line.lower():
                bool1=False
            for i in line:
                if i.lower() in lst1:
                    lst1.remove(i.lower())
                else:
                    bool1=False
            if bool1 and len(line)>=4:
                res.append(line.lower())
    return res

def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    try:
        res=[]
        while True:
            res.append(input())
    except EOFError:
        return res

def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]):
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    res=[]
    for i in user_words:
        lst1=letters+[]
        bool1=True
        if letters[4] not in i:
            bool1=False
        for j in i:
            if j in lst1:
                lst1.remove(j)
            else:
                bool1=False
        if bool1:
            res.append(i)
    del_ls=[]
    for j in res:
        if j in words_from_dict:
            del_ls.append(j)
    for j in del_ls:
        res.remove(j)
    return res

def results():
    """
    Returns result
    """
    grid1=generate_grid()
    print(grid1)
    grid1=grid1[0]+grid1[1]+grid1[2]
    grid1=[i.lower() for i in grid1]
    got_words=get_user_words()
    num=0
    for i in got_words:
        if i in get_words('en',grid1):
            num+=1
    print(num)
    for i in get_words('en',grid1):
        if i not in got_words:
            print(i)
    print(get_pure_user_words(got_words,grid1,get_words('en',grid1)))

print(get_words('en.txt', [el for el in 'gniarnoah']))
print(get_pure_user_words(get_user_words(), [el for el in 'gniarnoah'], get_words('en.txt', [el for el in 'gniarnoah'])))
