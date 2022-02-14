# We create the planets list and show it
planets = ['Mercury', 'Venus', 'Earth', 'Mars',
           'Jupiter', 'Saturn', 'Uranus', 'Neptune']

print(planets)

# Added pluton and show last element
planets.append('Pluton')
print("Numbers of planets are: ", len(planets))
print(planets[-1])

# Lista de planetas
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']
userPlanet = input("Please enter the name of the planet ").capitalize()
print(userPlanet)
planets.append(userPlanet)
# Busca el planeta en la lista
planet_index = planets.index(userPlanet)

# Muestra los planetas más cercanos al sol
print('Here are the planets closer than ' + userPlanet)
print(planets[0:planet_index])

print('Here are the planets further than ' + userPlanet)
print(planets[planet_index + 1:])
