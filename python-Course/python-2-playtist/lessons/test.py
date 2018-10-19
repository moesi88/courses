from classes import Planet

planetX= Planet('planetX',300000,8,'X System')
print(f'Name : {planetX.name}')
print(f'Radius : {planetX.radius}')
print(f'Gravity : {planetX.gravity}')
print(planetX.orbit())
print(planetX.commons())
print(planetX.spin('a very high speed'))
