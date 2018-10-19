with open('write.txt','w') as write_file:
    write_file.write('hey there ninjas, python is awesome')

      
#junk

with open('write.txt', 'a') as write_file:
    write_file.write('\nI love it so much, i dream in python.')


quotes =[
    '\nI can resist eveything except temtation',
    '\nWe are all in the gutter, but some of us afre looking at the state',
    '\nAlways forgive your enemies - nothing annoys them so much'
] 

with open('write.txt','a') as write_file:
    write_file.writelines(quotes)