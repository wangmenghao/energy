import sys, csv
from energydiagram import ED
from matplotlib import pyplot as plt
import pandas as pd


diagram = ED()

df = pd.read_csv('test1.csv')

max_location = df['location'].max()

for index, row in df.iterrows():
    print(index)
    print(row['name'])
    diagram.add_level(energy = row['energies'], bottom_text = row['name'], color = row['color'])
    if (row['location']) < max_location:
        diagram.add_link(row['location'] - 1, row['location'])
#plot ,ax = diagram.plot(show_IDs=True)
plt.show()

## we adjust some parameters
#diagram.ax.set_ylabel('My label')
#diagram.fig.set_figwidth(10)
## don't want tikcs on the y label
#diagram.ax.set_yticks([])
## I want to show on the x axis instead
#diagram.ax.axes.get_xaxis().set_visible(True)
#diagram.ax.spines['bottom'].set_visible(True)
#diagram.ax.set_xlabel("My x label")
## we replot the figure (sometimes we have to resize with the mouse the figure so we force to refresh)
#diagram.fig.show()

plt.show()