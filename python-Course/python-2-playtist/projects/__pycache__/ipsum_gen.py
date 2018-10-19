from random import randint


ninja_words=[
'Aiki','Buyu','Chimonjutsu','Cho sen','Dojo','Gakusei','Haibo',
'Jin','Kenshi','Obake ken','Rakusha','Sanmaru','Tekkon','Yoke'
]


def ninjarize(word):
    random_pos = randint(0, len(ninja_words) - 1)
    return f'{word} {ninja_words[random_pos]}'
    
paragraphs =int(input('How many paragraphs of ninja ipsum: '))


with open('ipsum.txt') as ipsum_origial:
    items = ipsum_origial.read().split() 

    for n in range(paragraphs):
        ninja_text=list(map(ninjarize,items))
        with open('ninja_ipsum.txt','a') as ipsum_ninja:
            ipsum_ninja.write(''.join(ninja_text) + '\n\n')