
class JuegoAdivinanzas:
    def __init__(self, numerosecreto=(1,100), maxIntentos=5 ):
        self.numerosecreto= numerosecreto
        self.maxIntentos= maxIntentos
        self.intentos=0       

    def validarNumero(self):
        n= ""
        if self.numerosecreto == n:
            print("Felicidades has encontrado el numero secreto")

        elif self.numerosecreto < n:
            print("El número que escogiste es menor al número secreto")
        
        elif self.numerosecreto > n:
            print("El número que escogiste es mayor al número secreto")
            return

    def registrarIntento(self):
        for i in range(5):
            contador +=1
        while self.intentos < self.maxIntentos:
            intento = []
            if intento == self.numerosecreto:
                print("Ganaste")
            elif intento != self.numerosecreto:
                print("Incorrecto, te quedan", self.maxIntentos - self.intentos, "intentos")
            
            elif intento == self.maxIntentos:
                print(f"Lo sentimos se acabaron tus intentos, el numero era {self.numerosecreto}")


    def reiniciar(self):
        self.__init__()
        
class Jugador(JuegoAdivinanzas):
    def __init__(self, nombre, historial, ganados):
        self.nombre=nombre
        self.historial= historial
        self.ganados=ganados

    def registrar(self, u):
        u=""
        b= self.nombre.append(u)
        print(b)
        
    def mostrarHistorial(self, intentos, resultado):
        print(self.nombre)
        self.historial.append(intentos, resultado)
        
    
    def estadística(self):
        intentos= len(self.historial)
        ganados= 0
        for i in self.historial:
            if i==1:
                ganados +=1
        PorcentajeGanados= (i/intentos)*100
        IntentosFallidos= intentos-ganados
        print(f"Porcentaje ganado: {PorcentajeGanados}")
        print(f"Cantidad fallida{IntentosFallidos}")

        
def menu():
    continuar = True
    historial = list()
    
    with open("Estadísticas.txt","w"):
        print("Archivo Estadísticas.txt ya existe")
        
    while continuar:
        print("""
a.Comenzar una nueva partida
b.Ver estadisticas del jugador
c.Salir del juego
              """)

        opcion = input("Ingrese una opción: ")

        if opcion == "a":
            u = input("Cree su nombre de jugador: ")
            print("**Adivina el número secreto**")
            n = int(input("Escriba un número del 1 al 100: "))
            Juego = JuegoAdivinanzas()
            Juego.validarNumero()
            Juego.registrarIntento()
            Player = Jugador()
            Player.registrar(u)

        elif opcion == "b":
            Player.mostrarHistorial()
            

        elif opcion == "c":
            print("Saliendo...")
            Juego.reiniciar()
            break

        else:
            print("Seleccione una opción correcta")
            return
menu()

    

