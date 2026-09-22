import numpy as np

rng = np.random.default_rng(7)
data = rng.standard_t(3, 1000)

z = (data - data.mean()) / data.std()
skewness = (z ** 3).mean()
kurtosis = (z ** 4).mean()
wanted = 0.003 * len(data)
observed = np.sum(np.abs(z) > 3)

print(f"skewness : {skewness:.3f}")
print(f"kurtosis : {kurtosis:.3f}")
print(f"observed |z| > 3 : {observed} / {len(data)} (wanted : {wanted:.1f})")


