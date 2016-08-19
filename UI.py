from functools import partial
import pymel.core as pm
from PySide import QtGui
import maya.OpenMayaUI as mui
import shiboken

try:
    import Maya_Rigging as Rigging
except:
    pass

try:
    import Maya_VertexColor as VertexColor
except:
    pass


def getMayaWindow():
    pointer = mui.MQtUtil.mainWindow()
    return shiboken.wrapInstance(long(pointer), QtGui.QMainWindow)

def MainMenu():
    if pm.menu('ToolBox', exists=1):
        pm.deleteUI('ToolBox')
    toolBoxM = pm.menu('ToolBox', p='MayaWindow', tearOff=1, allowOptionBoxes=1, label='ToolBox')

    # Rigging Tools
    RiggingMenu()

    # Misc Tools
    MiscMenu()


def RiggingMenu():
    try:
        riggingM = pm.menuItem(parent='ToolBox', subMenu=True, tearOff=True, label='Rigging')
        pm.menuItem(label='Auto Rig', command=partial(Rigging.UI.AutoRig.Open))
    except:
        pass


def MiscMenu():
    try:
        miscM = pm.menuItem(parent='ToolBox', subMenu=True, tearOff=True, label='Misc')
        pm.menuItem(label='Vertex Color', command=partial(VertexColor.Gradient.UI.Open))
    except:
        pass
