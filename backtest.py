import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"data/prix.csv")
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
for ax, a in zip(axes, ["AETH", "BTCX", "STAB"]):
    sous = df[df["actif"] == a]
    ma20 = sous["cloture"].rolling(20).mean()
    signal = (sous["cloture"] > ma20).astype(int).shift(1).fillna(0)
    print(f"backtest pour {a} :") 
    prix = sous["cloture"].tolist()
    rendements_trades = []
    def backtest(signal, prix):
        cash, pos = 1000.0, 0.0
        print(f"départ {a} : cash={cash}, pos={pos}") # prouf of reset for each tickers
        bh = 1000.0 * prix[-1] / prix[0] #buy and hold
        equity_curve = []
        for i in range(len(prix)):
            if signal[i] == 1 and pos == 0:
                pos = cash / prix[i]
                cash = 0.0
                entree = prix[i]
            elif signal[i] == 0 and pos > 0:
                cash = pos * prix[i]
                rendements_trades.append((prix[i] - entree) / entree)
                pos = 0.0
            valeur = cash + pos * prix[i]   # valeur du portefeuille CE jour-là, en cash ou en position
            equity_curve.append(valeur)
        pnl = cash + pos * prix[-1]
        equity_curve = np.array(equity_curve)
        pic = np.maximum.accumulate(equity_curve)
        dd = (equity_curve - pic) / pic
        drawdown_max = dd.min() * 100
        win_rate = sum(1 for r in rendements_trades if r > 0) / len(rendements_trades) * 100
        erreur = np.std(rendements_trades) / len(rendements_trades) ** 0.5
        print(round(pnl, 2))
        print(f"drawdown max : {round(drawdown_max, 2)}%")
        print(f"equity curve : {round(equity_curve[-1], 2)}")
        print(f"win rate : {round(win_rate, 2)}%")
        print(len(rendements_trades))
        print(f"T-Stat : {round(np.mean(rendements_trades) / erreur, 2)}")
        print(f"buy and hold : {round(bh, 2)}")
        idx_creux = np.argmin(dd)
        ax.scatter(idx_creux, equity_curve[idx_creux], color="red", zorder=5, s=40)
        idx_pic = np.argmax(pic[:idx_creux+1] == pic[idx_creux])  # le sommet avant ce creux
        ax.plot([idx_pic, idx_creux], [pic[idx_creux], equity_curve[idx_creux]], color="red", linestyle="--", linewidth=1.2)
        ax.annotate(f"DD max: {round(drawdown_max, 1)}%",
            xy=(idx_creux, equity_curve[idx_creux]),
            xytext=(idx_creux, equity_curve[idx_creux] * 0.85),
            color="red", fontsize=8, ha="center",
            arrowprops=dict(arrowstyle="->", color="red", lw=1))
        ax.plot(equity_curve, label="Strategy")
        ax.plot([0, len(equity_curve)-1], [bh, bh], color="blue", linestyle="--", label="Buy and Hold")
        ax.set_title(a)
        ax.legend()
    backtest(signal.tolist(), prix)
plt.tight_layout()
plt.show() #visualisation
