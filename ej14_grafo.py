from mi_grafo import Grafo

grafo1 = Grafo(dirigido=False)

grafo1.insertar_vertice('Cocina')
grafo1.insertar_vertice('Comedor')
grafo1.insertar_vertice('Cochera')
grafo1.insertar_vertice('Quincho')
grafo1.insertar_vertice('Baño1')
grafo1.insertar_vertice('Baño2')
grafo1.insertar_vertice('Habitacion1')
grafo1.insertar_vertice('Habitacion2')
grafo1.insertar_vertice('Sala de estar')
grafo1.insertar_vertice('Terraza')
grafo1.insertar_vertice('Patio')

grafo1.insertar_arista('Cocina', 'Sala de estar', 5)
grafo1.insertar_arista('Cocina', 'Habitacion1', 3)
grafo1.insertar_arista('Cocina', 'Baño1', 2)
grafo1.insertar_arista('Sala de estar', 'Patio', 7)
grafo1.insertar_arista('Sala de estar', 'Quincho', 2)
grafo1.insertar_arista('Sala de estar', 'Cochera', 4)
grafo1.insertar_arista('Sala de estar', 'Comedor', 6)
grafo1.insertar_arista('Sala de estar', 'Habitacion2', 5)
grafo1.insertar_arista('Comedor', 'Baño2', 6)
grafo1.insertar_arista('Comedor', 'Habitacion2', 7)
grafo1.insertar_arista('Comedor', 'Terraza', 4)
grafo1.insertar_arista('Comedor', 'Patio', 9)
grafo1.insertar_arista('Comedor', 'Cochera', 1)
grafo1.insertar_arista('Cochera', 'Patio', 15)
grafo1.insertar_arista('Cochera', 'Terraza', 23)
grafo1.insertar_arista('Cochera', 'Baño1', 21)
grafo1.insertar_arista('Quincho', 'Habitacion2', 12)
grafo1.insertar_arista('Quincho', 'Patio', 2)
grafo1.insertar_arista('Quincho', 'Baño2', 19)
grafo1.insertar_arista('Baño1', 'Terraza', 5)
grafo1.insertar_arista('Baño1', 'Patio', 9)
grafo1.insertar_arista('Baño1', 'Baño2', 30)
grafo1.insertar_arista('Baño2', 'Cocina', 27)
grafo1.insertar_arista('Baño2', 'Habitacion1', 45)
grafo1.insertar_arista('Baño2', 'Cochera', 39)
grafo1.insertar_arista('Habitacion1', 'Patio', 1)
grafo1.insertar_arista('Habitacion1', 'Terraza', 6)
grafo1.insertar_arista('Habitacion1', 'Habitacion2', 7)
grafo1.insertar_arista('Habitacion2', 'Terraza', 40)
grafo1.insertar_arista('Habitacion2', 'Patio', 29)
grafo1.insertar_arista('Habitacion2', 'Cochera', 10)
grafo1.insertar_arista('Terraza', 'Quincho', 11)
grafo1.insertar_arista('Terraza', 'Cocina', 18)
grafo1.insertar_arista('Terraza', 'Sala de estar', 20)
grafo1.insertar_arista('Patio', 'Baño2', 16)
grafo1.insertar_arista('Patio', 'Terraza', 33)
grafo1.insertar_arista('Patio', 'Cocina', 25)


print("Árbol de expanción mínima ")
arbol_minimo = grafo1.kruskal()
arbol_minimo = arbol_minimo[0].split('-')
peso_total = 0
for nodo in arbol_minimo:
    nodo = nodo.split(';')
    peso_total += int(nodo[2])
    print(f'{nodo[0]}-{nodo[1]}-{nodo[2]}')
print()
print(f"la cantidad de metros de cable necesario para conectar todos los ambientes es {peso_total}")
print()
if grafo1.existe_paso('Habitacion1', 'Sala de estar'):
    resultados = grafo1.dijkstra('Habitacion1')
    camino = grafo1.camino(resultados, 'Habitacion1', 'Sala de estar')
    print(f'El camino es ' , camino['camino'],'. Se necesitarán ' ,camino['costo'], ' metros de cable para conectar el router com el smart tv')
else:
    print('no se puede llegar')