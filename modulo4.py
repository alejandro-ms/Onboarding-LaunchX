text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest d"""

# Divide el texto
text_parts = text.split('.')
print(text_parts)

# Palabras clave
keyWords = ['average', 'temperature', 'distance']
print(keyWords)


# Ciclo for para recorrer la cadena
for sentence in text_parts:
    for key_word in keyWords:
        if key_word in sentence:
            print(sentence)

# Ciclo para cambiar C a Celsius
for sentence in text_parts:
    for key_word in keyWords:
        if key_word in sentence:
            print(sentence.replace(' C', ' Celsius'))

# Datos con los que vas a trabajar
name = "Moon"
gravity = 0.00162  # in kms
planet = "Earth"

# Creamos el título
title = f'Gravity Facts about {name}'

# Creamos la plantilla
hechos = f"""{'-'*80} 
Planet Name: {name} 
Gravity on {name}: {gravity * 1000} m/s2 
"""
# Unión de ambas cadenas
template = f"""{title.title()} 
{hechos} 
"""
print(template)

nombre = 'Ganímedes'
gravity = 0.00143
planet = 'Marte '

new_template = """
Datos de Gravedad sobre: {nombre}
-------------------------------------------------------------------------------
Nombre del planeta: {planeta}
Gravedad en {nombre}: {gravedad} m/s2
"""
print(new_template.format(nombre=name, planeta=planet, gravedad=gravity))

# Pista: print(nueva_plantilla.format(variables))
print(new_template.format(nombre=name, planeta=planet, gravedad=gravity*1000))
