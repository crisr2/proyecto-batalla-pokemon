#Proyecto Batalla Pokémon - Programación Avanzada - Elaborado por Cristian Reyes

import random
import time

class IAttackBehaviour():
    """Interfaz para el comportamiento de un ataque de un Pokémon"""
    def attack(self):
        pass
 
class Pokemon:
    """Clase base de un Pokémon

    Atributos: 
    * name: Nombre del Pokémon
    * max_hp: Puntos de vida maximos
    * current_hp: Puntos de vida que tiene actualmente (Empieza en el maximo y cambia según los ataques recibidos)
    * attacks: Lista de ataques que tiene el Pokémon
    * fainted: Si el Pokémon ha sido derrotado (Inicia como False)"""
    def __init__(self, name, hp, attacks: list):
        self.name = name
        self.max_hp = hp
        self.current_hp = hp
        self.attacks = attacks
        self.fainted = False
    
    def do_attack(self, attack, opponent):
        """Función propia de la clase Pokémon para realizar un ataque a otro Pokémon

        Args:
            attack (IAttackBehaviour): El ataque seleccionado de la lista de ataques a realizar.
            opponent (Pokemon): El Pokémon del oponente, objetivo del ataque.
        """
        print(f'\n¡{self.name} usó {attack.atk_name}!')
        time.sleep(1.5)
        opponent.take_damage(attack) 

    def take_damage(self, attack):
        """Función propia de la clase Pokémon para calcular el daño recibido por un ataque.

        Args:
            attack (IAttackBehaviour): El ataque recibido realizado por otro Pokémon.
        """
        self.current_hp = max(0, self.current_hp - attack.damage)
        print(f'¡{self.name} tomó {attack.damage} puntos de daño!') 
        time.sleep(1)
        print(f'La salud de {self.name} ahora es de {self.current_hp} puntos de vida.')
        time.sleep(1)

    def check_faint_status(self):
        """Función propia de la clase Pokémon que indica si el Pokémon sigue con vida o fue derrotado.

        Returns:
            boolean: Regresa el atributo fainted que indica el estado de vida del Pokémon.
        """
        self.fainted = self.current_hp <= 0
        return self.fainted
    
#Comportamiento de los diferentes ataques que un Pokémon puede tener:
class Attack_Impactrueno(IAttackBehaviour):
    def __init__(self):
        self.atk_name = 'Impactrueno'
        self.damage = 35

class Attack_Rayo(IAttackBehaviour):
    def __init__(self):
        self.atk_name = 'Rayo'
        self.damage = 55
    
class Attack_Rapido(IAttackBehaviour):
    def __init__(self):
        self.atk_name = 'Ataque Rápido'
        self.damage = 20

class Attack_Placaje(IAttackBehaviour):
    def __init__(self):
        self.atk_name = 'Placaje'
        self.damage = 20

class Attack_Tacleada(IAttackBehaviour):
    def __init__(self):
        self.atk_name = 'Tacleada'
        self.damage = 30

class Attack_Supersonico(IAttackBehaviour):
    def __init__(self):
        self.atk_name = 'Supersónico'
        self.damage = 10

class Attack_Drenadoras(IAttackBehaviour):
    def __init__(self):
        self.atk_name = 'Drenadoras'
        self.damage = 10

class Attack_Picotazo(IAttackBehaviour):
    def __init__(self):
        self.atk_name = 'Picotazo'
        self.damage = 25

class Attack_Remolino(IAttackBehaviour):
    def __init__(self):
        self.atk_name = 'Remolino'
        self.damage = 10

class Attack_Tornado(IAttackBehaviour):
    def __init__(self):
        self.atk_name = 'Tornado'
        self.damage = 30

class Attack_LatigoCepa(IAttackBehaviour):
    def __init__(self):
        self.atk_name = 'Látigo Cepa'
        self.damage = 35

class Attack_Somnifero(IAttackBehaviour):
    def __init__(self):
        self.atk_name = 'Somnífero'
        self.damage = 5

class Attack_Lanzallamas(IAttackBehaviour):
    def __init__(self):
        self.atk_name = 'Lanzallamas'
        self.damage = 55

class Attack_Grunido(IAttackBehaviour):
    def __init__(self):
        self.atk_name = 'Gruñido'
        self.damage = 10

class Attack_Aranazo(IAttackBehaviour):
    def __init__(self):
        self.atk_name = 'Arañazo'
        self.damage = 30

class Attack_Ascuas(IAttackBehaviour):
    def __init__(self):
        self.atk_name = 'Ascuas'
        self.damage = 30

class Attack_PistolaAgua(IAttackBehaviour):
    def __init__(self):
        self.atk_name = 'Pistola Agua'
        self.damage = 30

class Attack_Burbuja(IAttackBehaviour):
    def __init__(self):
        self.atk_name = 'Burbuja'
        self.damage = 30

class Attack_RayoBurbuja(IAttackBehaviour):
    def __init__(self):
        self.atk_name = 'Rayo Burbuja'
        self.damage = 55

class Attack_TajoCruzado(IAttackBehaviour):
    def __init__(self):
        self.atk_name = 'Tajo Cruzado'
        self.damage = 70

class Attack_Hipercolmillo(IAttackBehaviour):
    def __init__(self):
        self.atk_name = 'Hipercolmillo'
        self.damage = 55

class Attack_GolpeCabeza(IAttackBehaviour):
    def __init__(self):
        self.atk_name = 'Golpe Cabeza'
        self.damage = 50

class Attack_Lodo(IAttackBehaviour):
    def __init__(self):
        self.atk_name = 'Lodo'
        self.damage = 35

class Attack_BombaLodo(IAttackBehaviour):
    def __init__(self):
        self.atk_name = 'Bomba Lodo'
        self.damage = 60

class Attack_Acido(IAttackBehaviour):
    def __init__(self):
        self.atk_name = 'Ataque Ácido'
        self.damage = 20

class Attack_Infortunio(IAttackBehaviour):
    def __init__(self):
        self.atk_name = 'Infortunio'
        self.damage = 45

class Attack_Hidropulso(IAttackBehaviour):
    def __init__(self):
        self.atk_name = 'Hidropulso'
        self.damage = 50

# Clases concretas de los diferentes Pokémon:
class Pikachu(Pokemon):
    def __init__(self):
        super().__init__("Pikachu",100,[Attack_Impactrueno(), Attack_Rayo(), Attack_Rapido(), Attack_Placaje()])

class Caterpie(Pokemon):
    def __init__(self):
        super().__init__("Caterpie",115,[Attack_Placaje(), Attack_Tacleada(), Attack_Supersonico(), Attack_Drenadoras()])

class Pidgeotto(Pokemon):
    def __init__(self):
        super().__init__("Pidgeotto",125,[Attack_Picotazo(), Attack_Remolino(), Attack_Tornado(), Attack_Rapido()])

class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__("Bulbasaur",115,[Attack_LatigoCepa(), Attack_Drenadoras(), Attack_Placaje(), Attack_Somnifero()])

class Charmander(Pokemon):
    def __init__(self):
        super().__init__("Charmander",110,[Attack_Lanzallamas(), Attack_Grunido(), Attack_Aranazo(), Attack_Ascuas()])

class Squirtle(Pokemon):
    def __init__(self):
        super().__init__("Squirtle",108,[Attack_PistolaAgua(), Attack_Burbuja(), Attack_Rapido(), Attack_Placaje()])

class Krabby(Pokemon):
    def __init__(self):
        super().__init__("Krabby",90,[Attack_Burbuja(), Attack_RayoBurbuja(), Attack_Placaje(), Attack_TajoCruzado()])

class Raticate(Pokemon):
    def __init__(self):
        super().__init__("Raticate",115,[Attack_Hipercolmillo(), Attack_Rapido(), Attack_Placaje(), Attack_GolpeCabeza()])

class Muk(Pokemon):
    def __init__(self):
        super().__init__("Muk",135,[Attack_Lodo(), Attack_BombaLodo(), Attack_Acido(), Attack_Infortunio()])

class Kingler(Pokemon):
    def __init__(self):
        super().__init__("Kingler",115,[Attack_Hidropulso(), Attack_RayoBurbuja(), Attack_Rayo(), Attack_Placaje()])

def PKMN_List():
    """ Función que regresa los valores de los diferentes Pokemon disponibles.

    Returns:
        list: Lista de todas las instancias de la clase Pokémon creadas.
    """
    return [Pikachu(),Caterpie(),Pidgeotto(),Bulbasaur(),Charmander(),Squirtle(),Krabby(),Raticate(),Muk(),Kingler()]

def select_pokemon(pokemon_list):
    """Función utilizada para seleccionar un Pokémon de la lista de todos los Pokémon para añadirlo al equipo del jugador.

    Args:
        pokemon_list (list): Lista de todos los Pokémon disponibles a seleccionar.

    Returns:
        Pokemon: Regresa el Pokémon seleccionado por el jugador.
    """
    time.sleep(0.5)
    print('Elige un Pokémon (Escribe su numero en consola):\n')
    time.sleep(0.8)
    for n in range(0,len(pokemon_list)):
        print(f'{n+1}. {pokemon_list[n].name}')
    try:
        index = int(input('\n-> '))
    except ValueError:
        print(f'\nEl número de Pokémon escrito no es un número valido, intenta de nuevo.')
        time.sleep(1)
        return select_pokemon(pokemon_list)

    if index in range(1,len(pokemon_list)+1):
        return pokemon_list[index-1]
    else:
        print(f'\nEl número de Pokémon escrito no esta en la lista, por favor intenta de nuevo.')
        time.sleep(1)
        return select_pokemon(pokemon_list)

class Player():
    """Clase base para un Jugador. 

    Atributos: 
    * name: Nombre del Jugador
    * pokemon: Lista de sus Pokémon 
    * is_cpu: Si es una CPU o no
    * all_pkmn_fainted: Si todos sus Pokémon fueron derrotados
    * out_pkmn: Cual de sus Pokémon esta peleando en el campo (Por predetermindo es el primero de la lista)"""
    def __init__(self, name, pokemon: list): 
        self.name = name
        self.pokemon = pokemon
        self.is_cpu = False
        self.all_pkmn_fainted = False
        self.out_pkmn = self.pokemon[0]

    def select_attack_pokemon(self,pkmn):
        """Función usada por el jugador para seleccionar un ataque de el Pokémon que esta afuera peleando en el campo.
        Args:
            pkmn (Pokemon): Pokemon del jugador que se encuentra peleando.

        Returns:
            IAttackbehaviour: Regresa el ataque del Pokémon seleccionado por el jugador.
        """
        print(f'\nLista de ataques de {pkmn.name}:')
        for idx, attack in enumerate(pkmn.attacks, start=1):
            print(f'{idx}. {attack.atk_name} ({attack.damage} puntos de daño)')

        while True:
            try:
                time.sleep(0.5)
                print(f'\nElige un ataque (1-{len(pkmn.attacks)})')
                attack_choice = int(input('-> '))
                if 1 <= attack_choice <= len(pkmn.attacks):
                    break
                else:
                    print('Selecciona un número válido.')
            except ValueError:
                print('Por favor, ingresa un número válido.')

        return pkmn.attacks[attack_choice-1]
    
    def switch_pokemon(self):
        """Funcion utilizada por el jugador para cambiar el Pokémon que esta peleando actualmente."""
        current_pkmn = self.out_pkmn
        while True:
            try:
                print(f'\nElige un Pokemon (1-{len(self.pokemon)})')
                pokemon_choice = int(input('-> '))
                time.sleep(0.8)
                if 1 <= pokemon_choice <= len(self.pokemon):
                    if current_pkmn == self.pokemon[pokemon_choice - 1]:
                        print(f'¡{current_pkmn.name} ya esta afuera!')
                        time.sleep(1.5)
                        continue
                    else:
                        break
                else:
                    print('Selecciona un número válido.')
            except ValueError:
                print('Por favor, ingresa un número válido.')

        self.out_pkmn = self.pokemon[pokemon_choice - 1]
        print(f'{current_pkmn.name} ha sido cambiado por {self.out_pkmn.name}')    
        time.sleep(0.8)  

def create_player():
    """
    Función para crear una instancia de la clase Player.

    Returns:
        Player: Regresa un objeto Player perteneciente a un jugador humano, con su equipo Pokémon seleccionado.
    """
    print('\n¿Cual es tu nombre?')
    player_name = input('-> ')
    time.sleep(0.5)
    while True:
        time.sleep(0.5)
        print('\n¿Con cuantos Pokémon quieres jugar? (1, 2, o 3)')
        pkmn_amount = input('-> ')
        if pkmn_amount in ['1','2','3']:
            time.sleep(0.5)
            print('\n¿Deseas seleccionar tu equipo manualmente (Escribe 1) o aleatoriamente (Escribe 2)?')
            pkmn_selection = input('-> ')
            if pkmn_selection in ['1','2']:
                time.sleep(1)
                break
            else:
                print('\nOpción invalida, por favor intentalo de nuevo.')
                time.sleep(0.5)
                continue
        else:
            print(f'\nLa cantidad seleccionada no es valida, intenta de nuevo.')
            time.sleep(0.5)

    chosen_pkmn = []
    if pkmn_selection == '1':
        for n in range(0,int(pkmn_amount)):
            print('')
            print(f'Selecciona tu Pokémon #{n+1}'.center(50, "-"))
            time.sleep(0.5)
            chosen_pkmn.append(select_pokemon(PKMN_List()))
            print(f'\n{player_name} ha seleccionado a {chosen_pkmn[n].name} como su Pokémon #{n+1}')
            time.sleep(1)
    else:
        for n in range(0,int(pkmn_amount)):
            chosen_pkmn.append(random.choice(PKMN_List()))

    return Player(player_name, chosen_pkmn)

def create_cpu_player(pkmn_amount):
    """
    Función para crear una instancia de la clase Player para un jugador controlado por la CPU.

    Args:
        pkmn_amount (str): Cantidad de Pokémon que el computador agrega a su equipo. Es la misma cantidad de Pokémon que la del equipo del jugador humano rival.

    Returns:
        Player: Regresa un objeto Player perteneciente a la computadora, con su equipo Pokémon seleccionado aleatoriamente.
    """
    pkmn_list = []
    for n in range(0,int(pkmn_amount)):
        pkmn_list.append(random.choice(PKMN_List()))
    cpu = Player('CPU', pkmn_list)
    cpu.is_cpu = True
    return cpu

def create_players_teams(game_mode):
    """Función encargada de la creación de los equipos de ambos jugadores, ya sean humanos o controlados por la maquina.

    Args:
        game_mode (str): Valor que representa el modo de juego seleccionado por el jugador, contra un jugador o contra la maquina.

    Returns:
        Player: Retorna los 2 jugadores 
    """
    if game_mode == '1':
        player1 = create_player()
        amount = len(player1.pokemon)
        player2 = create_cpu_player(amount)

    else:
        print(f'\nJugador 1:')
        player1 = create_player()
        print(f'\nJugador 2:')
        player2 = create_player()

    p1_pkmn_names = []
    p2_pkmn_names = []

    for n in range(0,int(len(player1.pokemon))):
        p1_pkmn_names.append(player1.pokemon[n].name)

    for n in range(0,int(len(player2.pokemon))):
        p2_pkmn_names.append(player2.pokemon[n].name)

    print(f'\nPokémon de {player1.name}: {p1_pkmn_names}')
    time.sleep(0.5)
    print(f'Pokémon de {player2.name}: {p2_pkmn_names}\n')
    time.sleep(1.5)

    return player1,player2

def turn(player,rival):
    """Función que controla las opciones que pueden ocurrir dentro del turno de batalla de un jugador humano.

    Args:
        player (Player): Jugador humano quien tiene el turno y selecciona entre atacar o cambiar de Pokémon.
        rival (Player): Jugador humano o CPU que es el objetivo de los ataques del jugador que tiene el turno.
    """
    current_pokemon = player.out_pkmn
    turn_action_choice = ''

    print(f'\nEs el turno de {player.name}.\n')
    time.sleep(1)
    print(f'Lista de Pokémon de {player.name}:')
    for idx, pokemon in enumerate(player.pokemon, start=1):
        print(f'{idx}. {pokemon.name} ({pokemon.current_hp}/{pokemon.max_hp} HP)')
    while True:
        if len(player.pokemon) == 1:
            time.sleep(1)
            turn_action_choice = '1'
            break

        time.sleep(0.5)
        print(f'\nTu Pokémon en el campo es {current_pokemon.name}.\n ¿Atacar (1) o cambiar de Pókemon (2)?')
        turn_action_choice = input('-> ')
        if turn_action_choice in ['1','2']:
            time.sleep(1)
            break
        else:
            print('\nOpción invalida, por favor intentalo de nuevo.')
            time.sleep(0.5)

    if turn_action_choice == '1':
        attack = player.select_attack_pokemon(current_pokemon) 
        current_pokemon.do_attack(attack, rival.out_pkmn)
    else:
        player.switch_pokemon()

def cpu_turn(cpu,player):
    """Función que controla las opciones que ocurren en el turno de un jugador CPU.

    Args:
        cpu (Player): El jugador CPU que tiene el turno y escoge aleatoriamente entre atacar o cambiar el Pokémon que tiene afuera.
        player (Player): El jugador humano que recibe los ataques aleatorios del jugador CPU.
    """
    current_pokemon = cpu.out_pkmn
    print(f'\nEs el turno de la CPU.\n')
    time.sleep(1)
    turn_action_choice = ''

    if len(cpu.pokemon) == 1:
        turn_action_choice = '1'
    else:
        turn_action_choice = random.choice(['1','1','1','1','1','1','1','1','2','2'])

    if turn_action_choice == '1':
        print('¡CPU ataca!')
        random_attack = random.choice(current_pokemon.attacks)
        current_pokemon.do_attack(random_attack, player.out_pkmn)

    else:
        print('¡CPU eligio cambiar de Pokémon!')
        while True:
            new_pkmn_idx = random.choice(range(0,len(cpu.pokemon)))
            if current_pokemon != cpu.pokemon[new_pkmn_idx - 1]:
                break
        cpu.out_pkmn = cpu.pokemon[new_pkmn_idx - 1]
        print(f'{current_pokemon.name} ha sido cambiado por {cpu.out_pkmn.name}')       

def check_win_condition(player, opponent):
    """Función que evalua si las condiciones de victoria y derrota se cumplen entre la batalla de ambos jugadores.

    Args:
        player (Player): Jugador que tiene el turno quien se verifica si ha ganado.
        opponent (Player): Jugador oponente que se verifica si ha perdido.

    Returns:
        boolean: Regresa el atributo del jugador oponente que indica si todos su Pokémon han sido derrotados o no.
    """
    if len(opponent.pokemon) == 0:
        opponent.all_pkmn_fainted = True
        print(f'¡{opponent.name} no tiene más Pokémon!\n')
        time.sleep(0.8)
        print(f'¡{player.name} gana la batalla!'.center(50,'/'))
        
    return opponent.all_pkmn_fainted
    
def battle(player1, player2):
    """Función que inicia una batalla Pokémon entre dos jugadores y remueve los Pokémon que son derrotados.

    Args:
        player1 (Player): Jugador 1 que tiene el turno.
        player2 (Player): Jugador 2 oponente a quien se revisa el estado de su Pokémon que esta peleando.
    """
    print(f'¡{player1.name} VS {player2.name}!'.center(50,'/'))
    time.sleep(1)
    while not player1.all_pkmn_fainted and not player2.all_pkmn_fainted:
        if player1.is_cpu:
            cpu_turn(player1,player2)
        else:
            turn(player1, player2)

        if player2.out_pkmn.check_faint_status():
            player2.pokemon.remove(player2.out_pkmn)
            print(f'\nEl {player2.out_pkmn.name} de {player2.name} ha sido derrotado.')
            time.sleep(0.8)
            if not check_win_condition(player1,player2):
                player2.out_pkmn = player2.pokemon[0]

        player1, player2 = player2, player1
        
def start_menu():
    """Función que da forma al menú de inicio del programa."""

    print('\033[1m' +'¡Bienvenido al Simulador de Batallas Pokémon!'.center(70,'#'))
    print('\033[0m')
    while True:
        time.sleep(1)
        print('Selecciona el número del modo de juego que deseas jugar: \n\n1. Jugador Contra la Maquina \n2. Jugador Contra Jugador\n')
        game_mode = input(f'-> ')
        print('')
        if game_mode in ['1','2']:
            break
        else:
            print(f'El modo seleccionado no es valido, intenta de nuevo.\n')

    if game_mode == '1':
        time.sleep(0.5)
        print('BATALLA JUGADOR CONTRA LA MAQUINA'.center(50, "="))
        time.sleep(0.5)
        human_player, cpu_player = create_players_teams(game_mode)
        battle(human_player,cpu_player)

    else:
        time.sleep(0.5)
        print('BATALLA JUGADOR CONTRA JUGADOR'.center(50, "="))
        time.sleep(0.5)
        player1, player2 = create_players_teams(game_mode)
        battle(player1,player2)

    while True:
        time.sleep(1.5)
        print('\n¿Combatir de nuevo (1) o salir del programa (2)?')
        restart = input('-> ')
        if restart in ['1','2']:
            break
        else:
            print(f'La opción seleccionada no es valida, intenta de nuevo.\n')
    if restart == '1':
        start_menu()
    else:
        time.sleep(0.5)
        print('\n¡Gracias por jugar!\n')
        quit()

# Ejecución del programa de batallas Pokémon:
if __name__ == "__main__":
    start_menu()