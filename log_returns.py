import numpy as np 
import pandas as pd

df = pd.read_csv(r"data/prix.csv")
def analyse(df, actif):
    df = df[df["actif"] == actif]
    prix = df["cloture"].values
    lr = np.log(prix[1:] / prix[:-1]) * 100
    ann_lr = lr.mean()  * 252
    moy = lr.mean() 
    vol = lr.std() 
    ann_vol = vol * np.sqrt(252)
    best_daily_gain = lr.max() 
    worst_daily_loss = lr.min() 
    assert abs(lr.sum() - np.log(prix[-1] / prix[0]) * 100) < 1e-9
    return {"actif": actif, "vol_ann": ann_vol, "rdt_ann": ann_lr, "rdt_moy": moy, "vol": vol, "best_daily_gain": best_daily_gain, "worst_daily_loss": worst_daily_loss}

for a in ["AETH", "BTCX", "STAB"]:
    r = analyse(df, a)
    print(f"{r['actif']} — vol annualisée : {r['vol_ann']:.1f}% | rendement annualisé : {r['rdt_ann']:.1f}%")
