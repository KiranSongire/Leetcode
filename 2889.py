import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    df = animals[['name', 'weight']]
    df1 = animals[df['weight'] > 100]
    df1 = df1.sort_values(by='weight', ascending=False)[['name']]
    return df1
  