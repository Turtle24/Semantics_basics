import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/men_diet.csv")
print(df.head(5))
fig = plt.figure(figsize= (10, 8))
plt.title('Word Frequencies From Mens Health Website', size = 20)
sns.barplot(data = df, x = 'word', y='count', palette='magma', edgecolor='.6')
plt.show()