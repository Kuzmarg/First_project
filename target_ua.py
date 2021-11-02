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
    while i<5:
        random_letter=random.choice(start_list)
        if random_letter not in res:
            res.append(random_letter)
            i+=1
    return res

def get_words(file1,letters):
    """
    str,list -> list
    Generates a list of tuples containing words and the part of speech
    >>> get_words('base.lst',['щ'])
    [('щасні', 'noun'), ('щасно', 'adverb'), ('щастя', 'nou\
n'), ('ще', 'adverb'), ('щебет', 'noun'), ('щем', 'noun'), ('щем\
но', 'adverb'), ('щеня', 'noun'), ('щепа', 'noun'), ('щерба', 'n\
oun'), ('щигля', 'noun'), ('щипак', 'noun'), ('щипок', 'noun'), (\
'щипці', 'noun'), ('щир', 'noun'), ('щирий', 'adjective'), ('щит'\
, 'noun'), ('щиток', 'noun'), ('щі', 'noun'), ('щіпка', 'noun'), (\
'щітка', 'noun'), ('щіть', 'noun'), ('щічка', 'noun'), ('щогла', '\
noun'), ('щодва', 'adverb'), ('щодві', 'adverb'), ('щодня', 'adve\
rb'), ('щока', 'noun'), ('щоніч', 'adverb'), ('щораз', 'adverb'), ('\
щорік', 'adverb'), ('щотри', 'adverb'), ('щука', 'noun'), ('щуп', '\
noun'), ('щупак', 'noun'), ('щупик', 'noun'), ('щупля', 'noun'), ('\
щур', 'noun'), ('щурик', 'noun'), ('щурка', 'noun'), ('щуря', 'nou\
n'), ('щучий', 'adjective'), ('щучин', 'adjective'), ('щучка', 'noun')]
    """
    res=[]
    with open(file1, 'r', encoding='utf-8') as file:
        for line in file:
            line1=line.split()
            if line1[0][0] in letters and len(line1[0])<=5:
                if ('adj' in line or '/adj' in line) and '/n' not in line:
                    typo='adjective'
                elif 'adverb' in line or '/adv' in line:
                    typo='adverb'
                elif 'noun' in line or '/n' in line:
                    typo='noun'
                elif 'verb' in line or '/v' in line:
                    typo='verb'
                elif 'adv' in line:
                    typo='adverb'
                else:
                    typo=''
                # if line1[0]=='щасні':
                #     print(line)
                if typo!='':
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
    correct_words=[]
    forg_words=[]
    for i in dict_of_words:
        if i[0] in user_words and i[1]==language_part and i[0][0] in letters:
            correct_words.append(i[0])
            user_words.remove(i[0])
    for j in dict_of_words:
        if j[0] not in correct_words and j[1]==language_part:
            forg_words.append(j[0])
    return correct_words,forg_words

def game():
    """Contains the game"""
    grid1=generate_grid()
    dict_words=get_words('base.lst',grid1)
    print(grid1)
    part_lang=random.choice(['noun','adverb','verb','adjective'])
    print(part_lang)
    print('Input words:')
    res=check_user_words(get_user_words(),part_lang,grid1,dict_words)
    print('Correct words:')
    print(res[0])
    print("Words that you didn't mention:")
    print(res[1])

if __name__=='__main__':
    # # print(check_user_words([], "adverb", ['ш', 'ь', 'т', 'і', 'х'],
    # # get_words("base.lst", ['ш', 'ь', 'т', 'і', 'х'])))
    a=
    print(get_words("base.lst", ['щ']))
    import doctest
    doctest.testmod()
