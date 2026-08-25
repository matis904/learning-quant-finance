import numpy as np
import pandas as pd

t1 = pd.read_csv(r"data/trades_simple.csv")
pnl1 = (t1["vente"] - t1["achat"]) * t1["quantite"]
t2 = pd.read_csv(r"data/trades.csv")
pnl2 = t2["pnl_brut"] - t2["frais"]

def analyse(nom, pnls):
    nmb_trades = len(pnls)
    pnl_total = pnls.sum()
    moy = pnls.mean()
    std = pnls.std()
    wr = (pnls > 0).sum() * 100 / nmb_trades
    ratio = moy / std if std != 0 else float('inf')

    print(f"stratégie {nom}:")
    print(f"nombre de trades : {nmb_trades}")
    print(f"pnl total : {pnl_total}")
    print(f"moyenne : {moy}")
    print(f"écart type : {std}")
    print(f"win rate : {wr}%")
    print(f"ratio : {ratio}")

print("Analyse de la stratégie 1 : ")
analyse("t1", pnl1)
print("Analyse de la stratégie 2 : ")
analyse("t2", pnl2)
