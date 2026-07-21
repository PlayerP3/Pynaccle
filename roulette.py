from pynaccle.utils import *
import json
from pynaccle.moveableobject import Moveable_Object
from pynaccle.interactable import Interactable
from .States.Roulette.cycling import Cycling
from .States.Roulette.display import Display
from .States.Roulette.reset import Reset
from .States.Roulette.idle import Idle
import sys
from .tilemap import tilemapProcessor
from .objectsystem import objectManager
from .pathfinding import *
from .animatedsprite import AnimatedSprite


class Roulette(Interactable):

    def __init__(self,options:list=[],idleInteractTimerLimit:float=0.4,displayInteractTimerLimit:float=0.4):

        
        # get options  i.e what it cycles through
        self.options = options
        self.filteredOptions = options
        
        # variables that are constant and do not change
        self.idleInteractTimerLimit = idleInteractTimerLimit
        self.displayInteractTimerLimit = displayInteractTimerLimit

        # obj that first interacted with the roulette oj
        self.purchasingObj = None

        # get item display object
        self.displayItem = AnimatedSprite()
        self.finalDisplay = None

        Interactable.__init__(self)
        
        self.displayItem.zlayer_drawing = self.zlayer_drawing + 1
        


    def init(self):

        super().init()

        # set states
        # init state machine
        self.states = {'IDLE':Idle(),
                       'CYCLING':Cycling(),
                       'DISPLAY':Display(),
                       'RESET':Reset()
                       }
        
        # set new vars for certain states
        self.states['CYCLING'].timer_limit = 12
        self.states['DISPLAY'].timer_limit = 8
        
        # set animation player to not replay
        self.animationPlayer.timer_replay = False

        
        # set parent node for player states
        for x in self.states:
            self.states[x].parent_node = self
        
        self.state = self.states['IDLE']
        # self.state.enter()

        

    # what happens when pickup is done like changing stats etc
    def pay(self,gameobj):

        if gameobj.money >= self.cost:

            gameobj.money -= self.cost

            # give item
            self.give_item(gameobj=self.interactingObj)


    # swap weapon function
    def give_item(self,gameobj):
        pass

        # # first end weapon state
        # gameobj.weapon.state.completed()

        # # find first element in list which is current weapon
        # current_weapon = gameobj.allWeapons[0]
        
        # # set weapon to give to player
        # weapon_to_give = self.buildableObject

        # if len(gameobj.allWeapons) < gameobj.weaponCarryLimit:

        #     # remove current weapon and add to end of list
        #     gameobj.allWeapons.insert(0,weapon_to_give)


        # elif len(gameobj.allWeapons) >= gameobj.weaponCarryLimit:

        #     # remove current weapon and add to end of list
        #     gameobj.allWeapons.remove(current_weapon)
        #     gameobj.allWeapons.insert(0,weapon_to_give)

        # # set new weapon
        # gameobj.weapon = guns[weapon_to_give]
        # gameobj.weapon.wielded_by = gameobj

        # # enter state
        # gameobj.weapon.state = gameobj.weapon.states['PICKUP']
        # gameobj.weapon.state.enter()

    # swap weapon function
    # def remove_item(self,gameobj):

    #     # first end weapon state
    #     gameobj.weapon.state.completed()

    #     # find first element in list which is current weapon
    #     next_weapon = gameobj.allWeapons[1]
        
    #     # set weapon to give to player
    #     weapon_to_remove = self.buildableObject

    #     # remove weapon
    #     gameobj.allWeapons.remove(weapon_to_remove)

    #     # set new weapon
    #     gameobj.weapon = guns[next_weapon]
    #     gameobj.weapon.wielded_by = gameobj

    #     # enter state
    #     gameobj.weapon.state = gameobj.weapon.states['PULLOUT']
    #     gameobj.weapon.state.enter()

    # collision check
    def collision_check(self,axis:str='y'):

        self.state.collision_check()
        pass

    def handle_collision(self,axis:str='y'):

        self.state.handle_collision()
        pass

    def update_data(self):

        self.update_position()


    # function to get the images we cycle through
    def filter_cycle_options(self):

        pass

    # function to control how the display item acts during cycling
    def update_display_item(self):

        pass

    

    # pick the final result based on the options
    def choose_final_display(self):

        pass
            



    
