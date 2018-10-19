# def greet(name='jad',time='afternoon'):
#     # print(f'Good {time} {name}, hop you are well')
#     print('{0} {1},hop you are well'.format(name,time))

# # name = input('enter your name: ')
# # time = input('enter the time of day: ')

# greet('jad','afternoon')



def area(raduis):
    return (3.142 * raduis * raduis)

def vol(area,length):    
    print(area * length)

raduis = int(input('enter a raduis: '))
length = int(input('enter a length : '))


vol(area(raduis) ,length)   