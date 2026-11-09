import numpy as np
def online_simple_regression(xs, ys):
    n = len(xs)
    res = np.zeros((n, 2))
    mx = my = sxx = sxy = 0.0          # means and centred sums, not raw sums

    for i in range(n):
        x, y = xs[i], ys[i]
        k = i + 1

        dx = x - mx                    # uses the OLD means
        dy = y - my
        mx += dx / k                   # now move to the NEW means
        my += dy / k
        sxx += dx * (x - mx)           # old-mean factor times new-mean factor
        sxy += dx * (y - my)

        slope = sxy / sxx if sxx != 0 else 0
        intercept = my - slope * mx

        res[i] = [intercept, slope]

    return res