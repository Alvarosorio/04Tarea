from planeta import *
import matplotlib.pyplot as plt
import numpy as np

planeta_X = Planeta([10, 0, 0, 0.4])
planeta_Y = Planeta([10, 0, 0, 0.4])
planeta_Z = Planeta([10, 0, 0, 0.4])

pasos = 100000
fin = 10000.0
t = np.linspace(0, fin, pasos)

x_euler = np.zeros(pasos)
y_euler = np.zeros(pasos)
e_euler = np.zeros(pasos)

x_rk4 = np.zeros(pasos)
y_rk4 = np.zeros(pasos)
e_rk4 = np.zeros(pasos)

x_verlet = np.zeros(pasos)
y_verlet = np.zeros(pasos)
e_verlet = np.zeros(pasos)

h_euler = fin/pasos
h_rk4 = fin/pasos
h_verlet = fin/pasos


for i in range(0, pasos):
    planeta_X.avanza_euler(h_euler)
    x_euler[i] = planeta_X.y_actual[0]
    y_euler[i] = planeta_X.y_actual[1]
    e_euler[i] = planeta_X.energia_total()

for i in range(0, pasos):
    planeta_Y.avanza_rk4(h_rk4)
    x_rk4[i] = planeta_Y.y_actual[0]
    y_rk4[i] = planeta_Y.y_actual[1]
    e_rk4[i] = planeta_Y.energia_total()

for i in range(0, pasos):
    planeta_Z.avanza_verlet(h_verlet)
    x_verlet[i] = planeta_Z.y_actual[0]
    y_verlet[i] = planeta_Z.y_actual[1]
    e_verlet[i] = planeta_Z.energia_total()

fig = plt.figure()

plt.plot(x_euler, y_euler)
plt.xlabel('x')
plt.ylabel('y')
plt.title("Orbita para el metodo de euler")
plt.grid()

fig = plt.figure()

plt.plot(x_rk4, y_rk4, 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.title("Orbita para el metodo de rk4")
plt.grid()

fig = plt.figure()

plt.plot(x_verlet, y_verlet, 'g')
plt.xlabel('x')
plt.ylabel('y')
plt.title("Orbita para el metodo de verlet")
plt.grid()

fig = plt.figure()

plt.plot(t, e_euler)
plt.xlabel('Tiempo')
plt.ylabel('Energia')
plt.title("Energia para el metodo de euler")
plt.grid()

fig = plt.figure()

plt.plot(t, e_rk4, 'r')
plt.xlabel('Tiempo')
plt.ylabel('Energia')
plt.title("Energia para el metodo de rk4")
plt.grid()

fig = plt.figure()

plt.plot(t, e_verlet, 'g')
plt.xlabel('Tiempo')
plt.ylabel('Energia')
plt.title("Energia para el metodo de verlet")
plt.grid()

plt.show()
