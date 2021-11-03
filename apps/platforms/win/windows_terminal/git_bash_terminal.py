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
    def file_manager_open_parent():
        actions.insert("cd ..")
        actions.key("enter")

    def file_manager_current_path():
        path = ui.active_window().title
        #path = get_win_path(path)

        if path in directories_to_remap:
            path = directories_to_remap[title]

        if path in directories_to_exclude:
            path = ""
        return path

    def file_manager_show_properties():
        """Shows the properties for the file"""

    def file_manager_open_directory(path: str):
        """opens the directory that's already visible in the view"""
        actions.insert("cd ")
        path = '"{}"'.format(path)
        actions.insert(path)
        actions.key("enter")

    def file_manager_select_directory(path: str):
        """selects the directory"""
        actions.insert(path)

    def file_manager_new_folder(name: str):
        """Creates a new folder in a gui filemanager or inserts the command to do so for terminals"""
        #name = '"{}"'.format(name)

        actions.insert("mkdir " + name)

    def file_manager_open_file(path: str):
        """opens the file"""
        actions.insert(path)
        actions.key("enter")

    def file_manager_select_file(path: str):
        """selects the file"""
        actions.insert(path)

    def file_manager_open_volume(volume: str):
        """file_manager_open_volume"""
        actions.user.file_manager_open_directory(volume)

    def terminal_list_directories():
        actions.insert("ls ")
        #actions.key("enter")

    def terminal_list_all_directories():
        actions.insert("ls -a ")
        #actions.key("enter")

    def terminal_change_directory(path: str):
        actions.insert("cd {}".format(path))
        #if path:
        #    actions.key("enter")

    def terminal_change_directory_root():
        """Root of current drive"""
        actions.insert("cd /")
        actions.key("enter")

    def terminal_clear_screen():
        """Clear screen"""
        actions.key("ctrl-l")

    def terminal_run_last():
        actions.key("up enter")

    def terminal_kill_all():
        actions.key("ctrl-c")
        actions.insert("y")
        actions.key("enter")

    def terminal_print_working_directory():
        actions.insert("pwd")
        actions.key("enter")
