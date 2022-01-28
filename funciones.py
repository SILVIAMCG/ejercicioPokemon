#Abrir archivo efectividad y transformarlo a matriz

def abrir_efectividad():
    fd = open("tabla_efectividad.csv","r")
    a = []
    for i in fd:
        a.append(i.strip().split(","))
    fd.close()
    return a

#Borrar elemento en blanco
def eliminar_header_blanco(a):
    for i in range(0,len(a[0])):
        if a[0][i] == "":
            print(a[0][i])
            del a[0][i]
    return a

#Borrar espacio y transformar en float, para evitar problemas si se llegan a introducir más tipos
def transformar_y_limpiar(a):
    for i in range(1,len(a)):
        for j in range(1,len(a[i])):
            if a[i][j] == "":
                del a[i][j]
            else:
                a[i][j] = float(a[i][j])
    return a



#Pasamos la matriz, junto con el tipo del ataque y el tipo del pokemon a ser atacado, devuelve la posición donde se encuentra el valor
def efectividad_salida(a,tipo_ataque, tipo_pokemon):
    pos_x = 0
    pos_y = 0
    for i in range(0,len(a)):
        if a[i][0] == tipo_ataque:
            pos_y = i
            for j in range(0,len(a[0])):
                if a[0][j] == tipo_pokemon:
                    pos_x = j
                    break
    efectividad = a[pos_y][pos_x]
    return efectividad
#Conjunto completo de efectividad llamando a las demás funciones que realizan los procesos de limpieza y transformación de datos
def efectividad_ataque(tipo_ataque,tipo_pokemon_atacado):
    
    salida = efectividad_salida(transformar_y_limpiar
                                (eliminar_header_blanco
                                (abrir_efectividad()
                                )),
                                tipo_ataque,tipo_pokemon_atacado)

    return salida

    
    




def random_fl():
    from random import uniform
    random = round(uniform(0.85,1),2)
    return random



def calculo_stab(tipo_pokemon,tipo_ataque):
    if tipo_pokemon == tipo_ataque:
        stab = 1.2
    else:
        stab = 1
    return stab

def get_categoria_tipo(self,tipo):
    if tipo == "special":
        salida_tipo = self.defensa_esp
    else:
        salida_tipo = self.defensa
    return salida_tipo


