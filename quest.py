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


class Tasks(Enum):
    
    PLACEHOLDER = 'placeholder'
    FILLSOULBOX = 'fillSoulBox'
    PICKUPWEAPON = 'pickUpWeapon'
    PLACEWEAPON = 'placeWeapon'
    GOTOLOCATION = 'goToLocation'
    INTERACTWITHITEM = 'interactWithItem'
    


class Task(StateMachine):

    def __init__(self,parentNodes:list=[],linkedNodes:list=[],targetValue=1,taskType:str='placeholder',description:str='Complete this task.'):

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
        pass

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
            
    # set parent nodes
    def add_parent_nodes(self,nodes):
        
        if isinstance(nodes,list):
            self.parentNodes.extend(nodes)
            
        else:
            self.parentNodes.append(nodes)
            
    # set linked nodes
    def add_linked_nodes(self,nodes):
        
        if isinstance(nodes,list):
            self.linkedNodes.extend(nodes)
            
        else:
            self.linkedNodes.append(nodes)

    # set target value
    def set_target_value(self,value:float):
        
        self.targetValue = value
        
    # set description
    def set_description(self,value:str):
        
        self.description = value



class Quest():

    def __init__(self,parentNodes=[],prerequisites=[],rewards=[],tasks:dict={},followOrder:bool=False,description:str='Description goes here.'):

        self.parentNodes = parentNodes
        self.tasks = tasks
        self.description = description
        self.prerequisites = prerequisites
        self.rewards = rewards
        self.followOrder = followOrder
        self.displayIcon = AnimatedSprite()
        self.currentTask = 0
        

    def add_task(self,taskPosition:int,task:Tasks):

        self.tasks[taskPosition] = task
       

    def remove_task(self,taskPosition:int):
        
        del self.tasks[taskPosition]
        

    def update_tasks(self):
        
        # if we are following an order than we just run the current one
        if self.followOrder:
            self.tasks[self.currentTask].update()
    
    # set description
    def set_description(self,value:str):
        
        self.description = value

    @property
    def get_current_task(self):
        pass

