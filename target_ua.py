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
    