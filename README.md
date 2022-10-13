<h1 align="center">ECUACIONES-DIFERENCIALES</h1>

En este [repositorio](https://github.com/mat0ta/ecuaciones-diferenciales) quedan resueltos los ejercicios la tarea de esta semana. Puedes encontrar otros proyectos y tareas en mi perfil de GitHub: [mat0ta](https://github.com/mat0ta).

<h2>Ecuaciones diferenciales</h2>

Resuelve las ecuaciones diferenciales del examen

El c骴igo empleado para crear dicho algoritmo es el siguiente:

```py

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
        print("\nLa soluci贸n de la primera ecuaci贸n es: \n\n\n")
        sp.pprint(sol)
    def e2():
        x = sp.Symbol("x")
        y = sp.Function("y")
        ecuacion = sp.Eq(y(x).diff(x) * sp.sin(x), y(x) * sp.log(y(x)))
        ics = {y((math.pi/2)): math.e}
        sol = sp.dsolve(ecuacion, y(x), ics=ics)
        print("\nLa soluci贸n de la segunda ecuaci贸n es: \n")
        sp.pprint(sol)
    def e3():
        t = sp.Symbol("t")
        y = sp.Function("y")
        ecuacion = sp.Eq(y(t).diff(t) - (y(t)/(t-2)), 2*(t-2)**2)
        sol = sp.dsolve(ecuacion, y(t))
        print("\nLa soluci贸n de la tercera ecuaci贸n es: \n")
        sp.pprint(sol)
    def e4():
        t = sp.Symbol("t")
        y = sp.Function("y")
        ecuacion = sp.Eq(2*t*y(t).diff(t) - y(t), 3*t**2)
        sol = sp.dsolve(ecuacion, y(t))
        print("\nLa soluci贸n de la cuarta ecuaci贸n es: \n")
        sp.pprint(sol)

```

