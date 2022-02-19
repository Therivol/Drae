import os
import pygame as p
import json


class Controller:
    def __init__(self, game):
        self.game = game
        self.key_binds = self.game.settings.key_binds
        self.actions = {action: False for action in self.key_binds.values()}
        self.raw_keys = {}
        self.mouse_buttons = {}
        self.handled_keys = []
        self.handled_buttons = []

    def handle_events(self):
        for ev in p.event.get():
            if ev.type == p.QUIT:
                self.game.quit()

            if ev.type == p.VIDEORESIZE:
                self.game.window = p.display.set_mode((ev.w, ev.h), p.RESIZABLE)
                self.game.w_size = (ev.w, ev.h)

            if ev.type == p.KEYDOWN:
                self.set_key(ev.key)

            if ev.type == p.KEYUP:
                self.reset_key(ev.key)

            if ev.type == p.MOUSEBUTTONDOWN or p.MOUSEBUTTONUP:
                self.set_buttons()

    def reset(self):
        for action in self.actions:
            self.actions[action] = False

    def set_key(self, key):
        key_name = p.key.name(key)
        self.raw_keys[key_name] = True
        if key_name in self.key_binds.keys():
            self.actions[self.key_binds[key_name]] = True

    def reset_key(self, key):
        key_name = p.key.name(key)
        self.raw_keys[key_name] = False
        if key_name in self.handled_keys:
            self.handled_keys.remove(key_name)
        if key_name in self.key_binds.keys():
            self.actions[self.key_binds[key_name]] = False

    def set_buttons(self):
        presses = p.mouse.get_pressed()
        i = 1
        for press in presses:
            if press:
                self.mouse_buttons[str(i)] = True
            else:
                self.mouse_buttons[str(i)] = False
                if str(i) in self.handled_buttons:
                    self.handled_buttons.remove(str(i))
            i += 1

    def change_key_bind(self, action, key):
        self.key_binds[action] = key

    def get_key_down(self, key):
        if key in self.handled_keys:
            return False
        elif key in self.raw_keys.keys():
            if self.raw_keys[key]:
                self.handled_keys.append(key)
                return True
        return False

    def get_key(self, key):
        if key in self.raw_keys:
            return self.raw_keys[key]

    def get_action_down(self, action):
        act = self.actions[action]
        self.actions[action] = False
        return act

    def get_action(self, action):
        return self.actions[action]

    def get_button_down(self, button):
        if button in self.handled_buttons:
            return False
        elif button in self.mouse_buttons.keys():
            if self.mouse_buttons[button]:
                self.handled_buttons.append(button)
                return True
        return False

    def get_button(self, button):
        return self.mouse_buttons[button]

    def get_mouse_pos(self):
        return self.game.RES[0] * (p.mouse.get_pos()[0] / self.game.w_size[0]), \
               self.game.RES[1] * (p.mouse.get_pos()[1] / self.game.w_size[1])

    def get_mouse_scroll(self, scroll):
        non_scroll = self.get_mouse_pos()
        return non_scroll[0] + scroll[0], non_scroll[1] + scroll[1]

    def load_key_binds(self):
        with open(self.bind_path, "r") as open_file:
            return json.load(open_file)

    def save_key_binds(self):
        with open(self.bind_path, "w") as out_file:
            out_file.write(json.dumps(self.key_binds))
            out_file.close()

