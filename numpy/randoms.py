from numpy import random
import numpy as np
# x = random.randint(100)
# x = random.rand()
# x=random.randint(100, size=(10))
# x=random.randint(100, size=(2,3))
# x = random.rand(5)
# x = random.choice([3, 5, 7, 9])
# x = random.choice([3, 5, 7, 9], size=(3, 5))
# x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
# arr = np.array([1, 2, 3, 4, 5])

# random.shuffle(arr)
# print(random.permutation(arr))

# print(arr)



import matplotlib.pyplot as plt
import seaborn as sns

# sns.displot([0, 1, 2, 3, 4, 5])
sns.displot([0, 1, 2, 3, 4, 5],kind='kde')

plt.show()