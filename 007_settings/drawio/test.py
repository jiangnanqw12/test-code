import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create a 10x10 DataFrame with example values
df = pd.DataFrame(np.arange(1, 101).reshape((10, 10)))

# Plotting the table using Matplotlib
fig, ax = plt.subplots(figsize=(10, 10))
ax.axis('tight')
ax.axis('off')
ax.table(cellText=df.values, colLabels=df.columns,
         rowLabels=df.index, loc='center')

plt.show()
