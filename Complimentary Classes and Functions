#!/usr/bin/env python

import time
import random

#Creating the basic level of sentient beings in the game


class being:

    def __init__(self, x, y, health, attack):
        self.x = x
        self.y = y
        self.health = health
        self.attack = attack


#Creating the player
class Player(being):
    
    def __init__(self):
        super().__init__(2, 0, 90, 0)
        #2,0
        self.key = 0
        self.armor = 0
        self.startup = 0
        self.dead = False
        self.content = None
        self.container = None
        self.count = 0

    #Defining the attack function, which the player will use
    def kill(self, h2):
        #A player has a base attack damage of x, and then every attack has a chance to attain bonus damage added to the base damage. The bonus damage is a random value between 1 and 15
        print()
        time.sleep(1.5)
        rand = random.randint(1, 15)
        hit = self.attack + rand
        h2.health = h2.health - hit
        if rand >= 10:
            print("CRITICAL STRIKE")
    

                
        if h2.health <= 0:
            print("You hit for", hit, "and the", h2.name, "dies. Congratulations, slayer.")
            h2.dead = True
        else:
            print("You damage the", h2.name, "for", hit, "!", "It has", h2.health, "health left.")
            print()
            time.sleep(1.5)
            print("It now attacks you!")
            print()
            time.sleep(1.5)
            rand = random.randint(1, 15)
            hit = h2.attack + rand
            
            if rand >= 10:
                print("CRITICAL STRIKE")
               
                
            self.health = self.health - hit
            if self.health < 0:
                print("The", h2.name, "hits you for", hit, "and you crumple to the ground.")
                self.dead = True
            else:
                print("It just hit you for", hit, "and you have", self.health, "health left.")


class Monster(object):
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        self.dead = False
