
from moves import get_move
from math import sqrt as raiz
from funciones import *

class Pokemon:

#Definir atributos iniciales de cada pokemon
    def __init__(self):
        self.nombre = "indefinido"
        self.tipo = ""
        self.hp = 0
        self.ataque = 0
        self.defensa = 0
        self.defensaEspecial = 0
        self.ataqueEspecial = 0
        self.velocidad = 0
        self.movimientos = []
        self.nivel = "base"

##################################
#Setters
##################################
    def setNombre(self, nuevonombre):
        self.nombre = nuevonombre

    def setTipo(self, nuevotipo):
        self.tipo = nuevotipo

    def setHp(self,nuevoHp):
        self.hp = nuevoHp

    def setAtaque(self,nuevoataque):
        self.ataque = nuevoataque

    def setDefensa(self,nuevaDefensa):
        self.defensa = nuevaDefensa

    def setAtaqueEspecial(self,nuevoAtaqueEspecial):
        self.ataqueEspecial = nuevoAtaqueEspecial

    def setDefensaEspecial(self,nuevaDefensaEspecial):
        self.defensaEspecial = nuevaDefensaEspecial

    def setVelocidad(self,nuevaVelocidad):
        self.velocidad = nuevaVelocidad
    
    def setMovimientos(self,nuevoMovimientos):
        self.movimientos = nuevoMovimientos

    def setNivel(self, nuevoNivel):
        self.nivel = nuevoNivel

##################################
#Getters
##################################
    def getNombre(self):
        return self.nombre.capitalize()

    def getTipo(self):
        return self.tipo

    def getHp(self):
        return self.hp

    def getAtaque(self):
        return self.ataque

    def getDefensa(self):
        return self.defensa

    def getAtaqueEspecial(self):
        return self.ataqueEspecial 

    def getDefensaEspecial(self):
        return self.defensaEspecial
        
    def getVelocidad(self):
        return self.velocidad

    def getMovimientos(self):
        return self.movimientos

    def getNivel(self):
        return self.nivel

    # Incializa el objeto pokemon.
    #
    # Retorna True : si el Objeto Pokemon pudo ser inicializado satisfactoriamente
    # Retorna False: si el Objeto Pokemon no pudo ser inicializado con los valores correspondientes 
    def inicializar(self, nombrePokemon):
        # 1. verificar que el archivo pokemon_data.csv existe y lo puedo abrir en modo lectura
        
        textWrapper = open("pokemon_data.csv","r")

        # 2. recorrer el archivo buscando si nombrePokemonExiste
        
        #inicializo un indice en 0 para contar el numero de pokemon
        i = 0
        for lineRaw in textWrapper:
            
            lineSplitted = lineRaw.strip().split(",")
        
            name = lineSplitted[0]

            # 3. Si existe, debo hacer:
            #Si el pokemon esta en la lista, asignamos la LineSplited[0...8] a las variables de instancia (self)
            # y retornamos True
            # 3.1 asignar los siguientes valores al objeto (self) de acuerdo a su orden de aparicion en la lista
            # posición: 0 - Nombre
            #           1 - Tipo
            #           2 - hp
            #           3 - ataque
            #           4 - defensa
            #           5 - ataqueEspecial
            #           6 - defensaEspecial
            #           7 - velocidad
            #           8 - listado de movimientos (estan separados por ;)
            if name == nombrePokemon:
                self.nombre = lineSplitted[0]
                self.tipo = lineSplitted[1]
                self.hp = lineSplitted[2]
                self.ataque = lineSplitted[3]
                self.defensa = lineSplitted[4]
                self.ataqueEspecial = lineSplitted[5]
                self.defensaEspecial = lineSplitted[6]
                self.velocidad = lineSplitted[7]

                # Como el ultimo elemento trae la lista de movimientos separados por ; necesitamos hacer split de nuevo
                nombresDeMovimientos = lineSplitted[8].split(";")

                #recorremos la lista de movimientos y obtenemos los atributos de cada uno desde el archivo moves.py
                for nombreMovimiento in nombresDeMovimientos:
                    atributosMovimiento = get_move(nombreMovimiento)
                    

                    #Agrego el ataque en la lista de movimientos
                    self.movimientos.append(atributosMovimiento)

                #Una vez creado el Pokemon, retorno True por que la incializacion fue exitosa

                return True
            #incremento el indice para contar el numero de pokemon siguiente
            i+=1


        #4. Si el programa llego a esta linea es por que el nombre del pokemon no se encontro en el archivo y debo retornar False
        return False

    # Despliega numero, nombre y tipo del pokemon. 
    # Retorna: nada
    def despliegaInformacionBasica(self):
        # imprimir atributos de la siguiente manera: (recordar capitalizar el nombre y el tipo)
        # Pokemon número 380
        # Nombre del Pokémon: Latias
        # Sus tipos son: 
        #   - Dragon
        print("Nombre del Pokémon seleccionado: " + self.nombre.capitalize() + "\n")
        return

    # Cambia de nivel al pokemon de nivel base a nivel 50
    def cambiaDeNivel(self, level):
        #asigna el nivel del pokemon al nueva nivel
        self.nivel=level

        #inicia el calculo de hp y las otras stats
        #Los puntos individuales (𝐼𝑉) son un valor constante = 31
        iv = 31 

        #El nivel (𝐿𝑒𝑣𝑒𝑙) de los Pokémon es un valor constante = 50
        level50 = 50

        #Los puntos de esfuerzo (𝐸𝑉) son un valor constante = 250
        ev = 250

        #Los puntos base (𝐵𝑎𝑠𝑒) del “stat” de los Pokémon es un valor variable que está en el archivo CSV
        
        #Calculamos nuevos stats
        hpNivel50 = self.calculaStats("hp", self.getHp(), iv, ev, 50)
        ataqueNivel50 = self.calculaStats("ataque", self.getAtaque(), iv, ev, level50)
        defensaNivel50 = self.calculaStats("defensa", self.getDefensa(), iv, ev, level50)
        ataqueEspecialNivel50 = self.calculaStats("ataqueEspecial", self.getAtaqueEspecial(), iv, ev, level50)
        defensaEspecialNivel50 = self.calculaStats("defensaEspecial", self.getDefensaEspecial(), iv, ev, level50)
        velocidadNivel50 = self.calculaStats("velocidad", self.getVelocidad(), iv, ev, level50)

        #Asignamos los nuevos stats al Objeto pokemon
        self.setHp(hpNivel50)
        self.setAtaque(ataqueNivel50)
        self.setDefensa(defensaNivel50)
        self.setAtaqueEspecial(ataqueEspecialNivel50)
        self.setDefensaEspecial(defensaEspecialNivel50)
        self.setVelocidad(velocidadNivel50)

        return

    #Aqui va la formula de las ecuaciones 1 y 2
    # retorna el stat correspondiente al nivel 50 desde el stat base(actual) del pokemon
    def calculaStats(self, stat, base, iv, ev, level):
        nuevaStat = 0
        if stat == "hp":
            #ecuacion 1: Hp
            nuevaStat = (((int(base) + iv)*2+raiz(ev)/4)*level)/100 + level + 10
        else:
            #ecuacion 2: other Stats
            nuevaStat = (((int(base) + iv)*2+raiz(ev)/4)*level)/100 + 5
        
        return nuevaStat



    def despliegaStats(self):
        # Imprime los atributos del objeto en el siguiente formato:
        # Si self.nivel == "base"
            # el formato es:
            # Estadísticas base del Pokémon: 
            # - HP = 80
            # - Ataque = 80
            # - Defensa = 90
            # - Ataque especial = 110
            # - Defensa especial = 130
            # - Velocidad = 110

        if self.nivel == "base":
            print("Estadísticas base del Pokémon:")
            print("  - HP = " + str(self.hp))
            print("  - Ataque = " + str(self.ataque))
            print("  - Defensa = " + str(self.defensa))
            print("  - Ataque especial = " + str(self.ataqueEspecial))
            print("  - Defensa especial = " + str(self.defensaEspecial))
            print("  - Velocidad = " + str(self.velocidad)+ "\n")
        else: #Sino, significa que el el nivel es 50
            print("El hp al nivel 50 de " + self.nombre.capitalize() + " es " + str(self.hp))
            print("El atk al nivel 50 de " + self.nombre.capitalize() + " es " + str(self.ataque))
            print("El def al nivel 50 de " + self.nombre.capitalize() + " es " + str(self.defensa))
            print("El spa al nivel 50 de " + self.nombre.capitalize() + " es " + str(self.ataqueEspecial))
            print("El spd al nivel 50 de " + self.nombre.capitalize() + " es " + str(self.defensaEspecial))
            print("El spe al nivel 50 de " + self.nombre.capitalize() + " es " + str(self.velocidad))

        return

    # imprime los Ataques del Pokemon en el siguiente formato:
    # Movimientos que puede aprender el pokémon: 
    # 0 - Aerial Ace
    # 1 - Ally Switch
    # 2 - Attract
    # ...
    def despliegaMovimientos(self):
        # Obtener los datos desde self.movimientos, recorrer la lista y desplegar nombre y numero de cada uno
        # El nombre del ataque esta en el indice[0] de cada movimiento[i]
        
        print("Movimientos que puede aprender el pokémon: ")

        for i in range (0, len(self.movimientos)):
            print(str(i) +" - " + self.movimientos[i][0])

        return


    def get_categoria_tipo_defensa(self,tipo):
        if tipo == "special":
            salida_tipo = self.getDefensaEspecial()
        else:
            salida_tipo = self.getDefensa()
        return salida_tipo
    def get_categoria_tipo_ataque(self,tipo):
        if tipo == "special":
            salida_tipo = self.getAtaqueEspecial()
        else:
            salida_tipo = self.getAtaque()
        return salida_tipo
    # Ataca(pokemonRival) retorna el danno efectuado (float) por el Pokemon atacante al pokemon rival 
    # y resta el valor del danno del HP del PokemonRival
    ####def ataca(self, pokemonRival):
    def ataca(self,poder_ataque,tipo_rival,ataque,defensa,ataque_tipo):
        
        # 0. Leer la tabla

        # 1. calcular el modificador

        # 2. Hacer el calculo del danno

        # 3. al objeto pokemon rival, restarle el danno causado de sus hp. pokemonRival.setHp(pokemonRival.getHp() - danno)
        ataque = self.get_categoria_tipo_ataque(ataque)
        power = poder_ataque
        #Condición para evitar calculo, existen ataques que no producen daño, pero modifican otros aspectos
        if power > 0:
            stab = calculo_stab(self.getTipo(),ataque_tipo)
            efectividad = efectividad_ataque(ataque_tipo,tipo_rival)
            random = random_fl()
            modifier = efectividad* stab * random
            danio = ((((((2*50)/5)+2)*power*(ataque/defensa))/50)+2)*modifier
        else:
            danio = 0
        return danio
    

    def desplegarInformacionBasicaAtaque(self, numeroAtaque):
        salida = print("El ataque selecionado es: " + self.movimientos[numeroAtaque][0])
        print("Poder de ataque es: " + str(self.movimientos[numeroAtaque][1]))

        return salida


    




    

