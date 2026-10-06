import numpy as np

def risk_measure(n, seed):
    print(       "----------------------------")
    print(f"n = {n}, seed = {seed}")
    rng = np.random.default_rng(seed)
    rendements_jour_marché = rng.normal(0.0008, 0.015, n)
    epsilon = rng.normal(0, 0.005, n)
    rendements_jour = rendements_jour_marché * 1.3 + epsilon +  0.0005
    beta, alpha = np.polyfit(rendements_jour_marché, rendements_jour, 1)
    residue = rendements_jour - (beta * rendements_jour_marché + alpha)
    moyennes = [rng.normal(0, 0.005, n).mean() for _ in range(1000)]
    erreur = residue.std() / np.sqrt(n)
    t = alpha / erreur
    print(f"erreur : {erreur}")
    print(f"t-stat : {t}")
    print(np.std(moyennes))
    print(0.005 / np.sqrt(n))
    print(f"beta : {beta}")
    print(f"alpha : {alpha}")
    print(f"residue : {residue.std()}")
    return {
        "beta": beta,
        "alpha": alpha,
        "residue_std": residue.std(),
        "t_stat": t,
        "erreur": erreur
    }
for n in [60, 500, 5000]:
    risk_measure(n, 3)