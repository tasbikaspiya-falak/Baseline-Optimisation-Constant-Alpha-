import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar



g = 9.81                 
rho = 1.225              

mass = 5.0               
S = 0.7                  

CL_alpha = 5.0          
alpha0 = np.radians(-2) 

CD0 = 0.03               
K = 0.05                


def simulate_glide(alpha_const_deg):

    
    alpha = np.radians(alpha_const_deg)

    # Initial state
    x = 0
    h = 1000.0
    V = 20.0
    dt=0.1

    while h > 0:

        
        CL = CL_alpha * (alpha - alpha0)
        CD = CD0 + K * CL**2

        
        L = 0.5 * rho * V**2 * S * CL
        D = 0.5 * rho * V**2 * S * CD

        # Glide angle
        gamma = np.arctan(D / L)

        # Velocity components
        vx = V * np.cos(gamma)
        vz = -V * np.sin(gamma)

    
        x += vx * dt
        h += vz * dt

        
        if h < 0:
            h = 0

    return x, h


def negative_range(alpha):
    range_val, _ = simulate_glide(alpha)
    return -range_val

result = minimize_scalar(
    negative_range,
    bounds=(-5, 15),
    method='bounded'
)

best_alpha = result.x
best_range = -result.fun


# print("Best alpha (deg):", round(best_alpha, 2))
# print("Maximum range (m):", round(best_range, 2))


alpha_list=np.linspace(-5,15,50)
range_list=[]

for a in alpha_list:
    r,_=simulate_glide(a)
    range_list.append(r)


plt.figure(figsize=(8,5))    
plt.plot(alpha_list,range_list)
plt.xlabel("alpha(deg)")
plt.ylabel("max range")
plt.title("Range vs Angle of Attack")
plt.grid(True)
plt.show()




cl_values=np.linspace(0.1,1.5,200)
cd_values=CD0 + K * cl_values**2

glide_ratio=cl_values/cd_values

max_index=np.argmax(glide_ratio)

best_cl=cl_values(max_index)
best_ratio=glide_ratio(max_index)

print("\n")
