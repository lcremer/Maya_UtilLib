from PySide2 import QtWidgets
import maya.OpenMayaUI as mui
import shiboken2


def getMayaWindow():
    pointer = mui.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(long(pointer), QtWidgets.QMainWindow)
