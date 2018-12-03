from pymel.core.datatypes import Vector, Matrix, Point, BoundingBox
import math


# Note: Maya data types for Vector already supports Vector Projections, some of these methods are here as reference
# Example: Vector(a).projectionOnto(b)


def project_point_onto_line(a, b, point):
    # type: (Vector, Vector, Point) -> Point
    """ Returns point projected on line between vectors a and b """
    ap = point - a
    ab = b - a
    return a + ap.dot(ab) / ab.dot(ab) * ab


def project_vector_onto_vector(a, b):
    # type: (Vector, Vector) -> Vector
    """ Returns vector projected on line between vectors a and b """
    return a.cross(b) / a.length() * a


# TODO: reconsider the purpose of inner, this is not very clear
def project_point_onto_sphere(bounds, point, inner=True):
    # type: (BoundingBox, Point, bool) -> Point
    b_w = bounds.width()
    b_d = bounds.depth()
    b_h = bounds.height()

    shortest = b_w
    if shortest > b_d:
        shortest = b_d
    if shortest > b_h:
        shortest = b_h
    if inner:
        radius = shortest / 2
    else:
        radius = (bounds.min() - bounds.max()).length() / 2

    sphere_center = bounds.center()

    n = point - sphere_center
    n.normalize()
    return sphere_center + (n * radius)


def project_point_onto_scaled_sphere(bounds, point, inner=True):
    # type: (BoundingBox, Point, bool) -> Point
    b_w = bounds.width()
    b_d = bounds.depth()
    b_h = bounds.height()

    shortest = b_w
    if shortest > b_d:
        shortest = b_d
    if shortest > b_h:
        shortest = b_h

    if inner:
        radius = shortest / 2
    else:
        radius = (bounds.min() - bounds.max()).length() / 2
    r_ratio = Vector(b_w / shortest, b_h / shortest, b_d / shortest)

    sphere_center = bounds.center()

    n = point - sphere_center
    n.normalize()
    return sphere_center + (Vector(n[0] * r_ratio[0], n[1] * r_ratio[1], n[2] * r_ratio[2])) * radius


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


def bounding_box_intersection(bounds, point, direction):
    # type: (BoundingBox, Point, Vector) -> Point
    x = 0
    y = 1
    z = 2

    b_max = bounds.max()
    b_min = bounds.min()
    direction = direction.normal()

    dir = direction
    if dir[x] == 0:
        dir[x] = float('Inf')
    if dir[y] == 0:
        dir[y] = float('Inf')
    if dir[z] == 0:
        dir[z] = float('Inf')
    inv_dir = Vector(1 / dir[x], 1 / dir[y], 1 / dir[z])

    t1 = (b_min[x] - point[x]) * inv_dir[x]
    t2 = (b_max[x] - point[x]) * inv_dir[x]
    t3 = (b_min[y] - point[y]) * inv_dir[y]
    t4 = (b_max[y] - point[y]) * inv_dir[y]
    t5 = (b_min[z] - point[z]) * inv_dir[z]
    t6 = (b_max[z] - point[z]) * inv_dir[z]

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


def matrix_from_normal(up, forward=Vector(0, 0, 1)):
    # type: (Vector, Vector) -> Matrix
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
