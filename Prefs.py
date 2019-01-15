import pymel.core as pmc


def set_meters():
    pmc.currentUnit(linear='meter')
    pmc.setAttr('perspShape.nearClipPlane', 0.1)
    pmc.setAttr('perspShape.farClipPlane', 1000.0)


def set_centimeters():
    pmc.currentUnit(linear='cm')
    pmc.setAttr('perspShape.nearClipPlane', 0.001)
    pmc.setAttr('perspShape.farClipPlane', 10.0)
