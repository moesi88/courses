# def ninja_intro(dictionary):
#     for key,val in dictionary.items():
#         print ('i am {0} and i am a {1} belt'.format(key,val)



# ninja_belts={}

# while True:
#     ninja_name = input('enter a ninja name : ')
#     ninja_belts = input ('enter a belt colour: ')
#     ninja_belts[ninja_name] = ninja_belts 

#     another = input('add another ?(y\n)')
#     if another == 'y':
#         continue
#     else:
#         break 


# ninja_intro(ninja_belts)        

def belt_count(dictionary):
    belts = list(dictionary.values())
    for belt in set(belts):
        num = belts.count(belt)
        print(f'there are {num} {belt} belts') 

# def ninja_intro(dictionary):
#     for key, val in dictionary.items():
#         print(f'I am {key} and i am a {val} belt')

    
ninja_belts = {}


while True:
    ninja_name = input('enter a ninja name : ')
    ninja_belt = input('enter a belt colour : ')
    ninja_belts[ninja_name]= ninja_belt

    another = input('add another ? (y/n)')
    if another == 'y':
        continue
    else:
        break    



belt_count(ninja_belts)     