import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------
# Load Close column as string
# ---------------------------------
raw_close = np.genfromtxt(
    "stock_prices.csv",
    delimiter=",",
    skip_header=1,
    usecols=1,   
    dtype=str
)

# ---------------------------------
# Remove quotes and convert to float
# ---------------------------------
clean_close = np.char.strip(raw_close, '"')
close_prices = clean_close.astype(float)

# ---------------------------------
# Calculate daily returns (%)
# ---------------------------------
daily_returns = (close_prices[1:] - close_prices[:-1]) / close_prices[:-1] * 100

# ---------------------------------
# Mean and standard deviation
# ---------------------------------
mean_return = np.mean(daily_returns)
std_return = np.std(daily_returns)

print("Mean Daily Return:", mean_return)
print("Standard Deviation of Daily Returns:", std_return)

# ---------------------------------
# Top 5 positive & negative return days
# ---------------------------------
top_5_positive = np.argsort(daily_returns)[-5:][::-1] + 1
top_5_negative = np.argsort(daily_returns)[:5] + 1

print("Top 5 Positive Return Days (indices):", top_5_positive)
print("Top 5 Negative Return Days (indices):", top_5_negative)

# ---------------------------------
# Plot histogram using Matplotlib
# ---------------------------------
plt.figure(figsize=(8, 5))
plt.hist(daily_returns, bins=30)
plt.title("Histogram of Daily Stock Returns")
plt.xlabel("Daily Return (%)")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()