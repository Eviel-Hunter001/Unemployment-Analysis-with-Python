import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("default")

df = pd.read_csv("Unemployment_in_India_cleaned.csv", parse_dates=["Date"])
df.head()

#trend 
plt.figure(figsize=(12,6))
sns.lineplot(data=df.sort_values("Date"),
             x="Date",
             y="Estimated Unemployment Rate (%)")
plt.title("Unemployment Rate Trend Over Time in India")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#regin wise analysis
region_avg = df.groupby("Region")["Estimated Unemployment Rate (%)"].mean().sort_values(ascending=False)

plt.figure(figsize=(12,7))
region_avg.plot(kind="bar", color="skyblue")
plt.title("Average Unemployment Rate by Region")
plt.ylabel("Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#month wise analysis
month_avg = df.groupby("Month_Name")["Estimated Unemployment Rate (%)"].mean()

# proper month order
order = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
month_avg = month_avg.reindex(order)

plt.figure(figsize=(10,6))
month_avg.plot(kind="bar")
plt.title("Average Unemployment Rate by Month")
plt.ylabel("Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#hitmap
plt.figure(figsize=(8,6))
sns.heatmap(df[["Estimated Unemployment Rate (%)",
                "Estimated Employed",
                "Estimated Labour Participation Rate (%)"]].corr(),
            annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
