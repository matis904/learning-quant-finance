import numpy as np 
import log_returns as L6

z = (np.array(L6.lr) - np.array(L6.moy)) / np.array(L6.vol)
haut = (np.abs(z) > 2).sum()
extreme = (np.abs(z) > 3).sum()



print(f"z-score : {round(z, 4)}")
print(f"jours avec 2σ : {haut}")
pct2 = haut / len(z) * 100
print(f"{pct2:.1f}% au-delà de 2σ (attendu ≈ 5 %)")
pct3 = extreme / len(z) * 100
print(f"{pct3:.1f}% au-delà de 3σ (attendu ≈ 0.3 %)")