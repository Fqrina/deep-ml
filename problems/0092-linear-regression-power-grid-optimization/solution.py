import math
import numpy as np

PI = 3.14159


def power_grid_forecast(consumption_data):
    n = len(consumption_data)
    days = np.arange(1, n+1)

    fluctuation = 10 * np.sin(2 * PI * days / 10)
    detrended = np.array(consumption_data) - fluctuation

    X_b = np.column_stack([np.ones(n), days])
    beta = np.linalg.pinv(X_b.T @ X_b) @ X_b.T @ detrended
    day_15_base = np.array([1, 15]) @ beta

    day_15_fluctuation = 10 * math.sin(2 * PI * 15 / 10)
    day_15_total = day_15_base + day_15_fluctuation

    rounded_pred = round(day_15_total)
    final_forecast = math.ceil(rounded_pred * 1.05)

    return int(final_forecast)
