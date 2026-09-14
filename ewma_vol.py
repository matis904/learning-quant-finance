import numpy as np 
import pandas as pd
import random

rng = np.random.default_rng(7)
calme = rng.normal(0, 0.01, 258)      # 258 jours calmes, σ = 1%
agite = rng.normal(0, 0.04, 42)       # 42 derniers jours, σ = 4% (×4)
rendements = np.concatenate([calme, agite])
r = pd.Series(rendements)

vol = (r ** 2).ewm(alpha=0.06).mean() ** 0.5 # daily volatility, EWMA with λ=0.94 (α=0.06)
vol30 = r[-30:].std() # last 30 days
vol252 = r[-252:].std() # annualised


print(f"vol : {round(vol.iloc[-1], 4)}")
print(f"vol30 : {round(vol30, 4)}")
print(f"vol300 : {round(vol252, 4)}")
print(f"annualized : {round(vol252.mean() * 252 ** 0.5, 4)}")
