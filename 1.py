class TreeNode:
    def __init__(self, pokemon):
        self.pokemon = pokemon
        self.left = None
        self.right = None

class Pokedex:
    def __init__(self):
        self.root_by_number = None
        self.root_by_name = None
        self.tree_by_type = {}

    def _insert_by_number(self, node, pokemon):
        if not node:
            return TreeNode(pokemon)
        if pokemon['numero'] < node.pokemon['numero']:
            node.left = self._insert_by_number(node.left, pokemon)
        elif pokemon['numero'] > node.pokemon['numero']:
            node.right = self._insert_by_number(node.right, pokemon)
        return node

    def _insert_by_name(self, node, pokemon):
        if not node:
            return TreeNode(pokemon)
        if pokemon['nombre'] < node.pokemon['nombre']:
            node.left = self._insert_by_name(node.left, pokemon)
        elif pokemon['nombre'] > node.pokemon['nombre']:
            node.right = self._insert_by_name(node.right, pokemon)
        return node

    def agregar_pokemon(self, nombre, numero, tipos):
        pokemon = {'nombre': nombre, 'numero': numero, 'tipos': tipos}
        self.root_by_number = self._insert_by_number(self.root_by_number, pokemon)
        self.root_by_name = self._insert_by_name(self.root_by_name, pokemon)
        for tipo in tipos:
            if tipo not in self.tree_by_type:
                self.tree_by_type[tipo] = []
            self.tree_by_type[tipo].append(pokemon)

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.pokemon)
            self._inorder_traversal(node.right, result)

    def listar_pokemon_por_numero(self):
        result = []
        self._inorder_traversal(self.root_by_number, result)
        return result

    def listar_pokemon_por_nombre(self):
        result = []
        self._inorder_traversal(self.root_by_name, result)
        return result

    def buscar_pokemon(self, consulta):
        resultados = []

        if consulta.isdigit():
            numero = int(consulta)
            current = self.root_by_number
            while current:
                if numero == current.pokemon['numero']:
                    resultados.append(current.pokemon)
                    break
                elif numero < current.pokemon['numero']:
                    current = current.left
                else:
                    current = current.right

        current = self.root_by_name
        while current:
            if consulta.lower() in current.pokemon['nombre'].lower():
                resultados.append(current.pokemon)
            if consulta.lower() < current.pokemon['nombre'].lower():
                current = current.left
            else:
                current = current.right

        if not resultados:
            print("No se encontró ningún Pokémon que coincida con la consulta.")
        else:
            for pokemon in resultados:
                print(f"Nombre: {pokemon['nombre']}, Número: {pokemon['numero']}, Tipos: {', '.join(pokemon['tipos'])}")

    def nombres_por_tipo(self, tipos):
        resultados = []
        for tipo in tipos:
            if tipo in self.tree_by_type:
                for pokemon in self.tree_by_type[tipo]:
                    resultados.append(pokemon['nombre'])
        return resultados

    def listar_nombres_por_tipos(self, tipos_buscados):
        nombres_por_tipo = self.nombres_por_tipo(tipos_buscados)
        if not nombres_por_tipo:
            print("No se encontraron Pokémon con los tipos especificados.")
        else:
            print("Nombres de Pokémon por tipo:", nombres_por_tipo)

    def contar_tipos(self, tipos):
        contador = 0
        for tipo in tipos:
            if tipo in self.tree_by_type:
                contador += len(self.tree_by_type[tipo])
        return contador
pokedex = Pokedex()

pokedex.agregar_pokemon("Jolteon", 135, ["Eléctrico"])
pokedex.agregar_pokemon("Dragonair", 148, ["Dragón"])
pokedex.agregar_pokemon("Magnezone", 462, ["Eléctrico", "Acero"])
pokedex.agregar_pokemon("Drapion", 452, ["Veneno", "Oscuro"])
pokedex.agregar_pokemon("Torkoal", 324, ["Fuego"])
pokedex.agregar_pokemon("Sunflora", 192, ["Planta"])
pokedex.agregar_pokemon("Gastrodon", 423, ["Agua", "Tierra"])
pokedex.agregar_pokemon("Dragapult", 887, ["Fantasma", "Dragón"])
pokedex.agregar_pokemon("Lycanroc", 745, ["Roca"])
pokedex.agregar_pokemon("Tyrantrum", 697, ["Roca", "Dragón"])

print("Pokemon comenzados por Dra")
pokedex.buscar_pokemon("dra")

print("Pokémon de los tipos Agua, Fuego, Planta y Eléctrico")
tipos_buscados = ["Agua", "Fuego", "Planta", "Eléctrico"]
pokedex.listar_nombres_por_tipos(tipos_buscados)

print("Listado por número:")
pokemon_por_numero = pokedex.listar_pokemon_por_numero()
for pokemon in pokemon_por_numero:
    print(f"Número: {pokemon['numero']}, Nombre: {pokemon['nombre']}")

print("Listado por nombre:")
pokemon_por_nombre = pokedex.listar_pokemon_por_nombre()
for pokemon in pokemon_por_nombre:
    print(f"Nombre: {pokemon['nombre']}, Número: {pokemon['numero']}")

print("Datos de Jolteon:")
pokedex.buscar_pokemon("Jolteon")

print("Datos de Lycanroc:")
pokedex.buscar_pokemon("Lycanroc")

print("Datos de Tyrantrum:")
pokedex.buscar_pokemon("Tyrantrum")

tipos_busqueda = ["Eléctrico", "Acero"]
total_tipos = pokedex.contar_tipos(tipos_busqueda)
print(f"Total de Pokémon de tipo Eléctrico y Acero: {total_tipos}")