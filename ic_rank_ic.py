import numpy as np 
from scipy.stats import rankdata
from feature import df

df["hasard"] = np.random.default_rng().normal(size=len(df))
def compute_IC_rankIC():
    for nom in ["mom5", "ecart_mm20", "vol_rel", "hasard"]:
        pred = df.groupby("actif")[nom].shift(1)
        reel = df["log_return"]
        ok = pred.notna() & reel.notna()
        pred, reel = pred[ok], reel[ok]
        ic =  np.corrcoef(pred, reel)[0, 1]
        t = ic * len(pred) ** 0.5
        ric =  np.corrcoef(rankdata(pred), rankdata(reel))[0, 1]
        ics = []

        pred = np.array_split(pred.to_numpy(), 5)
        reel = np.array_split(reel.to_numpy(), 5)
        for p, r in zip(pred, reel):
            ics.append(np.corrcoef(p, r)[0, 1])
        tstat_ics = lambda: np.mean(ics) / (np.std(ics) / np.sqrt(len(ics)))
        print(nom, ic)
        print(f"IC de {nom} {ic :.4f} t stats = {t :.4f} Rank IC = {ric :.4f} t stats IC 20 = {tstat_ics() :.4f} IC 20 = {np.mean(ics) :.4f} t stats ICS = {tstat_ics() :.4f}")
    return ric, ic, t
compute_IC_rankIC()