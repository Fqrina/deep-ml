import numpy as np


def logit_margin(z, t):
  z = np.asarray(z, dtype=np.float64)
  zt = z[t]
  z_others = np.delete(z, t)
  max_val = np.max(z_others)
  log_sum = max_val + np.log(np.sum(np.exp(z_others - max_val)))
  return float(zt - log_sum)


def precision_cliff(dtype):
  dt = np.dtype(dtype)
  low = 0.0
  high = 100.0

  for _ in range(100):
    mid = (low + high) / 2.0
    exp_val = np.array(np.exp(-mid), dtype=dt)
    if np.array(1.0, dtype=dt) + exp_val == np.array(1.0, dtype=dt):
      high = mid
    else:
      low = mid

  return round(float(high), 4)