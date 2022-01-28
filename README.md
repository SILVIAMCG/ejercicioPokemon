# ejercicioPokemon
Programa de un juego Pokemon
II. Enunciado.
El evento más importante del mundo de los juegos acaba de anunciar una nueva versión para este año, en la que cada uno de los países que compone el globo reúne a millares de niños, jóvenes y adultos para enfrentarse en un duelo campal para demostrar quién es el mejor. El evento consiste en que los participantes, denominados entrenadores, se enfrentan entre sí en torneos locales de cada país junto a sus monstruos de bolsillo llamados Pokémon, criaturas con poderes inimaginables que vuelven cada enfrentamiento una experiencia emocionante, tanto para los entrenadores como para los espectadores.
El torneo consiste en que cada entrenador posee como máximo de 6 criaturas de las cuales sólo pueden utilizar 4 en cada enfrentamiento. La dificultad de este evento radica en que actualmente existen 898 tipos de Pokémon y por lo tanto existen muchas combinaciones posibles de equipos: 𝐶6(898)=(8986)=898!6!(898−6)!=898⋅897⋅896⋅895⋅894⋅8936∙5∙4∙3∙2∙1=716236263669472 combinaciones
Cada Pokémon tiene sus propias estadísticas, ventajas y desventajas que lo vuelven único. Las estadísticas base de cada criatura son las siguientes:
• HP o Puntos de vida, Puntos de Ataque, Puntos de Defensa, Puntos de Ataque Especial, Puntos de Defensa Especial, y Puntos de Velocidad.
Las ventajas o desventajas de cada Pokémon al enfrentarse a otro están determinadas por su tipo y el de su contrincante:
• Normal, Fuego, Agua, Eléctrico, Planta, Hielo, Lucha, Veneno, Tierra, Volador, Psíquico, Bicho, Roca, Fantasma, Dragón, Siniestro, Acero, y Hada.
Un entrenador, cuyo nombre es Nabu Go, ha participado en innumerables torneos y ha recopilado la información completa de los Pokémon existentes en un archivo CSV (pokemon_data.csv) y la efectividad de cada tipo de Pokémon (tabla_efectividad.csv), además de un script en Python (moves.py) que devuelve el poder de ataque de un movimiento de cada personaje (consultar el Anexo D para ver su funcionamiento)
Tarea 2 – Introducción a la Programación - 2021
El CSV (delimitado por comas) del archivo pokemon_data.csv está organizado de la siguiente forma:
nombre,tipo,puntos_de_vida,puntos_de_ataque_fisico_base,puntos_de_defensa_fisica_base, puntos_de_ataque_especial_base,puntos_de_defensa_especial_base,puntos_de_velocidad_base,movimientos posibles delimitado por ;,
Ejemplo de los datos:
charizard,fire,78,84,78,109,85,100,aerialace;aircutter;airslash;attract;bide;blastburn;bodyslam;brickbreak;brutalswing;bulldoze;captivate;confide;counter;curse;cut;defensecurl;defog;dig;doubleedge;doubleteam;dragonbreath;dragonclaw;dragondance;dragonpulse;dragonrage;dragontail;dynamicpunch;earthquake;echoedvoice;ember;endure;facade;fireblast;firefang;firepledge;firepunch;firespin;fissure;flameburst;flamecharge;flamethrower;flareblitz;fling;fly;focusblast;focuspunch;frustration;furycutter;gigaimpact;growl;headbutt;heatwave;hiddenpower;holdhands;honeclaws;hyperbeam;incinerate;inferno;irontail;leer;megakick;megapunch;metalclaw;mimic;mudslap;naturalgift;ominouswind;outrage;overheat;poweruppunch;protect;rage;reflect;rest;return;roar;rockslide;rocksmash;rocktomb;roost;round;sandstorm;scaryface;scratch;secretpower;seismictoss;shadowclaw;skullbash;skydrop;slash;sleeptalk;smokescreen;snore;solarbeam;steelwing;strength;submission;substitute;sunnyday;swagger;swift;swordsdance;tailwind;takedown;thunderpunch;toxic;twister;willowisp;wingattack;workup,
Nabu lo ha contactado a usted para desarrollar una herramienta que permita a los entrenadores planificar mejor sus estrategias en las batallas de torneos competitivos. La idea es que el software pueda calcular el daño aproximado que provocará un ataque considerando el tipo, el poder del ataque, la potencia de ataque del Pokémon y la resistencia del Pokémon rival.
Para lograr el objetivo debe realizar lo siguiente:
1. Debe calcular los puntos estadísticos (Stats) de ambos Pokémon utilizando las siguientes fórmulas:
a. Fórmula para determinar los puntos de vida del Pokémon:
𝐻𝑃=[ ((𝐵𝑎𝑠𝑒+𝐼𝑉)∗2+[√𝐸𝑉]4)∗𝐿𝑒𝑣𝑒𝑙100] +𝐿𝑒𝑣𝑒𝑙+10
Ecuación 1 - Fórmula para calcular los puntos de vida
b. Fórmula para calcular los otros puntos estadísticos (Ataque, Defensa, Ataque Especial, Defensa Especial y Velocidad):
𝑂𝑡ℎ𝑒𝑟𝑆𝑡𝑎𝑡=[ ((𝐵𝑎𝑠𝑒+𝐼𝑉)∗2+[[√𝐸𝑉]4 ])∗𝐿𝑒𝑣𝑒𝑙100] +5
Ecuación 2 - Fórmula para calcular otros puntos estadísticos
Tarea 2 – Introducción a la Programación - 2021
Considere que:
• El nivel (𝐿𝑒𝑣𝑒𝑙) de los Pokémon es un valor constante = 50
• Los puntos base (𝐵𝑎𝑠𝑒) del “stat” de los Pokémon es un valor variable que está en el archivo CSV
• Los puntos individuales (𝐼𝑉) son un valor constante = 31
• Los puntos de esfuerzo (𝐸𝑉) son un valor constante = 250
2. Una vez obtenido los “Stats”, debe calcular la potencia de daño que hará un ataque que seleccione el usuario desde el Pokémon Atacante al Pokémon Rival utilizando la siguiente formula:
𝐷𝑎𝑚𝑎𝑔𝑒= ((2∗𝐿𝑒𝑣𝑒𝑙5+2)∗𝑃𝑜𝑤𝑒𝑟∗ 𝐴𝐷⁄50+2)∗𝑀𝑜𝑑𝑖𝑓𝑖𝑒𝑟
Ecuación 3 - Fórmula para calcular el daño aproximado
Considere que:
• Donde 𝐷𝑎𝑚𝑎𝑔𝑒 es el daño aproximado que provocará el ataque,
• 𝐿𝑒𝑣𝑒𝑙 es el nivel del Pokémon atacante, es un valor constante = 50,
• 𝑃𝑜𝑤𝑒𝑟 es la potencia del ataque y es un valor variable que entrega la función get_move del script moves.py,
• 𝐴 son los puntos de ataque del Pokémon atacante que se obtiene a partir de la fórmula para calcular los otros “stats” (Ecuación 2). Nota: dependiendo de la categoría del ataque, si especial o físico, el valor que utilizará esta variable será ataque especial o física, respectivamente,
• 𝐷 son los puntos de defensa del Pokémon rival que se obtiene a partir de la fórmula para calcular los otros “stats” (Ecuación 2). Dependiendo de la categoría del atacante, si especial o físico, el valor que utilizará esta variable será defensa especial o física respectivamente,
• 𝑀𝑜𝑑𝑖𝑓𝑖𝑒𝑟 es un valor dinámico que se obtiene utilizando la siguiente formula:
𝑀𝑜𝑑𝑖𝑓𝑖𝑒𝑟=𝑇𝑦𝑝𝑒∗𝑆𝑇𝐴𝐵∗ 𝑟𝑎𝑛𝑑𝑜𝑚∗1
Ecuación 4 - Fórmula para calcular el daño aproximado
o 𝑟𝑎𝑛𝑑𝑜𝑚 es un valor aleatorio entre 0.85 y 1,
o 𝑆𝑇𝐴𝐵 es 1.2 siempre y cuando el ataque ejecutado sea del mismo tipo del Pokémon atacante de lo contrario es 1
o El tipo de ataque (𝑇𝑦𝑝𝑒) determinará si el ataque es efectivo o no, considerando los siguientes valores:
✓ 0: No tiene efecto (Ejemplo: Normal contra Fantasma),
✓ 0.5: No es efectivo (Ejemplo: Fuego contra Agua),
✓ 1: Efectividad normal (Ejemplo: Tierra contra Lucha),
✓ 2: Super Efectivo (Ejemplo: Dragón contra Dragón).
❖ Esta información se puede obtener desde el archivo “tabla_efectividad.csv”, consultar Anexo C para ver su estructura.
❖ Importante: Existen Pokémon que tiene un solo tipo, como Blastoise que es solo de tipo Agua(water), y otros que tienen 2 tipos, como Charizard que es Fuego(fire) y Volador(flying). Para esta aplicación considere solo el primer tipo, es decir, para el caso de Charizard, solo tome que es Fuego.
❖ Si la función get_move entrega como valor 0 no se puede calcular el daño, se debe validar y solicitar al usuario que seleccione otro ataque.
