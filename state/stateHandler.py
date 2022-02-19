import os
from os.path import exists
import pygame as p
import pickle


class StateHandler:
    def __init__(self, state):
        self.stack = []
        self.prev_state = None
        self.current = None
        self.enter_state(state)

    def enter_state(self, state):
        self.stack.append(state)
        self.current = state
        print(state.name)

    def exit_state(self):
        self.current.save()
        self.stack.pop()
        self.current = self.stack[-1]
        print(self.current.name)

    def exit_all(self):
        while len(self.stack) > 1:
            self.exit_state()
