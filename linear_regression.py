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
    return {
        "slope": round(float(a), 6),
        "intercept": round(float(b), 6),
        "mse_model": round(float(mse), 6),
        "mse_baseline": round(float(mse_base), 6)
    }
for a in ["AETH", "BTCX", "STAB"]:
    result = linear_regression(df, a)
    print(round(result["slope"], 2))
    print(f"mse : {result['mse_model']}")
    print(f"mse baseline : {result['mse_baseline']}")
