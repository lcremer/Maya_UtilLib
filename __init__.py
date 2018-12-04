import os
import sys
import Maya_UtilLib.Easing
import Maya_UtilLib.VMath
import pymel.core as pm
from functools import partial
from PySide2 import QtWidgets as widgets

ui_name = "LeoTools"
ui_title = "Leo's Tools"


def main_window():
    for widget in widgets.qApp.topLevelWidgets():
        if widget.objectName() == 'MayaWindow':
            return widget
    # TODO: figure out why this isnt working
    #raise MessageException('QT Main window could not be detected')


def get_module_path(name='Maya_UtilLib'):
    module = __import__(name, globals(), locals(), ["*"], -1)
    path = module.__path__[0]
    return path


def remove_module(name):
    print('info', 'Removing {} module'.format(name))

    to_delete = []
    for m in sys.modules:
        if m.split('.')[0] == name:
            to_delete.append(m)

    for m in to_delete:
        del (sys.modules[m])


def remove_all_modules():
    remove_module('Maya_Rigging')
    remove_module('Maya_VertexColor')
    #remove_module('Maya_UtilLib')

    try:
        import Maya_Rigging
        import Maya_VertexColor
    except:
        pass


class MenuSingleton:
    class __MenuSingleton:
        def __init__(self):
            self.Modules = []
            self.ModuleMenusFunc = []

        def add(self, module, menu_func):
            if module in self.Modules:
                return
            if menu_func in self.ModuleMenusFunc:
                return
            self.Modules.append(module)
            self.ModuleMenusFunc.append(menu_func)

        def draw_module_menus(self):
            for drawFunc in self.ModuleMenusFunc:
                drawFunc()

    instance = None

    def __init__(self):
        if not MenuSingleton.instance:
            MenuSingleton.instance = MenuSingleton.__MenuSingleton()

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def add_module_menu(self, module, menu_func):
        # type: (str, function) -> None
        self.instance.add(module, menu_func)

    def reload_all(self, *args):
        self.instance.Reload()

    @staticmethod
    def remove_all(self):
        remove_all_modules()

    @staticmethod
    def kill(self):
        i = os.getpid()
        os.system("taskkill /PID " + str(i) + " /f")

    def draw(self):
        if pm.menu(ui_name, exists=1):
            pm.deleteUI(ui_name)
        tool_box_m = pm.menu(ui_name, p='MayaWindow', tearOff=1, allowOptionBoxes=1, label=ui_title)

        self.instance.draw_module_menus()

        pm.setParent(tool_box_m, menu=True)
        pm.menuItem(label="Reset", command=partial(self.remove_all))
        pm.menuItem(label="Kill Maya", command=partial(self.kill))


Menu = MenuSingleton()
