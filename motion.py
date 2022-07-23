import numpy as np
from numpy.linalg import norm

def dydt(t,y, G, m1, m2, m3):
#def dydt(y, t): #For the use of the odeint integrator

     #G = 6.67259e-20 #Universal Gravitational Constant (km^3/kg/s^2)

     #Input Data: 

     #m1 = 1e26 # First Body's Mass - kg
     #m2 = 1e26 # Second Body's Mass - kg
     #m3 = 1e26 # Second Body's Mass - kg

     R1 = y[0:3]
     R2 = y[3:6]
     R3 = y[6:9]

     V1 = y[9:12]
     V2 = y[12:15]
     V3 = y[15:18]

     r_12 = np.subtract(R2, R1)
     r12 = norm(r_12)

     r_13 = np.subtract(R3, R1)
     r13 = norm(r_13)

     r_23 = np.subtract(R3, R2)
     r23 = norm(r_23)

     # Creating the return motion vector dydt = [V1 V2 V3 A1 A2 A3]
     dydt = np.zeros(18)

     dydt[0:3] = V1
     dydt[3:6] = V2
     dydt[6:9] = V3

     # Finding the Accelerations thought the Motion Equation     
     dydt[9:12]  = [(G * m2 * ((R2[0] - R1[0])/(r12**3))) + (G * m3 * ((R3[0] - R1[0])/(r13**3))),
                    (G * m2 * ((R2[1] - R1[1])/(r12**3))) + (G * m3 * ((R3[1] - R1[1])/(r13**3))),
                    (G * m2 * ((R2[2] - R1[2])/(r12**3))) + (G * m3 * ((R3[2] - R1[2])/(r13**3)))]

     dydt[12:15] = [(G * m1 * ((R1[0] - R2[0])/(r12**3))) + (G * m3 * ((R3[0] - R2[0])/(r23**3))),
                    (G * m1 * ((R1[1] - R2[1])/(r12**3))) + (G * m3 * ((R3[1] - R2[1])/(r23**3))),
                    (G * m1 * ((R1[2] - R2[2])/(r12**3))) + (G * m3 * ((R3[2] - R2[2])/(r23**3)))]

     dydt[15:18] = [(G * m1 * ((R1[0] - R3[0])/(r13**3))) + (G * m2 * ((R2[0] - R3[0])/(r23**3))),
                    (G * m1 * ((R1[1] - R3[1])/(r13**3))) + (G * m2 * ((R2[1] - R3[1])/(r23**3))),
                    (G * m1 * ((R1[2] - R3[2])/(r13**3))) + (G * m2 * ((R2[2] - R3[2])/(r23**3)))]

     # Returning the vector with Velocity and Acceleration of the Bodies 
     return dydt