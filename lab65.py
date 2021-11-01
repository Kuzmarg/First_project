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


def get_words(f: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    res=[]
    with open(f, 'r') as file:
        for line in file:
            lst1=letters
            line=line.strip()
            bool1=True
            if lst1[4] not in line.lower():
                bool1=False
            for i in line:
                if i.lower() in lst1:
                    lst1.remove(i.lower())
                else:
                    bool1=False
            if bool1:
                res.append(line.lower())
            



def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    pass


def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    pass


def results():
    pass
