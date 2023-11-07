class Grafo:
    def __init__(self):
        self.vertices = {}
        self.aristas = []

    def agregar_personaje(self, nombre):
        self.vertices[nombre] = set()

    def agregar_relacion(self, personaje1, personaje2, episodios):
        if personaje1 in self.vertices and personaje2 in self.vertices:
            self.vertices[personaje1].add((personaje2, episodios))
            self.vertices[personaje2].add((personaje1, episodios))
            self.aristas.append((personaje1, personaje2, episodios))

    def hallar_arbol_expansion_minimo(self):
        arbol_expansion_minimo = []
        self.aristas.sort(key=lambda x: x[2])
        padre = {personaje: personaje for personaje in self.vertices}
        rango = {personaje: 0 for personaje in self.vertices}

        def encontrar(personaje):
            if padre[personaje] != personaje:
                padre[personaje] = encontrar(padre[personaje])
            return padre[personaje]

        def unir(personaje1, personaje2):
            raiz1 = encontrar(personaje1)
            raiz2 = encontrar(personaje2)
            if raiz1 != raiz2:
                if rango[raiz1] < rango[raiz2]:
                    padre[raiz1] = raiz2
                elif rango[raiz1] > rango[raiz2]:
                    padre[raiz2] = raiz1
                else:
                    padre[raiz2] = raiz1
                    rango[raiz1] += 1

        for arista in self.aristas:
            personaje1, personaje2, episodios = arista
            if encontrar(personaje1) != encontrar(personaje2):
                arbol_expansion_minimo.append(arista)
                unir(personaje1, personaje2)

        return arbol_expansion_minimo

    def contiene_yoda(self, arbol_expansion_minimo):
        for arista in arbol_expansion_minimo:
            personaje1, personaje2, _ = arista
            if "Yoda" in (personaje1, personaje2):
                return True
        return False

    def numero_maximo_episodios_compartidos(self):
        max_episodios = 0
        personajes_max_episodios = []

        for arista in self.aristas:
            personaje1, personaje2, episodios = arista
            if episodios > max_episodios:
                max_episodios = episodios
                personajes_max_episodios = [(personaje1, personaje2)]
            elif episodios == max_episodios:
                personajes_max_episodios.append((personaje1, personaje2))

        return max_episodios, personajes_max_episodios

grafo = Grafo()

personajes = ["Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", "C-3PO", "Leia", "Rey", "Kylo Ren", "Chewbacca", "Han Solo", "R2-D2", "BB-8"]
for personaje in personajes:
    grafo.agregar_personaje(personaje)

relaciones = [
    ("Luke Skywalker", "Darth Vader", 5),
    ("Luke Skywalker", "Yoda", 3),
    ("Darth Vader", "Yoda", 2),
    ("Luke Skywalker", "Leia", 4),
    ("Leia", "Rey", 3),
    ("Rey", "Kylo Ren", 4),
    ("Chewbacca", "Han Solo", 6),
    ("R2-D2", "BB-8", 2),
    ("Boba Fett", "C-3PO", 1),
    ("C-3PO", "R2-D2", 4),
]
for relacion in relaciones:
    grafo.agregar_relacion(relacion[0], relacion[1], relacion[2])

arbol_expansion_minimo = grafo.hallar_arbol_expansion_minimo()
print("Árbol de Expansión Mínimo:")
print(arbol_expansion_minimo)

contiene_yoda = grafo.contiene_yoda(arbol_expansion_minimo)
print("¿El árbol de expansión mínimo contiene a Yoda?", contiene_yoda)

max_episodios, personajes_max_episodios = grafo.numero_maximo_episodios_compartidos()
print("Número máximo de episodios compartidos:", max_episodios)
print("Personajes con el número máximo de episodios compartidos:")
print(personajes_max_episodios)
