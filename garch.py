import numpy as np
import random

rng = np.random.default_rng(1)
omega = 0.05
alpha = 0.1
beta = 0.85
calme = rng.normal(0, 1, 270)
agite = rng.normal(0, 4, 30)
r = np.concatenate([calme, agite])
var = r[0] ** 2
vars_garch = []
for jour in range(1, len(r)):
    var = omega + alpha * r[jour-1] ** 2 + beta * var
    vars_garch.append(var)
    print(f"days {jour} : vol = {var ** 0.5}")

vars_garch = np.array(vars_garch)
volmoy = np.mean(np.sqrt(vars_garch))
reel = np.abs(r[2:])
pred_moyenne = np.full_like(reel, volmoy)
pred_hier = np.sqrt(vars_garch[:-1]) 
erreur_garch  = ((np.sqrt(vars_garch[1:]) - reel) ** 2).mean()
erreur_hier   = ((pred_hier - reel) ** 2).mean()
erreur_moyenne = ((pred_moyenne - reel) ** 2).mean()
print(f"erreur GARCH = {erreur_garch}")
print(f"erreur hier = {erreur_hier}")
print(f"erreur moyenne = {erreur_moyenne}")
print(f"mean volatility of the full history = {volmoy}")
print(len(vars_garch))
print(len(vars_garch[1:]), len(pred_hier), len(reel))