import numpy as np
import pandas as pd

rng = np.random.default_rng(7)
iv = rng.normal(20, 5, 200)     
bruit = rng.normal(0, 4, 200)
realisee = iv - 3 + bruit
n_crises = int(0.05 * 200)           
indices_crise = rng.choice(200, n_crises, replace=False)  
realisee[indices_crise] = iv[indices_crise] * 3            

def iv_prime(realisee, iv):
    r = (realisee - iv) / iv
    mean = r.mean()
    sigma = r.std()
    worst = r.min()
    z = (r - mean) / sigma
    skew = (z ** 3).mean()
    prime = (iv - realisee).mean()
    pnl = iv - realisee
    z_pnl = (pnl - pnl.mean()) / pnl.std()
    skew_pnl = (z_pnl ** 3).mean()
    print(f"skew du P&L (pas de r) = {skew_pnl:.4f}")
    print(f"r = {r}, prime = {prime} mean = {mean}, sigma = {sigma}, worst = {worst}, skew = {skew}")
    return prime
iv_prime(realisee, iv)