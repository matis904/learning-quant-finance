import numpy as np

def correlation(n, k=19):
    rng = np.random.default_rng(42)
    ref = rng.normal(0, 1, n)
    pire = 0
    for i in range(k):
        autre = rng.normal(0, 1, n)
        c = np.corrcoef(ref, autre)[0, 1]
        print(n, round(c, 3))
        if abs(c) > pire:
            pire = abs(c)
    return pire


for taille in [5, 50, 5000]:
    print(f"n = {taille} → pire : {correlation(taille):.3f}")