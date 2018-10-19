from space.planet import Planet
from space.calc import planet_mass,planet_vol

maher = Planet('maher',200000,5.5,'Maher System')
# print(f'Name is :{maher.name}')
# print(f'Radius is : {maher.radius}')
# print(f'The gravity is {maher.gravity}')
# print(maher.orbit())
maher_mass = planet_mass(maher.gravity, maher.radius)
maher_vol = planet_vol(maher.radius)
 
print(f'{maher.name} has a mass of {maher_mass} and volume of {maher_vol} ')
# planetX= Planet('planetX',300000,8,'X System')
# print(f'Name : {planetX.name}')
# print(f'Radius : {planetX.radius}')
# print(f'Gravity : {planetX.gravity}')
# print(planetX.orbit())
# print(planetX.commons())
# print(planetX.spin('a very high speed'))