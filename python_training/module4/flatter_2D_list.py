'''Suppose I want to flatten a given 2D list and only include those '''
planets=[['Mercury','Venus','Earth'],
         ['Mars','Jupiter','Saturn'],
         ['Uranus','Neptune','Pluto']]
flatten_planets=[planets for sublist in planets for planets in sublist if len(planets)<6]
print(flatten_planets)