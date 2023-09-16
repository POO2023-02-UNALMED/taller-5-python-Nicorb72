class Mamifero:
    _listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._listado.append(self)

    @staticmethod
    def cantidadMamiferos():
        return len(Mamifero._listado)
    
    @classmethod
    def crearCaballo(cls, nombre, edad, habitat, genero):
        