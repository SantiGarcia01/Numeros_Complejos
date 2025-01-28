import math

def sumacplx(a,b):
    return a[0] + b[0], a[1] + b[1]

def multcplx(a,b):
    return ((a[0] * b[0]) - (a[1] * b[1])),((a[0] * b[1]) + (a[1] * b[0]))

def restacplx(a,b):
    return a[0] - b[0], a[1] - b[1]

def divcplx(a,b):
    return (((a[0]*b[0])+(a[1]*b[1]))/(b[0]**2+b[1]**2)),(((b[0]*a[1])-(a[0]*b[1]))/((b[0]**2)+(b[1]**2)))

def modulocplx(a):
    return ((a[0] * 2) + (a[1] * 2))**(1 / 2)

def conjugadocplx(a):
    return (a[0]),((-1) * a[1])

def carte_a_polar(a):
    return modulocplx(a),math.atan(a[1] / a[0])

def polar_a_carte(a):
    return (a[0] * math.cos(a[1])),(a[0] * math.sin(a[1]))

def retornar_fasecplx(a):
    return math.atan2(a[1],a[0])

def main():

    print(sumacplx((3.5, 6),(-6.7, 2)))
    print(multcplx((3.5,6),(-6.7,2)))
    print(restacplx((3.5,6),(-6.7,2)))
    print(divcplx((3.5,6),(-6.7,2)))
    print(modulocplx((3.5,6)))
    print(conjugadocplx((3.5,6)))
    print(carte_a_polar((3.5,6)))
    print(polar_a_carte((3.5,6)))
    print(retornar_fasecplx((3.5,6)))

main()