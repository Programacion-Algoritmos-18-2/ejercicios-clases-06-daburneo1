import abc

class PersonaEquipo(metaclass=abc.ABCMeta): #Se define la clase abstracta
    
    def __init__(self, nom):
        self.nombre = nom

    @abc.abstractmethod #Decorador, hace el metodo abstracto. 
    def entrenar(): 
        pass    #pass es una caracteristica del metodo abstracto. El pass no hace nada, solo dice que define el metodo pero no se lo implemente
                #un metodo abstracto no tiene implementacion

class Entrenador(PersonaEquipo):
    #constructor
    def __init__(self, n):
        super(Entrenador, self).__init__(n) #Recibe parametro del init de PersonaEquipo
        self.codigo_entrenador = ""

    def entrenar(self):
        print("Yo %s, entrenador, soy el director que dirige el entrenamiento" % \
            self.nombre)

    def agregar_codigo_entrenador(self, ce):
        self.codigo_entrenador = ce

    def obtener_codigo_entrenador(self):
        return self.codigo_entrenador

class Futbolista(PersonaEquipo): #Subclase
	#constructor
    def __init__(self, n):
        super(Futbolista, self).__init__(n) #Heredar
        self.posicion_campo = ""

    def entrenar(self): #Metodo abstracto
        print("Yo %s, futbolista, hago práctica en eltrenamiento" % \
                self.nombre) #Presentar 
        #Metodos set y get
    def agregar_posicion_campo(self, pc):
        self.posicion_campo = pc

    def obtener_posicion_campo(self):
        return self.posicion_campo

class MedicoEquipo(PersonaEquipo): #Subclase
	#constructor
    def __init__(self, n):
        super(MedicoEquipo, self).__init__(n)
        self.titulo = ""

    def entrenar(self): #Metoodo abstracto
        print("Yo %s, medico, atiendo a los jugadores en el entrenamiento" % \
            self.nombre)
        #Metodos set y get
    def agregar_titulo(self, t):
        self.titulo = t

    def obtener_titulo(self):
        return self.titulo

class PresidenteEquipo(PersonaEquipo):  #Subclase
	#constructor
    def __init__(self, n):
        super(PresidenteEquipo, self).__init__(n)#Heredar
        self.numero_propiedades = ""

    def entrenar(self): #Metodo abstracto
        print("Yo %s, presidente, soy el que pongo dinero para el entrenamiento" % \
            self.nombre)
        #Metodos set y get
    def agregar_numero_propiedades(self, np):
        self.numero_propiedades = np

    def obtener_numero_propiedades(self):
        return self.numero_propiedades
