import numpy as np

FUNCS = {                                    # name: (function, its derivative)
    "square": (lambda v: v ** 2, lambda v: 2 * v),
    "sin":    (np.sin, np.cos),
    "exp":    (np.exp, np.exp),
    "log":    (np.log, lambda v: 1 / v),
}

def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
    grad, v = 1.0, x
    for name in reversed(functions):         # innermost function first
        f, df = FUNCS[name]
        grad *= df(v)                        # derivative at the CURRENT inner value
        v = f(v)                             # becomes the input of the next one out
    return grad