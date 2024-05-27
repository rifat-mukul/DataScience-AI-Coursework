# import numpy as np
# import matplotlib.pyplot as plt

# x = np.linspace(-2, 2, num=5)

# print(x)

import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a plot
plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.grid(True)

# Show the plot
plt.show()
