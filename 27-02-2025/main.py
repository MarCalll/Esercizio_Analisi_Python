import pandas as pd
from sklearn.datasets import load_wine
import seaborn as sns

#Branch1
pinguini = sns.load_dataset('penguins')
print(pinguini)
print(pinguini.info())
print(pinguini.describe())

specie = pinguini['species'].value_counts()
print("\nQuantità specie:\n",specie)
