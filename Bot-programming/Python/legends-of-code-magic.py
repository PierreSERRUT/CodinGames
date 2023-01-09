#legends-of-code-magic
#https://www.codingame.com/ide/puzzle/legends-of-code-magic
#python
import sys
import math

def debug(var_name, var):
    print(var_name, var, file=sys.stderr, flush=True)

class Player:
    def __init__(self, hp, mana, deck, rune, draw ):
        self.hp = hp
        self.mana = mana
        self.deck = deck
        self.rune = rune
        self.draw = draw


class Card:
    def __init__(self, id, instance_id, location, card_type, cost, attack, defense, abilities, hp_change, hp_change_enemy,card_draw):
        self.id = id
        self.instance_id = instance_id
        self.location = location
        self.card_type = card_type
        self.cost = cost
        self.attack = attack
        self.defense = defense
        self.abilities = abilities
        self.hp_change = hp_change
        self.hp_change_enemy = hp_change_enemy
        self.card_draw = card_draw

class Guard:
    def __init__(self, id ,defense):
        self.id=id
        self.defense=defense

class Pick_Card:
    def __init__(self, index, id, cost, attack, defense):
        self.index=index
        self.id=id
        self.cost=cost
        self.attack=attack
        self.defense=defense

phase=0
mana_max=0
guards=[]
#abilities: 
#B-----
#-C----
#---G--

while True:
    cards = []  
    players = []
    guards=[]
    picks=[]

    for i in range(2):
        player_health, player_mana, player_deck, player_rune, player_draw = [int(j) for j in input().split()]
        players.append(Player(player_health, player_mana, player_deck, player_rune, player_draw))
    opponent_hand, opponent_actions = [int(i) for i in input().split()]

    for i in range(opponent_actions):
        card_number_and_action = input()
    card_count = int(input())
    for i in range(card_count):      
        inputs = input().split()
        card_number = int(inputs[0])
        instance_id = int(inputs[1])
        location = int(inputs[2])
        card_type = int(inputs[3])
        cost = int(inputs[4])
        attack = int(inputs[5])
        defense = int(inputs[6])
        abilities = inputs[7]
        my_health_change = int(inputs[8])
        opponent_health_change = int(inputs[9])
        card_draw = int(inputs[10])
        cards.append(Card(card_number,instance_id,location,card_type,cost,attack,defense,abilities,my_health_change,opponent_health_change,card_draw))
    
    if (players[0].mana == 0):
        #phase de pick pour l'instant full PICK 1 // A changer dans le futur
        debug("phase:","Draft")
        print("PICK 1")
    else:  
        #phase combat
        mana_max=players[0].mana
        mana_left=mana_max
        action=''
        np_action=0
        
        #trie par defense
        cards.sort(key=lambda x: x.defense, reverse=True)
        #ajout des guards
        for i in range(card_count):
            if cards[i].location == -1 and cards[i].abilities == '---G--':
                guards.append(Guard(cards[i].instance_id,cards[i].defense))

        #trie par attack
        cards.sort(key=lambda x: x.attack, reverse=True)
        
        #attaque guard plus grosse def en premier
        #puis adversaire direct
        for i in range(card_count):
            if cards[i].location == 1:
                g_len=len(guards)
                if g_len >= 1:
                    action = action + 'ATTACK '+ str(cards[i].instance_id)+' '+ str(guards[0].id) +';'
                    if cards[i].attack > guards[0].defense:
                        guards.pop(0)
                    else:
                        guards[0].defense-=cards[i].attack
                else:
                    action = action + 'ATTACK '+ str(cards[i].instance_id)+' -1 ;'
        
        debug("action:",action)

        #invoque de tous en priorité les gros couts
        cards.sort(key=lambda x: x.cost, reverse=True)
        
        while np_action==0:
            debug('while','')
            max_cost=Pick_Card(-1,-1,-1,-1,-1)
            #for toutes les cartes
            for i in range(card_count):
                #debug("card cost (i):",cards[i].cost)
                #debug("card id (i):",cards[i].instance_id)
                if cards[i].cost > max_cost.cost and cards[i].cost <= mana_left and cards[i].location == 0: 
                    max_cost.index=i
                    max_cost.id=cards[i].instance_id
                    max_cost.cost=cards[i].cost
            debug("max cost:",max_cost.cost)
            if max_cost.index >=0:
                mana_left-=max_cost.cost
                action = action + 'SUMMON '+ str(max_cost.id)+';'
                cards.pop(max_cost.index)
                card_count-=1
            else:
                np_action=1
            debug('mana left:',mana_left)
            debug("action:",action)
        #fin while     
            
        print(action)
    debug("card count",card_count)
    
