import math
import sympy as sp
from sympy import *

class EDO():
    def e1():
        x = sp.Symbol("x")
        y = sp.Symbol("y")
        e1 = integrate((1 + 1/y), y)
        e2 = integrate((x**2 - 1), x)
        ecuacion = sp.Eq(e1, e2)
        sol = sp.solve(ecuacion, y)
        print("\nLa solución de la primera ecuación es: \n\n\n")
        sp.pprint(sol)
    def e2():
        x = sp.Symbol("x")
        y = sp.Function("y")
        ecuacion = sp.Eq(y(x).diff(x) * sp.sin(x), y(x) * sp.log(y(x)))
        ics = {y((math.pi/2)): math.e}
        sol = sp.dsolve(ecuacion, y(x), ics=ics)
        print("\nLa solución de la segunda ecuación es: \n")
        sp.pprint(sol)
    def e3():
        t = sp.Symbol("t")
        y = sp.Function("y")
        ecuacion = sp.Eq(y(t).diff(t) - (y(t)/(t-2)), 2*(t-2)**2)
        sol = sp.dsolve(ecuacion, y(t))
        print("\nLa solución de la tercera ecuación es: \n")
        sp.pprint(sol)
    def e4():
        t = sp.Symbol("t")
        y = sp.Function("y")
        ecuacion = sp.Eq(2*t*y(t).diff(t) - y(t), 3*t**2)
        sol = sp.dsolve(ecuacion, y(t))
        print("\nLa solución de la cuarta ecuación es: \n")
        sp.pprint(sol)