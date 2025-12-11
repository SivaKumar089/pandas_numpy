import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

# df.plot()

# df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')
# df.plot(kind = 'scatter', x = 'Calories', y = 'Maxpulse')

df["Pulse"].plot(kind = 'hist')

plt.show()