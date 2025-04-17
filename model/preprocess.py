import pandas as pd

def preprocess_input(pclass, sex, age):
    sex = 0 if sex.lower() == 'male' else 1
    return pd.DataFrame([[pclass, sex, age]], columns=['pclass', 'sex', 'age'])

