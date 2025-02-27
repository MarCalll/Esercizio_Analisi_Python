import pandas as pd
from sklearn.datasets import load_wine
import seaborn as sns

#Branch1
pinguini = sns.load_dataset('penguins')
print(pinguini)
pinguini.dropna(inplace=True)
print(pinguini.info())
# print(pinguini.describe())

specieCount = pinguini['species'].value_counts()
print("\nQuantità specie:\n",specieCount)

#Branch2
# studiare la relazione tra peso corporeo dei pinguini con altre variabili come sesso e lunghezza del becco
mean_body_mass_g_sex = pinguini.groupby('sex')['body_mass_g'].mean()
flipper_length_mm_sex = pinguini.groupby('sex')['flipper_length_mm'].mean()
islandCount = pinguini['island'].value_counts()
print("\nbody mass by sex:\n",mean_body_mass_g_sex)
print("\nflipper length by sex:\n",flipper_length_mm_sex)
print("\nisland count:\n",islandCount)




