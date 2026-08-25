import pandas as pd

df = pd.read_csv(r"data/trades.csv")
pnl = df["pnl_brut"] - df["frais"]
p_gain = (pnl > 0).mean()
p_perte = 1 - p_gain
gain_moy = pnl[pnl > 0].mean()
perte_moyenne = pnl[pnl < 0].mean()
winrate = p_gain
loss_rate = p_perte


esp = p_gain * gain_moy + p_perte * perte_moyenne


print(f"espérance : {round(esp, 2)}")
print(f"win rate : {round(winrate.mean() * 100, 2)}%")
print(f"loss rate : {round(loss_rate.mean() * 100, 2)}%")
