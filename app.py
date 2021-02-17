from data_creator import RetrieveSearchData
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create Excel-CSV. Inputs are men/women and search_term can be anything you want to search.
RetrieveSearchData.create_csv('women', 'workout')

# Plot Data you searched
# data = pd.read_csv('data/men_workout.csv')
# y_pos = np.arange(10)

# plt.rcdefaults()
# fig, ax = plt.subplots()

# ax.barh(y_pos, data['count'], align='center')
# ax.set_yticks(y_pos)
# ax.set_yticklabels(data['word'])
# ax.invert_yaxis()
# plt.show()