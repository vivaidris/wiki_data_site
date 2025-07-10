import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import uniform_filter1d

ypoints = np.array([
    29390240489, 25761512520, 26570111288, 25375399127, 24687776934,
    22502788885, 22944011876, 23917158773, 22956185963, 23526882938,
    23982688442, 23810878374, 25862536862, 22828399708, 25060822696,
    24414584166, 26420439216, 25000185121
])

months = ['Jan 2024', 'Feb 2024', 'Mar 2024', 'Apr 2024', 'May 2024', 'Jun 2024', 'Jul 2024', 'Aug 2024', 'Sep 2024', 'Oct 2024', 'Nov 2024', 'Dec 2024',
 'Jan 2025', 'Feb 2025', 'Mar 2025', 'April 2025', 'May 2025', 'June 2025']

x = np.arange(len(ypoints))

error = 0.01 * ypoints

smoothed_error = uniform_filter1d(error, size=5)

plt.figure(figsize=(10, 6))
plt.plot(x, ypoints, label='Values', marker='o')

plt.fill_between(x, ypoints - smoothed_error, ypoints + smoothed_error,
                 alpha=0.15, label='Smoothed Inaccuracy Band')

plt.xticks(ticks=x, labels=months, rotation=45)

plt.xlabel("Months")
plt.ylabel("Views (1x10^10)")
plt.title("Wikipedia Monthly Views (Jan 2024 - Jun 2025)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

