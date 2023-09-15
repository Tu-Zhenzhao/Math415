import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Step 1: Define the function representing the ODE
def ode_func(x, t):
    return 3*x*(1-x/10)*(x/2-1)

# Step 2: Generate a mesh grid
x = np.linspace(-1, 11, 20) # Adjust the range and points as necessary
t = np.linspace(0, 10, 20)  # Adjust the range and points as necessary

X, T = np.meshgrid(x, t)
U = ode_func(X, T)
V = np.ones_like(T)  # Since the differential equation is only in terms of x, we can consider time to be flowing at a constant rate.

# Save the data to a csv file
data = {'T': T.flatten(), 'X': X.flatten(), 'U': U.flatten(), 'V': V.flatten()}
df = pd.DataFrame(data)
df.to_csv('vector_field_data.csv', index=False)

# Step 3: Plot the vector field
plt.quiver(T, X, U, V)
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('Vector Field')
plt.grid()
plt.show()

