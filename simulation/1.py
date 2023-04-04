import numpy as np
import matplotlib.pyplot as plt

# Generate a random 4x4x8 descriptor
descriptor = np.random.rand(4, 4, 8)

# Plot the descriptor
fig, axs = plt.subplots(4, 4, figsize=(8, 8))
for i in range(4):
    for j in range(4):
        axs[i, j].bar(range(8), descriptor[i, j])
        axs[i, j].set_xticks(range(8))
        axs[i, j].set_yticks([])
        axs[i, j].set_xticklabels([])
        axs[i, j].set_title(f'Cell ({i+1}, {j+1})')

plt.tight_layout()
plt.show()
