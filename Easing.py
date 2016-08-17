import math


def Linear(numerator, denominator=1.0, start=0.0, end=1.0):
    return end * (numerator/denominator) + start


# Sin Easing
def SinIn(numerator, denominator=1.0, start=0.0, end=1.0):
    return -end * math.cos(numerator / denominator * (math.pi / 2)) + end + start


def SinOut(numerator, denominator=1.0, start=0.0, end=1.0):
    return end * math.sin(numerator / denominator * (math.pi / 2)) + start


def SinInOut(numerator, denominator=1.0, start=0.0, end=1.0):
    return -end / 2 * (math.cos(math.pi * numerator / denominator) - 1) + start


# Quadratic Easing
def QuadraticIn(numerator, denominator=1.0, start=0.0, end=1.0):
    return end * math.pow(numerator/denominator, 2) + start


def QuadraticOut(numerator, denominator=1.0, start=0.0, end=1.0):
    return -end * (numerator / denominator) * (numerator / denominator - 2) + start


def QuadraticInOut(numerator, denominator=1.0, start=0.0, end=1.0):
    numerator /= (denominator / 2)
    # if numerator < 1: return end / 2 * math.pow(numerator,2) + start
    if numerator < 1:
        return end / 2 * numerator * numerator + start
    numerator -= 1
    return -end / 2 * (numerator * (numerator - 2) - 1) + start


# Cubic Easing
def CubicIn(numerator, denominator=1.0, start=0.0, end=1.0):
    return end * math.pow(numerator / denominator, 3) + start


def CubicOut(numerator, denominator=1.0, start=0.0, end=1.0):
    return end * (math.pow(numerator / denominator - 1, 3) + 1) + start


def CubicInOut(numerator, denominator=1.0, start=0.0, end=1.0):
    numerator /= (denominator / 2)
    if numerator < 1:
        return end / 2 * math.pow(numerator, 3) + start
    numerator -= 2
    return end / 2 * (math.pow(numerator, 3) + 2) + start


# Quartic Easing
def QuarticIn(numerator, denominator=1.0, start=0.0, end=1.0):
    return end * math.pow(numerator/denominator, 4) + start


def QuarticOut(numerator, denominator=1.0, start=0.0, end=1.0):
    return -end * (math.pow(numerator / denominator - 1, 4) - 1) + start


def QuarticInOut(numerator, denominator=1.0, start=0.0, end=1.0):
    numerator /= (denominator / 2)
    if numerator < 1:
        return end / 2 * math.pow(numerator, 4) + start
    numerator -= 2
    return -end / 2 * (math.pow(numerator, 4) - 2) + start


# Quintic Easing
def QuinticIn(numerator, denominator=1.0, start=0.0, end=1.0):
    return end * math.pow(numerator/denominator, 5) + start


def QuinticOut(numerator, denominator=1.0, start=0.0, end=1.0):
    return end * (math.pow(numerator / denominator - 1, 5) + 1) + start


def QuinticInOut(numerator, denominator=1.0, start=0.0, end=1.0):
    numerator /= (denominator / 2)
    if numerator < 1:
        return end / 2 * math.pow(numerator, 5) + start
    numerator -= 2
    return end / 2 * (math.pow(numerator, 5) + 2) + start


# Exponential
def ExponentialIn(numerator, denominator=1.0, start=0.0, end=1.0):
    if numerator == 0:
        return start
    return end * math.pow(2, 10 * (numerator / denominator - 1)) + start


def ExponentialOut(numerator, denominator=1.0, start=0.0, end=1.0):
    if numerator == denominator:
        return start + end
    return end * (-math.pow(2, -10 * numerator / denominator) + 1) + start


def ExponentialInOut(numerator, denominator=1.0, start=0.0, end=1.0):
    if numerator == 0:
        return start
    elif numerator == denominator:
        return start + end
    numerator /= denominator / 2
    if numerator < 1:
        return end / 2 * math.pow(2, 10 * (numerator - 1)) + start
    else:
        return end / 2 * (-math.pow(2, -10 * (numerator-1)) + 2) + start


# Circular
def CircularIn(numerator, denominator=1.0, start=0.0, end=1.0):
    return -end * (math.sqrt(1 - math.pow(numerator/denominator, 2)) - 1) + start


def CircularOut(numerator, denominator=1.0, start=0.0, end=1.0):
    return end * math.sqrt(1 - math.pow(numerator/denominator - 1, 2)) + start


def EasingList():
    return ['Linear',
            # Sin
            'SinIn',
            'SinOut',
            'SinInOut',
            # Quadratic
            'QuadraticIn',
            'QuadraticOut',
            'QuadraticInOut',
            # Cubic
            'CubicIn',
            'CubicOut',
            'CubicInOut',
            # Quartic
            'QuarticIn',
            'QuarticOut',
            'QuarticInOut',
            # Quintic
            'QuinticIn',
            'QuinticOut',
            'QuinticInOut',
            # Exponential
            'ExponentialIn',
            'ExponentialOut',
            'ExponentialInOut'
            # Circular
            'CircularIn',
            'CircularOut']


def EasingDictionary():
    return {
            'Linear': Linear,
            # Sin
            'SinIn': SinIn,
            'SinOut': SinOut,
            'SinInOut': SinInOut,
            # Quadratic
            'QuadraticIn': QuadraticIn,
            'QuadraticOut': QuadraticOut,
            'QuadraticInOut': QuadraticInOut,
            # Cubic
            'CubicIn': CubicIn,
            'CubicOut': CubicOut,
            'CubicInOut': CubicInOut,
            # Quartic
            'QuarticIn': QuarticIn,
            'QuarticOut': QuarticOut,
            'QuarticInOut': QuarticInOut,
            # Quintic
            'QuinticIn': QuinticIn,
            'QuinticOut': QuinticOut,
            'QuinticInOut': QuinticInOut,
            # Exponential
            'ExponentialIn': ExponentialIn,
            'ExponentialOut': ExponentialOut,
            'ExponentialInOut': ExponentialInOut,
            # Circular
            'CircularIn': CircularIn,
            'CircularOut': CircularOut
            }
