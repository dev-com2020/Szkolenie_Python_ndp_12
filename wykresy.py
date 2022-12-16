import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data.csv')
df['date'] = pd.to_datetime(df.date, format='%d/%m/%Y')
y = df['Close']
x = df['date']

fig, ax = plt.subplots(2, 2, figsize=(10, 10))
# title = ax.set_title('Wykres numer 1')
ax[0, 0].plot(x, y)
ax[1, 0].bar(x, y)
ax[0, 1].scatter(x, y, marker='x', alpha=.5)
ax[1, 1].pie([100, 65], labels=['TAK', 'NIE'])
plt.style.use('dark_background')
plt.show()
