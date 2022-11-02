from mi_grafo import Grafo

grafo1 = Grafo(dirigido=False)

lista1=[['La Gran Muralla China', 'China', 'Arquitectonica'],
        ['Petra', 'jordania', 'Arquitectonica'],
        ['El Coliseo', 'Italia', 'Arquitectonica'],
        ['Chichen Itza', 'Mexico', 'Arquitectonica'],
        ['Taj Mahal', 'India', 'Arquitectonica'],
        ['Machu Picchu', 'Peru', 'Arquitectonica'],
        ['Cristo Redentor', 'Brasil', 'Arquitectonica'],
        ['Baia de Ha Long', 'Vietnam', 'Natural'],
        ['Isla de Comodo', 'Indonesia', 'Natural'],
        ['Rio Subterraneo de Puerto Princesa', 'Filipinas', 'Natural'],
        ['Cataratas del Iguazu', 'Brasil-Argentina', 'Natural'],
        ['Selva Amazonica', 'Brasil-Ecuador-Peru-Bolibia-Colombia-Guayana Francesa-Venezuela-Surinam', 'Natural'],
        ['Montaña de la mesa', 'Sudafrica', 'Natural'],
        ['Isla Jeju', 'Corea del Sur', 'Natural']
]
for nombre, pais, tipo in lista1:
    datos = {'pais': pais,
             'tipo': tipo}
    grafo1.insertar_vertice(nombre, datos)


grafo1.insertar_arista('La Gran Muralla China', 'Petra', 6217)
grafo1.insertar_arista('La Gran Muralla China', 'El Coliseo', 9663)
grafo1.insertar_arista('La Gran Muralla China', 'Chichen Itza', 12953)
grafo1.insertar_arista('La Gran Muralla China', 'Taj Mahal', 2909)
grafo1.insertar_arista('La Gran Muralla China', 'Machu Picchu', 17662)
grafo1.insertar_arista('La Gran Muralla China', 'Cristo Redentor', 18713)
grafo1.insertar_arista('Petra', 'El coliseo', 4187)
grafo1.insertar_arista('Petra', 'Chichen Itza', 12548)
grafo1.insertar_arista('Petra', 'Taj Mahal', 4396)
grafo1.insertar_arista('Petra', 'Machu Picchu', 12547)
grafo1.insertar_arista('Petra', 'Cristo Redentor', 10629)
grafo1.insertar_arista('El Coliseo', 'Chichen Itza', 10141)
grafo1.insertar_arista('El Coliseo', 'Taj Mahal', 6565)
grafo1.insertar_arista('El Coliseo', 'Machu Picchu', 12547)
grafo1.insertar_arista('El Coliseo', 'Cristo Redentor', 9064)
grafo1.insertar_arista('Chichen Itza', 'Taj Mahal', 15094)
grafo1.insertar_arista('Chichen Itza', 'Machu Picchu', 4717)
grafo1.insertar_arista('Chichen Itza', 'Cristo Redentor', 6924)
grafo1.insertar_arista('Taj Mahal', 'Machu Picchu', 16941)
grafo1.insertar_arista('Taj Mahal', 'Cristo Redentor', 14766)
grafo1.insertar_arista('Machu Picchu', 'Cristo Redentor', 2573)
grafo1.insertar_arista('Baia de Ha Long', 'Isla de Comodo', 5521)
grafo1.insertar_arista('Baia de Ha Long', 'Rio Subterraneo de Puerto Princesa', 1464)
grafo1.insertar_arista('Baia de Ha Long', 'Cataratas del Iguazu', 17785)
grafo1.insertar_arista('Baia de Ha Long', 'Selva Amazonica', 18430)
grafo1.insertar_arista('Baia de Ha Long', 'Montana de la mesa', 10356)
grafo1.insertar_arista('Baia de Ha Long', 'Isla Jeju', 3109)
grafo1.insertar_arista('Isla de Comodo', 'Rio Subterraneo de Puerto Princesa', 1748)
grafo1.insertar_arista('Isla de Comodo', 'Cataratas del Iguazu', 16805)
grafo1.insertar_arista('Isla de Comodo', 'Selva Amazonica', 19364)
grafo1.insertar_arista('Isla de Comodo', 'Montaña de la mesa', 10051)
grafo1.insertar_arista('Isla de Comodo', 'Isla Jeju', 4322)
grafo1.insertar_arista('Rio Subterraneo de Puerto Princesa', 'Cataratas del Iguazu', 18524)
grafo1.insertar_arista('Rio Subterraneo de Puerto Princesa', 'Selva Amazonica', 18868)
grafo1.insertar_arista('Rio Subterraneo de Puerto Princesa', 'Montaña de la mesa', 11550)
grafo1.insertar_arista('Rio Subterraneo de Puerto Princesa', 'Isla Jeju', 2628)
grafo1.insertar_arista('Cataratas del Iguazu', 'Selva Amazonica', 2606)
grafo1.insertar_arista('Cataratas del Iguazu', 'Montaña de la Mesa', 7450)
grafo1.insertar_arista('Cataratas del Iguazu', 'Isla Jeju', 18848)
grafo1.insertar_arista('Selva Amazonica', 'Montaña de la mesa', 9342)
grafo1.insertar_arista('Selva Amazonica', 'Isla Jeju', 16255)
grafo1.insertar_arista('Montaña de la Mesa', 'Isla Jeju', 13165)

print()
arbol_minimo = grafo1.kruskal()
#print(arbol_minimo)
print()
arbolito1=arbol_minimo[0].split('-')
arbolito2=arbol_minimo[1].split('-')

print('Árbol de expansión mínimo de maravillas arquitectónicas')
peso_total = 0
for nodo in arbolito1:
    nodo = nodo.split(';')
    peso_total += int(nodo[2])
    print(f'{nodo[0]}-{nodo[1]}-{nodo[2]}')

#print(peso_total)
print()

print('Árbol de expansión mínimo de maravillas naturales')
peso_total = 0
for nodo in arbolito2:
    nodo = nodo.split(';')
    peso_total += int(nodo[2])
    print(f'{nodo[0]}-{nodo[1]}-{nodo[2]}')

#print(peso_total)
print()
maravillas=grafo1.contar_maravillas()
for maravilla in maravillas:
    if maravillas[maravilla]['arq'] and maravillas[maravilla]['nat']:
        print(f'{maravilla} tiene maravillas arquitectonicas y naturales')

print()
maravillas2=grafo1.contar_maravillas_2()
for maravilla in maravillas2:
    if maravillas2[maravilla]['arq']>1 or maravillas2[maravilla]['nat']>1:
        print(f'{maravilla}, tiene más de una maravilla del mismo tipo')