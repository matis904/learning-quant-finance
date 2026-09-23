import numpy as np
import pandas as pd

rng = np.random.default_rng(7)
rendements = rng.standard_t(4, 1000)


def var(rendements, niveau, methode):
    if methode == "historique":
        v = -np.percentile(rendements, 100 - niveau)
    elif methode == "gaussienne":
        multiple = 1.65 if niveau == 95 else 2.33
        v = multiple * rendements.std()
    return v
v1 = var(rendements, 95, "historique")
v2 = var(rendements, 95, "gaussienne")
v3 = var(rendements, 99, "historique")
v4 = var(rendements, 99, "gaussienne")

print(v1, v2, v3, v4)

for nom, v in [("hist95", v1), ("gauss95", v2), ("hist99", v3), ("gauss99", v4)]:
    breaches = (rendements < -v).sum()
    pct = breaches / len(rendements) * 100
    print(nom, breaches, round(pct, 2), "% (attendu:", 5 if "95" in nom else 1, "%)")