from paquete.modelo import *

#p = PersonaEquipo("Luis")

entrenador = Entrenador ("Jose")
#entrenador.entrenar() #Se llama al metoodo entrenar para que imprima

futbolista = Futbolista("Antonio") 
#futbolista.entrenar()

medico = MedicoEquipo("Ramon")
#medico.entrenar()

presidente = PresidenteEquipo("Francisco")
#presidente.entrenar()

lista = [futbolista, medico, presidente, entrenador] #lista para presentar

for l in lista: #Recorrer
    l.entrenar()