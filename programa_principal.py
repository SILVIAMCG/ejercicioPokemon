from moves import get_move
from clase_pokemon import Pokemon


# 1. Deplegamos la Bienvenida al Simulador
print("Bienvenido al simulador")


# 2. Ingreso Nombre del Pokemon Atacante
inicializado = False
while inicializado == False:
        # Hacer 

            # 2.0 Solicitar el nombre y recibirlo en una variable 
    nombreAtacante = input("Ingrese el nombre del primer Pokémon: ")
    print("\n")


            # 2.1 Validar que nombre no sea vacio

            # 2.2 Transformar el nombre a minusculas
    nombreAtacante = nombreAtacante.lower()

            # 2.3 Crear el objeto Pokemon
    pokemonAtacante = Pokemon()

            # 2.35 Intentar Inicializar el boolean inicializado = Pokemon.inicializar(nombre). Si pudo inicializarlo, retorna true
    inicializado = pokemonAtacante.inicializar(nombreAtacante)


            # 2.4 Si inicializado == false. Desplegar 'No existe un pokemon con dicho nombre'. 
    if inicializado != True:
        print("No existe un pokemon con dicho nombre")
     
#Aqui termina el While

# 3. Despliega la informacion del Pokemon Atacante a nivel base

    # 3.1 PokemonAtacante.despliegaInformacionBasica(), va a ser: numero, nombre y tipo
pokemonAtacante.despliegaInformacionBasica()


    # 3.2 PokemonAtacante.despliegaStats(), 
pokemonAtacante.despliegaStats()

    # 3.3 PokemonAtacante.despliegaMovimientos()

pokemonAtacante.despliegaMovimientos()

# 4. Seleccionar Ataque a ejecutar (Pokemon Atacante)

     # Hacer 
esAtaqueValido = False
numeroAtaque = 0
while esAtaqueValido == False: 
    
        # 4.1 Solicitar el número del ataque
    numeroAtaque = int(input("Seleccione un ataque a ejecutar: "))

    esAtaqueValido = numeroAtaque > 0 and numeroAtaque < len(pokemonAtacante.getMovimientos())

    if esAtaqueValido == False:
        print("No existe un Ataque con dicho número")
        
    else:
        # 4.4 Desplegar información básica del ataque. 
    # 
    #   pokemon.desplegarInformacionBasicaAtaque(numeroAtaque) 
    #     Debe desplegar nombre de ataque seleccionado y poder de ataque
        pokemonAtacante.desplegarInformacionBasicaAtaque(numeroAtaque)
        
        


# 5. Desplegar poder de ataque y Stats a nivel 50 

    #5.0 PokemonAtacante.cambiaDeNivel(nivel=50), donde nivel podria ser 'base' o 50.
pokemonAtacante.cambiaDeNivel("50")

    #5.1 PokemonAtacante.despliegaStats()
pokemonAtacante.despliegaStats()


# 6. Ingreso el nombre del Pokemon Rival
inicializadoRival = False
while inicializadoRival == False:
        # Hacer 

            # 6.0 Solicitar el nombre y recibirlo en una variable 
    nombreRival = input("Ingrese el nombre a atacar Pokémon: ")
    print ("\n")



            # 6.1 Validar que nombre no sea vacio

            # 6.2 Transformar el nombre a minusculas
    nombreRival = nombreRival.lower()

            # 6.3 Crear el objeto Pokemon
    pokemonRival = Pokemon()

            # 6.35 Intentar Inicializar el boolean inicializado = Pokemon.inicializar(nombre). Si pudo inicializarlo, retorna true
    inicializadoRival = pokemonRival.inicializar(nombreRival)


            # 6.4 Si inicializado == false. Desplegar 'No existe un pokemon con dicho nombre'. 
    if inicializadoRival != True:
        print("No existe un pokemon con dicho nombre")

#7 Muestra nombre de pokemon rival
pokemonRival.despliegaInformacionBasica()


# 8. Desplegar poder de ataque y Stats a nivel 50
    # ver punto 5

    #8.0 PokemonRival.cambiaDeNivel(nivel=50), donde nivel podria ser 'base' o 50.
pokemonRival.cambiaDeNivel("50")

    #8.1 PokemonRival.despliegaHP a nivel 50()
hpRival=pokemonRival.getHp()
print ("El hp a nivel 50 de " + pokemonRival.getNombre() + " es " + str(hpRival))

# 9. Desplegar el daño realizado por el Pokemon Atacante al Pokemon Rival 
    # 9.1 PokemonAtacante.Ataca(PokemonRival) retona el danno efectuado por el Pokemon atacante al pokemon rival 
    #      y resta el valor del danno del HP del PokemonRival


tipo_de_ataque = pokemonAtacante.getMovimientos()[numeroAtaque]
dannoEfectuado = pokemonAtacante.ataca(tipo_de_ataque[1],pokemonRival.getTipo(),tipo_de_ataque[3],pokemonRival.get_categoria_tipo_defensa(tipo_de_ataque[3]),tipo_de_ataque[2])

print("El daño que realizó "+pokemonAtacante.getNombre()+" a "+pokemonRival.getNombre()+" fue de: " + str(dannoEfectuado))
hp = pokemonRival.getHp()
pokemonRival.setHp(hp-dannoEfectuado)

# 10. Desplegar el HP restante del Pokemon Rival 
    # 11.1 desplegar el HP restante del pokemon rival despues del daño. PokemonRival.getHp()

print(pokemonRival.getNombre()+" quedó con un HP de: "+ str(pokemonRival.getHp()))

# 12. Fin del Programa 


