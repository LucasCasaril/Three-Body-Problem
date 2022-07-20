import numpy as np
from numpy.linalg import norm 


def dydt(t,y, G, m1, m2, m3):
#def dydt(y, t):

     #G = 6.67259e-20 #Universal Gravitational Constant (km^3/kg/s^2)

     #Input Data: 
     #m1 = 1e26 # First Body's Mass - kg
     #m2 = 1e20 # Second Body's Mass - kg
     #m3 = 1e20 # Second Body's Mass - kg

     R1 = [y[0], y[1], y[2]]
     R2 = [y[3], y[4], y[5]]
     R3 = [y[6], y[7], y[8]]

     V1 = [y[9],  y[10], y[11]]
     V2 = [y[12], y[13], y[14]]
     V3 = [y[15], y[16], y[17]]

     r_12 = np.subtract(R2, R1)
     r_12_vec = list(r_12)
     r12 = norm(r_12_vec)
 
     r_13 = np.subtract(R3, R1)
     r_13_vec = list(r_13)
     r13 = norm(r_13_vec)
 
     r_23 = np.subtract(R3, R2)
     r_23_vec = list(r_23)
     r23 = norm(r_23_vec)

     # Finding the acceleration of the Bodies
     accel_1_X = (G * m2 * ((R2[0] - R1[0])/(r12**3))) + (G * m3 * ((R3[0] - R1[0])/(r13**3)))
     accel_1_Y = (G * m2 * ((R2[1] - R1[1])/(r12**3))) + (G * m3 * ((R3[1] - R1[1])/(r13**3)))
     accel_1_Z = (G * m2 * ((R2[2] - R1[2])/(r12**3))) + (G * m3 * ((R3[2] - R1[2])/(r13**3)))
     
     accel_1 = [accel_1_X, accel_1_Y, accel_1_Z]
     
     accel_2_X = (G * m1 * ((R1[0] - R2[0])/(r12**3))) + (G * m3 * ((R3[0] - R2[0])/(r23**3)))
     accel_2_Y = (G * m1 * ((R1[1] - R2[1])/(r12**3))) + (G * m3 * ((R3[1] - R2[1])/(r23**3)))
     accel_2_Z = (G * m1 * ((R1[2] - R2[2])/(r12**3))) + (G * m3 * ((R3[2] - R2[2])/(r23**3)))
     
     accel_2 = [accel_2_X, accel_2_Y, accel_2_Z]
     
     accel_3_X = (G * m1 * ((R1[0] - R3[0])/(r13**3))) + (G * m2 * ((R2[0] - R3[0])/(r23**3)))
     accel_3_Y = (G * m1 * ((R1[1] - R3[1])/(r13**3))) + (G * m2 * ((R2[1] - R3[1])/(r23**3)))
     accel_3_Z = (G * m1 * ((R1[2] - R3[2])/(r13**3))) + (G * m2 * ((R2[2] - R3[2])/(r23**3)))
     
     accel_3 = [accel_3_X, accel_3_Y, accel_3_Z]


     dydt = np.concatenate((V1, V2, V3, accel_1, accel_2, accel_3), axis=None)

     # Returning the vector with Velocity and Acceleration of the Bodies 
     return dydt