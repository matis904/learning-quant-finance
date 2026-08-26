import numpy as np
import pandas as pd

df = pd.read_csv(r"data/prix.csv")


def linear_regression(df, actif, part_train=0.7):
    df = df[df["actif"] == actif]
    prix = df["cloture"].values
    r = np.log(prix[1:] / prix[:-1])
    x = r[:-1] 
    y = r[1:] 
    coupe = int(len(x) * part_train)
    x_tr, y_tr = x[:coupe], y[:coupe]
    x_te, y_te = x[coupe:], y[coupe:]
    a, b = np.polyfit(x_tr, y_tr, 1)     
    pred = a * x_te + b                 
    mse = ((y_te - pred) ** 2).mean()    
    mse_base = (y_te ** 2).mean()        
    print(round(a, 2))
    print(f"mse : {mse}")
    print(f"mse baseline : {mse_base}")
    return 
for a in ["AETH", "BTCX", "STAB"]:
    linear_regression(df, a)




