# --- cell 1 ---
import numpy as np


def optimizer_step(param, grad, state, lr, momentum=0.9):
    param = np.asarray(param, dtype=np.float64)
    grad = np.asarray(grad, dtype=np.float64)

    step = state.get("step", 0) + 1
    velocity = state.get("velocity", np.zeros_like(param))

    velocity = momentum * velocity + grad
    new_param = param - lr * velocity

    new_state = {
        "step": step,
        "velocity": velocity,
    }
    return new_param, new_state