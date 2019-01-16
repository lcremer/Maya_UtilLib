import pymel.core as pmc


def distance_to_scene_units(distance):
    """
    This converts the distance dimension distance output to scene units
    It doesn't seem like maya does this and the default distance unit is in centimeters
    """
    unit = pmc.currentUnit(q=True)

    # Chose not to use convertUnit(value, fromUnit, toUnit) because it returns suffix in string
    # millimeters
    if unit == 'mm':
        return distance * 10
    # centimeters
    if unit == 'cm':
        return distance
    # meters
    if unit == 'm':
        return distance / 100
    # inch
    if unit == 'in':
        return distance / 2.54
    # foot
    if unit == 'ft':
        return distance / 30.48
    # yard
    if unit == 'yd':
        return distance / 91.44


def conversion_factor():
    unit = pmc.currentUnit(q=True)
    if unit == 'mm':
        return 10
    # centimeters
    if unit == 'cm':
        return 1
    # meters
    if unit == 'm':
        return .01
    # inch
    if unit == 'in':
        return 1 / 2.54
    # foot
    if unit == 'ft':
        return 1 / 30.48
    # yard
    if unit == 'yd':
        return 1 / 91.44
