from data_creator import RetrieveSearchData
import matplotlib.pyplot as plt
import pandas as pd

# Create Excel-CSV. Inputs are men/women and search_term can be anything you want to search.
# RetrieveSearchData.create_csv('men', 'workout')

# Plot Data you searched
data = pd.read_csv('data/men_workout.csv')
plt.plot(data['count'])
plt.xticks([1,2,3,4,5,6,7,8,9,10],
            data['word'])
plt.show()