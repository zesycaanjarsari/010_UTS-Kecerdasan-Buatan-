#Zesyca Dwi Anjarsari
#21091397010
#Manajemen Informatika B
import numpy as np

inputs = [2.0, 3.0, 2.1, 4.3, 4.5, 2.3, 3.5, 7.5, 3.4, 6.5]
weights = [3.2, 1.2, 4.3, 0.6, 1.5, 6.2, 2.4, 3.2, 1.5, 3.4]

bias = 2.5

outputs = np.dot(weights, inputs) + bias
print(outputs)
