import random,string
import pygame,math,sys
from pygame.math import Vector2
from .screen import gameScreen
from .utils import *
from enum import Enum,auto
from .animatedsprite import AnimatedSprite
from .statemachine import StateMachine
from .States.Task.idle import Idle
from .States.Task.active import Active
from .States.Task.completed import Completed

class Task(StateMachine,Enum):

    PLACEHOLDER = 'placeholder'
    FILLSOULBOX = 'fillSoulBox'
    PICKUPWEAPON = 'pickUpWeapon'
    PLACEWEAPON = 'placeWeapon'
    GOTOLOCATION = 'goToLocation'
    INTERACTWITHITEM = 'interactWithItem'
    

    def __init__(self,parentNodes:list=[],linkedNodes:list=[],targetValue=1,taskType:str='s',description:str='Complete this task.'):

        self.description = description
        self.parentNodes = parentNodes
        self.linkedNodes = linkedNodes
        self.taskType = taskType
        self.targetValue = targetValue
        self.currentValue = 0
        self.displayIcon = AnimatedSprite()

    def init(self):

        # init state machine
        self.states = {'IDLE':Idle(),
                       'ACTIVE':Active(),
                       'COMPLETED':Completed()}

        # set parent node for player states
        for x in self.states:
            self.states[x].parent_node = self
            self.states[x].timer_limit = self.stateTimeLimit[x]
        
        # pick state to start in
        self.state = self.states['IDLE']


    def update(self):

        if self.taskType == 'fill souls':

            
            pass
        pass

    # @property
    # def is_complete(self):

    #     if self.taskType is Task.FILLSOULBOX:
    #         pass

    #     return False
    #     pass

    def display_progress(self):
        pass

    # @property
    # def description(self):

    #     if self.taskType is Task.FILLSOULBOX:
    #         return  'Fill '

    def activate(self):
        pass

    def end_condition(self):

        if self.currentValue >= self.targetValue:
            self.done = True






class Quest():

    def __init__(self,parentNodes,prerequisites,rewards,tasks:dict={},description:str='Build Upgraded Weapon'):

        self.parentNodes = parentNodes
        self.tasks = tasks
        self.description = description
        self.prerequisites = prerequisites
        self.rewards = rewards
        self.displayIcon = AnimatedSprite()
        self.currentTask = 0

    def add_task(self,taskPosition:int,task:Task):

        self.tasks[taskPosition] = task
        pass

    def remove_task(self):
        pass

    def update_task(self):

        pass

    @property
    def get_current_task(self):
        pass


