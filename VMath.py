from pymel.core.datatypes import Vector, Matrix, Point
import math


def ProjectPointOntoLine(a, b, point):
    ap = point - a
    ab = b - a
    return a + ap.dot(ab) / ab.dot(ab) * ab


def ProjectVectorOntoVector(a, b):
    return a.cross(b) / a.length() * a


def ProjectPointOntoSphere(bounds, point, inner=True):
    bW = bounds.width()
    bD = bounds.depth()
    bH = bounds.height()

    shortest = bW
    if shortest > bD:
        shortest = bD
    if shortest > bH:
        shortest = bH
    if inner:
        radius = shortest / 2
    else:
        radius = (bounds.min() - bounds.max()).length() / 2

    sphereCenter = bounds.center()

    n = point - sphereCenter
    n.normalize()
    return sphereCenter + (n * radius)


def ProjectPointOntoScaledSphere(bounds, point, inner=True):
    bW = bounds.width()
    bD = bounds.depth()
    bH = bounds.height()

    shortest = bW
    if shortest > bD:
        shortest = bD
    if shortest > bH:
        shortest = bH

    if inner:
        radius = shortest / 2
    else:
        radius = (bounds.min() - bounds.max()).length()/2
    rRatio = Vector(bW / shortest, bH / shortest, bD / shortest)

    sphereCenter = bounds.center()

    n = point - sphereCenter
    n.normalize()
    return sphereCenter + (Vector(n[0]*rRatio[0], n[1]*rRatio[1], n[2]*rRatio[2])) * radius


# TODO: finish implementing
# def ScaledSphereIntersection(bounds, point, direction):
#     x = 0
#     y = 1
#     z = 2
#
#     bMax = bounds.max()
#     bMin = bounds.min()
#     direction.normalize()
#
#     sphereW = bounds.width()
#     sphereH = bounds.height()
#     sphereD = bounds.depth()
#
#     shortest = sphereW
#     if sphereH < shortest:
#         shortest = sphereH
#     if sphereD < shortest:
#         shortest = sphereD
#
#     sphereCenter = Point.center(bMax, bMin)
#
#     # Using point as clamp origin
#     # Get difference between point and sphere center
#     vpc = sphereCenter - point
#
#     # Need to get vector from center to point constrained within scaled sphere
#     radius = shortest/2
#     if vpc.dot(direction) < 0:
#         if vpc.length() > radius : return None
#         elif vpc.length() == radius: return point
#         else:
#             projectedCenter = ProjectVectorOntoVector(vpc, direction)
#             dist = math.sqrt(math.pow(radius,2) - math.pow((projectedCenter - sphereCenter).length(),2))
#             di1 = dist - (projectedCenter - point).length()
#             return point + direction * di1
#     else:
#         projectedCenter = ProjectVectorOntoVector(vpc, direction)
#         if (sphereCenter - projectedCenter).length() > radius:
#             return None
#         else:
#             dist = math.sqrt(math.pow(radius, 2) - math.pow((projectedCenter - sphereCenter).length(), 2))
#             if vpc.length() > radius:
#                 di1 = (projectedCenter - point).length() - dist
#             else:
#                 di1 = (projectedCenter - point).length() + dist
#             return point + (direction * di1)


def BoundingBoxIntersection(bounds, point, direction):

    x = 0
    y = 1
    z = 2

    bMax = bounds.max()
    bMin = bounds.min()
    direction = direction.normal()

    dir = direction
    if dir[x] == 0:
        dir[x] = float('Inf')
    if dir[y] == 0:
        dir[y] = float('Inf')
    if dir[z] == 0:
        dir[z] = float('Inf')
    invDir = Vector(1 / dir[x], 1 / dir[y], 1 / dir[z])

    t1 = (bMin[x] - point[x]) * invDir[x]
    t2 = (bMax[x] - point[x]) * invDir[x]
    t3 = (bMin[y] - point[y]) * invDir[y]
    t4 = (bMax[y] - point[y]) * invDir[y]
    t5 = (bMin[z] - point[z]) * invDir[z]
    t6 = (bMax[z] - point[z]) * invDir[z]

    tmin = max(max(min(t1, t2), min(t3, t4)), min(t5, t6))
    tmax = min(min(max(t1, t2), max(t3, t4)), max(t5, t6))

    if tmax < 0:
        t = tmax
        # print('max failed to intersect')
        return point + (direction * t)

    if tmin > tmax:
        t = tmax
        # print('min failed to intersect')
        return point + (direction * t)

    t = tmin

    return point + (direction * t)


def MatrixFromNormal(up, forward=Vector(0, 0, 1)):
    up.normalize()
    forward.normalize()

    side = Vector.cross(up, forward)
    forward = Vector.cross(side, up)

    # the new matrix is
    return Matrix(
        side.x, side.y, side.z, 0,
        up.x, up.y, up.z, 0,
        forward.x, forward.y, forward.z, 0,
        0, 0, 0, 1)
