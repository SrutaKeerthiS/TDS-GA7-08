# analysis.py
import pandas as pd
import matplotlib.pyplot as plt

# Email for verification
EMAIL = "22f3002573@ds.study.iitm.ac.in"

# Quarterly data
data = {
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "Efficiency": [76.89, 76.48, 73.89, 81.36]
}

# Industry benchmark
industry_target = 90

# Create DataFrame
df = pd.DataFrame(data)

# Compute average
average_eff = df["Efficiency"].mean()
print(f"Average efficiency: {average_eff:.2f}")

# Visualization
plt.figure(figsize=(8,6))
plt.plot(df["Quarter"], df["Efficiency"], marker="o", label="Equipment Efficiency")
plt.axhline(y=industry_target, color="r", linestyle="--", label="Industry Target (90)")
plt.title("Quarterly Equipment Efficiency vs Industry Target")
plt.xlabel("Quarter")
plt.ylabel("Efficiency Rate")
plt.legend()
plt.grid(True)
plt.savefig("efficiency_trend.png")

# HTML wrapper for GitHub Pages preview (optional)
with open("report.html", "w") as f:
    f.write(f"""
    <html>
    <head><title>Manufacturing Performance Analysis</title></head>
    <body>
    <h2>Equipment Efficiency Trend (2024)</h2>
    <p>Email Verification: {EMAIL}</p>
    <p>Average Efficiency: {average_eff:.2f} (Industry Target: {industry_target})</p>
    <img src="efficiency_trend.png" width="600">
    </body>
    </html>
    """)
