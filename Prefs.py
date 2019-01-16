import pymel.core as pmc


def print_grid():
    g_size = pmc.grid(q=True, size=True)
    g_spacing = pmc.grid(q=True, spacing=True)
    g_divisions = pmc.grid(q=True, divisions=True)

    print "size: " + str(g_size)
    print "spacing: " + str(g_spacing)
    print "divisions: " + str(g_divisions)


def get_grid():
    g_size = pmc.grid(q=True, size=True)
    g_spacing = pmc.grid(q=True, spacing=True)
    g_divisions = pmc.grid(q=True, divisions=True)
    return [g_size, g_spacing, g_divisions]


def set_unit(unit, near_clip, far_clip):
    pmc.currentUnit(linear=unit)
    pmc.setAttr('perspShape.nearClipPlane', near_clip)
    pmc.setAttr('perspShape.farClipPlane', far_clip)


def set_meters():
    g_props = get_grid()
    set_unit('m', 0.1, 1000.0)
    pmc.grid(size=g_props[0], spacing=g_props[1], divisions=g_props[2])


def set_centimeters():
    g_props = get_grid()
    set_unit('cm', 0.001, 10.0)
    pmc.grid(size=g_props[0], spacing=g_props[1], divisions=g_props[2])
