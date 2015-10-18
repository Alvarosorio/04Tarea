#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Planeta(object):
    '''
    Complete el docstring.
    '''

    def __init__(self, condicion_inicial, alpha=0):
        '''
        __init__ es un método especial que se usa para inicializar las
        instancias de una clase.

        Ej. de uso:
        >> mercurio = Planeta([x0, y0, vx0, vy0])
        >> print(mercurio.alpha)
        >> 0.
        '''
        self.y_actual = condicion_inicial
        self.t_actual = 0.
        self.alpha = alpha

    def ecuacion_de_movimiento(self, x, y):
        '''
        Implementa la ecuación de movimiento, como sistema de ecuaciónes de
        primer orden.
        '''
        r = np.sqrt(x**2 + y**2)
        ax = -(1/r**2 + self.alpha/r**3)*(x/r)   # asumimos M*G = 1
        ay = -(1/r**2 + self.alpha/r**3)*(y/r)

        return [self.y_actual[2], self.y_actual[3], ax, ay]

    def avanza_euler(self, dt):
        '''
        Toma la condición actual del planeta y avanza su posicion y velocidad
        en un intervalo de tiempo dt usando el método de Euler explícito. El
        método no retorna nada, pero re-setea los valores de self.y_actual.
        '''
        pass

    def avanza_rk4(self, dt):
        '''
        Similar a avanza_euler, pero usando Runge-Kutta 4.
        '''
        vx1, vy1, ax1, ay1 = self.ecuacion_de_movimiento(self.y_actual[0], self.y_actual[1])
        k1_x = vx1*dt, ax1*dt
        k1_y = vy1*dt, ay1*dt

        vx2, vy2, ax2, ay2 = self.ecuacion_de_movimiento(self.y_actual[0] + k1_x[0]/2.0, self.y_actual[1] + k1_y[1]/2.0)
        k2_x = vx2*dt, ax2*dt
        k2_y = vy2*dt, ay2*dt

        vx3, vy3, ax3, ay3 = self.ecuacion_de_movimiento(self.y_actual[0] + k2_x[0]/2.0, self.y_actual[1] + k2_y[1]/2.0)
        k3_x = vx3*dt, ax3*dt
        k3_y = vy3*dt, ay3*dt

        vx4, vy4, ax4, ay4 = self.ecuacion_de_movimiento(self.y_actual[0] + k3_x[0], self.y_actual[1] + k3_y[1])
        k4_x = vx4*dt, ax4*dt
        k4_y = vy4*dt, ay4*dt

        x_f = self.y_actual[0] + (1/6.0) * (k1_x[0] + 2*k2_x[0] + 2*k3_x[0] + k4_x[0])
        y_f = self.y_actual[1] + (1/6.0) * (k1_y[0] + 2*k2_y[0] + 2*k3_y[0] + k4_y[0])

        vx_f = self.y_actual[2] + (1/6.0) * (k1_x[1] + 2*k2_x[1] + 2*k3_x[1] + k4_x[1])
        vy_f = self.y_actual[3] + (1/6.0) * (k1_y[1] + 2*k2_y[1] + 2*k3_y[1] + k4_y[1])

        self.y_actual = [x_f, y_f, vx_f, vy_f]

        pass


    def avanza_verlet(self, dt):
        '''
        Similar a avanza_euler, pero usando Verlet.
        '''
        pass

    def energia_total(self):
        '''
        Calcula la enérgía total del sistema en las condiciones actuales.
        '''
        pass
