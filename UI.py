from PySide import QtGui
import maya.OpenMayaUI as mui
import shiboken

def getMayaWindow():
    pointer = mui.MQtUtil.mainWindow()
    return shiboken.wrapInstance(long(pointer), QtGui.QMainWindow)