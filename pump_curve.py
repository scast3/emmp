import matplotlib.pyplot as plt

# Define the x and y coordinates of the points
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create the scatter plot
plt.scatter(x, y)

# Add labels and a title to the plot
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Pump Curve')

# Display the plot
plt.show()
