import random

def calcular_distancia(x1,y1,x2,y2):
    return ((x2-x1)**2+(y2-y1)**2)**(1/2)

def generar_ciudades(num_ciudades):
    return [{'nombre': 'Ciudad '+ str(i), 'demanda': random.randint(100,1000), 'x':random.randint(0,101), 'y': random.randint(0,100), 'energia_recibida': 0 } for i in  range (num_ciudades)]

def generar_fuentes(num_fuentes):
    return [{'nombre': 'Fuente '+ str(i), 'capacidad': random.randint(100,1000), 'x':random.randint(0,101), 'y': random.randint(0,100), 'energia_asignada': 0 } for i in  range (num_fuentes)]

def encontrar_fuente_cercana(ciudad,fuentes):
    return sorted([(fuentes[i],calcular_distancia(fuentes[i]['x'],fuentes[i]['y'],ciudad['x'],ciudad['y'])) for i in range(len(fuentes))], key = lambda x: x[1])

def actualizar_demanda(ciudades):
    for c in ciudades:
        c['demanda'] *=random.uniform(0.9,1.2)
        c['energia_recibida']=0

def asignar_energia(ciudades,fuentes):
    lista = [{'ciudad': c['nombre'], 'fuente': encontrar_fuente_cercana(c, fuentes)[0][0]['nombre'], 'energia': c['demanda']} for c in ciudades]
    for l in lista:
        
        for c in ciudades:
            if l['ciudad']==c['nombre']:
                c['energia_recibida']+= l['energia']

        for f in fuentes:
             if l['fuente']==f['nombre']:
                 f['energia_asignada']+= l['energia']

    return lista

def graficar(ciudades,fuentes,asignaciones):
    pass

ciudades = generar_ciudades(2)
fuentes = generar_fuentes(2)

print(ciudades)
print('\n',fuentes)

for i in range (len(ciudades)):
    print('\n',encontrar_fuente_cercana(ciudades[i],fuentes))

#actualizar_demanda(ciudades)
#print('\n',ciudades)

print('\n',asignar_energia(ciudades,fuentes))

print('\n',ciudades)
print('\n',fuentes)

