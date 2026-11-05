PI = 3.14159

import math
import numpy as np

def power_grid_forecast(consumption_data):
    consumption_data = np.array(consumption_data)
    i = np.arange(1, len(consumption_data) + 1)   # days 1..10

    def fluc(days):
        return 10 * np.sin(2 * np.pi * days / 10)

    # 1) Remove the daily fluctuation
    no_fluc = consumption_data - fluc(i)

    # 2) Linear regression on the detrended data
    m, c = np.polyfit(i, no_fluc, 1)

    # 3) Predict day 15's base consumption
    y = m * 15 + c

    # 4) Add the day 15 fluctuation back (about 0, since sin(3π) = 0)
	fluc_y = y + fluc(15)

    # 5) 5% safety margin, rounded up
	final = int(math.ceil(1.05 * fluc_y))

    # 6) Return an integer
    return final