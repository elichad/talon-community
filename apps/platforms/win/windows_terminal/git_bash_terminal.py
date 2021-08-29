from talon import Context, Module, actions, imgui, settings, ui, app

import os

ctx = Context()
mod = Module()
mod.apps.git_bash_terminal = """
os: windows
and app.name: Visual Studio Code
os: windows
and app.exe: Code.exe
os: windows
and app.name: Git Bash
os: windows
and app.exe: git-bash.exe
os: windows
and app.exe: mintty.exe
"""
ctx.matches = r"""
app: git_bash_terminal
"""

user_path = os.path.expanduser("~")
directories_to_remap = {}
directories_to_exclude = {}

@ctx.action_class('edit')
class EditActions:
    def paste(): actions.key('shift-insert')
    def copy():  actions.key('ctrl-insert')

@ctx.action_class("user")
class UserActions:
    def stuff():
        pass