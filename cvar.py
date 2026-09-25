import numpy as np
import pandas as pd

rng = np.random.default_rng(7)
r = rng.standard_t(4, 1000)

var = np.percentile(r, 5)
cvar = r[r <= var].mean()
link = cvar / var
print(f" VaR = {var} CVaR = {cvar} link = {link}")

var = np.percentile(r, 1)
cvar = r[r <= var].mean()
link = cvar / var
print(f" VaR = {var} CVaR = {cvar} link = {link}")

corps = rng.normal(0, 1, 950)
juste_pire = rng.normal(-3.0, 0.1, 30)

pire_A = rng.normal(-3.8, 0.15, 20)
pire_B = rng.uniform(-12, -4, 20)

portefeuille_A = np.concatenate([corps, juste_pire, pire_A])
portefeuille_B = np.concatenate([corps, juste_pire, pire_B])
def var(r, niveau):
    return -np.percentile(r, 100-niveau)

def cvar(r, niveau):
    v = var(r, niveau)
    return -r[r < -v].mean()

print("VaR A:", var(portefeuille_A, 95), " VaR B:", var(portefeuille_B, 95))
print("CVaR A:", cvar(portefeuille_A, 95), " CVaR B:", cvar(portefeuille_B, 95))