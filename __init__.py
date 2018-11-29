import os
import sys
import Maya_UtilLib.UI
import Maya_UtilLib.Easing
import Maya_UtilLib.VMath
import pymel.core as pm
from functools import partial


def ReloadAll():
    ReloadModule('Maya_Rigging')
    ReloadModule('Maya_VertexColor')
    ReloadModule('Maya_UtilLib')


def ReloadModule(name="Maya_UtilLib", *args):
    module = __import__(name, globals(), locals(), ["*"], -1)
    path = module.__path__[0]
    __reloadRecursive(path, name)


def __reloadRecursive(path, parentName):
    for root, dirs, files in os.walk(path, True, None):
        # parse all the files of given path and reload python modules
        for sfile in files:
            if sfile.endswith(".py"):
                if sfile == "__init__.py":
                    name = parentName
                else:
                    name = parentName+"."+sfile[:-3]

                try:
                    module = __import__(name, globals(), locals(), ["*"], -1)
                    reload(module)
                except ImportError, e:
                    for arg in e.args:
                        sys.stdout.write('ImportError: ' + arg)
                except Exception, e:
                    for arg in e.args:
                        sys.stdout.write('Exception: ' + arg)

        # Now reload sub modules
        for dirName in dirs:
            __reloadRecursive(path+"/"+dirName, parentName+"."+dirName)
        break


class MenuSingleton:
    class __MenuSingleton:
        def __init__(self):
            self.Modules = []
            self.ModuleMenusFunc = []

        def Add(self, module, menuFunc):
            if module in self.Modules:
                return
            if menuFunc in self.ModuleMenusFunc:
                return
            self.Modules.append(module)
            self.ModuleMenusFunc.append(menuFunc)

        def Reload(self):
            for m in self.Modules:
                ReloadModule(name=m)

        def DrawModuleMenus(self):
            for drawFunc in self.ModuleMenusFunc:
                drawFunc()

    instance = None

    def __init__(self):
        if not MenuSingleton.instance:
            MenuSingleton.instance = MenuSingleton.__MenuSingleton()

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def AddModuleMenu(self, module, menuFunc):
        self.instance.Add(module, menuFunc)

    def ReloadAll(self, *args):
        self.instance.Reload()

    def Draw(self):
        if pm.menu('CustomTools', exists=1):
            pm.deleteUI('CustomTools')
        toolBoxM = pm.menu('CustomTools', p='MayaWindow', tearOff=1, allowOptionBoxes=1, label='Custom Tools')

        self.instance.DrawModuleMenus()

        pm.setParent(toolBoxM, menu=True)
        pm.menuItem(label="Reload", command=partial(self.ReloadAll))


Menu = MenuSingleton()
