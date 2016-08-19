from functools import partial
import pymel.core as pm
from PySide import QtGui
import maya.OpenMayaUI as mui
import shiboken


def getMayaWindow():
    pointer = mui.MQtUtil.mainWindow()
    return shiboken.wrapInstance(long(pointer), QtGui.QMainWindow)


def MainMenu():
    if pm.menu('CustomTools', exists=1):
        pm.deleteUI('CustomTools')
    toolBoxM = pm.menu('CustomTools', p='MayaWindow', tearOff=1, allowOptionBoxes=1, label='Custom Tools')

    # Rigging Tools
    try:
        import Maya_Rigging
        riggingM = pm.menuItem(parent='CustomTools', subMenu=True, tearOff=True, label='Rigging')
        pm.menuItem(label='Auto Rig', command=partial(Maya_Rigging.UI.AutoRig.Open))
    except:
        print('failed to import Maya_Rigging')
        pass

    # Misc Tools
    try:
        import Maya_VertexColor
        miscM = pm.menuItem(parent='CustomTools', subMenu=True, tearOff=True, label='Misc')
        pm.menuItem(label='Vertex Color', command=partial(Maya_VertexColor.Gradient.UI.Open))
    except:
        print('failed to import Maya_VertexColor')
        pass