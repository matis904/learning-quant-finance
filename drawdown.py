import numpy as np

rng = np.random.default_rng(3)
rendements_jour = rng.normal(0.0008, 0.015, 500)
V0 = 10000
equity = V0 * np.cumprod(1 + rendements_jour)
pic = np.maximum.accumulate(equity)
dd = (equity - pic) / pic

i_creux = np.argmin(dd)
date_pic = np.argmax(equity[:i_creux])


sous_eau = (dd < 0)
print(sous_eau.sum())

max_serie, courante = 0, 0
for b in sous_eau:
    courante = courante + 1 if b else 0
    max_serie = max(max_serie, courante)
print(max_serie)

rendement_annualiser = (equity[-1]/equity[0]) ** (252/500) - 1
calmar = rendement_annualiser / abs(dd.min())
print(f"drawdown max = {dd.min():.2%}")
print(f"date pic = {date_pic}, date creux = {i_creux}")
print(f"plus long passage sous l'eau = {max_serie} jours")
print(f"calmar = {calmar:.2f}")