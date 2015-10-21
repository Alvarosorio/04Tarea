from planeta import *
import matplotlib.pyplot as plt
import numpy as np

planeta_W = Planeta([10, 0, 0, 0.4], 10**(-2.786)) # RUT 17.951.786-8

pasos = 100000
fin = 10000.0
t = np.linspace(0, fin, pasos)

x_verlet = np.zeros(pasos)
y_verlet = np.zeros(pasos)
e_verlet = np.zeros(pasos)

h_verlet = fin/pasos

for i in range(0, pasos):
    planeta_W.avanza_verlet(h_verlet)
    x_verlet[i] = planeta_W.y_actual[0]
    y_verlet[i] = planeta_W.y_actual[1]
    e_verlet[i] = planeta_W.energia_total()
    planeta_W.t_actual += h_verlet


fig = plt.figure()

plt.plot(x_verlet, y_verlet, 'g')
plt.xlabel('x')
plt.ylabel('y')
plt.title("Orbita para el Metodo de Verlet con correccion")
plt.grid()

fig = plt.figure()

plt.plot(t, e_verlet, 'g')
plt.xlabel('Tiempo')
plt.ylabel('Energia')
plt.title("Energia para el Metodo de Verlet")
plt.grid()

plt.show()
