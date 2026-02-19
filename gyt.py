# jupiter

# %% [markdown]
# # Example Jupyter Python File
# This file can be run in:
# - VS Code (with Python/Jupyter extension)
# - Jupyter Lab
# - Jupyter Notebook (after conversion)
#
# Each `# %%` creates a new cell.

# %%
# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# %%
# Create sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# %%
# Plot the data
plt.figure()
plt.plot(x, y)
plt.title("Sine Wave")
plt.xlabel("X values")
plt.ylabel("sin(X)")
plt.show()

# %%
# Simple calculation
def square(number):
    return number ** 2

result = square(5)
print("Square of 5 is:", result)

# %%
# Interactive input example
name = input("Enter your name: ")
print(f"Hello, {name}! Welcome to Jupyter Python.")



