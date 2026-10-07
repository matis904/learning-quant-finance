import numpy as np
import pandas as pd

df = pd.read_csv(r"data/prix.csv")

def compute_features(x):
    m = x.pct_change(5)
    return (m - m.rolling(60).mean()) / m.rolling(60).std()

df["log_return"] = df.groupby("actif")["cloture"].transform(lambda x: np.log(x / x.shift(1)))
mom5_z = lambda x: (x.pct_change(5) - x.pct_change(5).rolling(60).mean()) / x.pct_change(5).rolling(60).std()
df["mom5"]       = df.groupby("actif")["cloture"].transform(mom5_z)
df["ecart_mm20"] = df.groupby("actif")["cloture"].transform(lambda x: x / x.rolling(20).mean() - 1)
df["vol_rel"]    = df.groupby("actif")["log_return"].transform(lambda r: r.rolling(5).std()) / df.groupby("actif")["log_return"].transform(lambda x: x.rolling(60).std())

for nom in ["mom5", "ecart_mm20", "vol_rel"]:
    veille = df.groupby("actif")[nom].shift(1)
    print(f"{nom} : moyenne={df[nom].mean():.4f}, σ={df[nom].std():.4f}, "
          f"corr avec le rendement du lendemain={veille.corr(df['log_return']):.4f}")
