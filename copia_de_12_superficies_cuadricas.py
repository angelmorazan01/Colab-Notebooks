# -*- coding: utf-8 -*-
"""Copia_de_12_Superficies_Cuadricas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14IEr-zpYhuSYs-xXFtmyYDxGSpOCl5eH

# Cilindros

El tipo más sencillo de superficie cuádrica es aquél en el que sólo aparecen
involucradas una o dos variables.

**Definición.** Un *cilindro* es la superficie formada por rectas paralelas cada
una de las cuales contiene un punto de una curva plana llamada *directriz* del
cilindro. Cada una de las rectas paralelas es una *generatriz* del cilindro.

![Cilindro parabólico y cilindro hiperbólico en posición canónica](https://i.imgur.com/9OGTU23.png)

**Figura.** Cilindro parabólico y cilindro hiperbólico en posición canónica.

Con base en la imágen anterior, grafiquémos el cilindro parabólico en $\mathbb{R}^{3}$

$$x^2 = 4z,$$

o equivalente, $z=\frac{1}{4}x^2$:
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm # Para definir el color
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = y = np.linspace(-5.0, 5.0, 10**3)
X, Y = np.meshgrid(x, y)

z = np.array([1/4*x**2 for x in np.ravel(X)])
Z = z.reshape(X.shape)

ax.plot_surface(X, Y, Z, cmap=cm.autumn_r)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.view_init(30, 25) # Ángulos: (elevación, azimut)

"""**Nota.** Si el ángulo de visión por defecto no es óptimo, podemos utilizar el método `view_init` para establecer los ángulos de elevación y azimutal. En nuestro caso, utilizamos una elevación de 30 grados (es decir, 30 grados por encima del plano $XY$ ) y un azimut de 25 grados (es decir, girado 25 grados en sentido contrario a las agujas del reloj alrededor del eje $Z$ ):

>**Ejercicio 1.** Grafique el cilindro parabólico en $\mathbb{R}^{3}$  
$$y^2 = x.$$

Ahora, grafiquémos el cilindro hiperbólico en $\mathbb{R}^{3}$

$$\frac{z^2}{4} - x^2 = 1,$$

o equivalente, $x = \pm\sqrt{\frac{z^2}{4}-1}$:
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm # Para definir el color
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

y = z = np.linspace(-10, 10, 10**3)
Y, Z = np.meshgrid(y, z)

x = np.array([1/4*z**2 - 1 for z in np.ravel(Z)])
X = x.reshape(Y.shape)

ax.plot_surface(-np.sqrt(X), Y, Z, cmap=cm.autumn_r) # Raíz negativa
ax.plot_surface(np.sqrt(X), Y, Z, cmap=cm.autumn_r) # Raíz positiva

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.view_init(25, 20)

""">**Ejercicio 2.** Grafique el cilindro hiperbólico en $\mathbb{R}^{3}$  
$$\frac{y^2}{4} - z^2 = 1.$$

Grafiquémos el cilindro elíptico en $\mathbb{R}^{3}$

$$x^2 + \frac{z^2}{4} = 1,$$

o equivalente, $x = \pm\sqrt{1-\frac{z^2}{4}}$:
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm # Para definir el color
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

y = z = np.linspace(-2, 2, 10**3)
Y, Z = np.meshgrid(y, z)

x = np.array([1 - 1/4*z**2 for z in np.ravel(Z)])
X = x.reshape(Y.shape)

ax.plot_surface(-np.sqrt(X), Y, Z, cmap=cm.autumn_r) # Raíz negativa
ax.plot_surface(np.sqrt(X), Y, Z, cmap=cm.autumn_r) # Raíz positiva

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.view_init(25, 20)

""">**Ejercicio 3.** Grafique el cilindro elíptico en $\mathbb{R}^{3}$  
$$\frac{x^2}{4} + y^2 = 1.$$

# Superficies de Revolución

Otra forma sencilla de obtener superficies cuádricas es rotar una cónica en
torno a uno de sus ejes de simetría.

**Definición.** Una *superficie de revolución* es la superficie generada al rotar una curva plana en torno a una recta contenida en ese mismo plano.

![](https://i.imgur.com/pjWz4aU.png)

**Figura.** Meridianos y paralelos de una superficie de revolución.

Las distintas posiciones de la curva generatriz se denominan *meridianos* de la superficie de revolución, y las circunferencias descritas por cada uno de los puntos de la curva generatriz se denominan *paralelos* de la superficie de revolución, generalizando así los conceptos de meridiano y paralelo del globo
terráqueo.

De la definición es inmediato que una superficie de revolución es simétrica respecto a cualquier plano que pase por el eje de revolución, pues cada meridiano tiene un simétrico respecto a cualquiera de esos planos.

Grafiquémos el elipsoide de revolución en $\mathbb{R}^{3}$

$$x^2 + \frac{y^2}{4} + \frac{z^2}{4} = 1,$$

o equivalente, $x = \pm\sqrt{1 - \frac{y^2}{4}- \frac{z^2}{4}}$:
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm # Para definir el color
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

y = z = np.linspace(-4, 4, 10**3)
Y, Z = np.meshgrid(y, z)

x = np.array([1 - y**2 - z**2/16 for y, z in zip(np.ravel(Y), np.ravel(Z))])
X = x.reshape(Y.shape)

ax.plot_surface(-np.sqrt(X), Y, Z, cmap=cm.autumn_r) # Raíz negativa
ax.plot_surface(np.sqrt(X), Y, Z, cmap=cm.autumn_r) # Raíz positiva

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.view_init(25, 20)

"""Ahora, grafiquémos el paraboloide de revolución en $\mathbb{R}^{3}$

$$x^2 + z^2 = 4y,$$

o equivalente, $y = \frac{x^2 + z^2}{4}$:
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm # Para definir el color
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = z = np.linspace(-5, 5, 10**3)
X, Z = np.meshgrid(x, z)

y = np.array([(x**2 + z**2)/4 for x, z in zip(np.ravel(X), np.ravel(Z))])
Y = y.reshape(X.shape)

ax.plot_surface(X, Y, Z, cmap=cm.autumn_r)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.view_init(25, 20)

"""Grafiquémos el hiperboloide de dos hojas $\mathbb{R}^{3}$

$$-x^2 - y^2 + z^2 = 1,$$

o equivalente, $z = \pm\sqrt{1 + x^2 + y^2}$:
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm # Para definir el color
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = y = np.linspace(-3, 3, 10**3)
X, Y = np.meshgrid(x, y)

z = np.array([1 + x**2 + y**2 for x, y in zip(np.ravel(X), np.ravel(Y))])
Z = z.reshape(X.shape)

ax.plot_surface(X, Y, -np.sqrt(Z), cmap=cm.autumn_r) # Raíz negativa
ax.plot_surface(X, Y, np.sqrt(Z), cmap=cm.autumn_r) # Raíz positiva

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.view_init(25, 45)

"""Finalmente, grafiquémos el hiperboloide de una hoja $\mathbb{R}^{3}$

$$x^2 + y^2 - z^2 = 1,$$

o equivalente, $z = \pm\sqrt{x^2 + y^2 - 1}$:
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm # Para definir el color
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = y = np.linspace(-2, 2, 10**3)
X, Y = np.meshgrid(x, y)

z = np.array([x**2 + y**2 - 1 for x, y in zip(np.ravel(X), np.ravel(Y))])
Z = z.reshape(X.shape)

ax.plot_surface(X, Y, -np.sqrt(Z), cmap=cm.rainbow_r) # Raíz negativa
ax.plot_surface(X, Y, np.sqrt(Z), cmap=cm.rainbow) # Raíz positiva

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.view_init(20, 20)

""">**Ejercicio 4.** Grafique el cono (infinito) $\mathbb{R}^{3}$  
$$x^2 + y^2 - z^2 = 0.$$

# Las Posibles Superficies Cuádricas

Una ecuación de segundo grado en tres variables sin términos mixtos tiene la
forma

$$Ax^2 + By^2 + Cz^2 + Gx + Hy + Iz + J = 0. \qquad (1)$$

Es importante notar que, en general, para satisfacerla podemos elegir arbitrariamente el valor de dos de las variables y entonces la tercera queda obligada excepto por el signo. Por haber **dos grados de libertad** decimos que una ecuación en tres variables representa una superficie.

**Nota.** Cuando hay términos mixtos en una ecuación cuadrática, éstos pueden
eliminarse mediante una rotación adecuada con centro en el origen $(0, 0, 0)$.

* Resulta conveniente tener un función en Python que nos retorne el tipo de superficie que determina la ecuación (1). Entonces, ¡Construyámosla!:
"""

# En construcción !!! (Para la clase del jueves)