import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

# ── Load Data ────────────────────────────────────
df = pd.read_excel("CodeAlpha TASK-1.xlsx")
print("=" * 55)
print("       BOOKS DATASET - EDA ANALYSIS")
print("=" * 55)

# ── 1. Data Structure ────────────────────────────
print("\n📋 1. DATA STRUCTURE")
print(f"   Rows    : {df.shape[0]}")
print(f"   Columns : {df.shape[1]}")
print(f"\n   Column Names & Data Types:")
print(df.dtypes)

print(f"\n   Null Values:")
print(df.isnull().sum())

print(f"\n   First 5 rows:")
print(df.head())

# ── 2. Meaningful Questions ──────────────────────
print("\n❓ 2. MEANINGFUL QUESTIONS & ANSWERS")

print(f"\n   Q1: Total books in dataset?")
print(f"   A : {len(df)} books")

print(f"\n   Q2: Average price?")
print(f"   A : £{df['Price (£)'].mean():.2f}")

print(f"\n   Q3: Cheapest book?")
cheapest = df.loc[df['Price (£)'].idxmin()]
print(f"   A : {cheapest['Title']} - £{cheapest['Price (£)']:.2f}")

print(f"\n   Q4: Most expensive book?")
expensive = df.loc[df['Price (£)'].idxmax()]
print(f"   A : {expensive['Title']} - £{expensive['Price (£)']:.2f}")

print(f"\n   Q5: How many 5-star books?")
five_star = df[df['Rating (1-5)'] == 5]
print(f"   A : {len(five_star)} books")

print(f"\n   Q6: Rating distribution?")
print(df['Rating (1-5)'].value_counts().sort_index())

# ── 3. Statistics ────────────────────────────────
print("\n📊 3. STATISTICAL SUMMARY")
print(df[['Price (£)', 'Rating (1-5)']].describe())

# ── 4. Visualizations ────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Books Dataset - EDA Analysis", fontsize=16, fontweight='bold')

# Chart 1: Rating Distribution (Bar)
rating_counts = df['Rating (1-5)'].value_counts().sort_index()
colors = ['#FF6B6B', '#FFA07A', '#FFD700', '#90EE90', '#4169E1']
axes[0, 0].bar(rating_counts.index, rating_counts.values, color=colors)
axes[0, 0].set_title('Rating Distribution', fontweight='bold')
axes[0, 0].set_xlabel('Rating (Stars)')
axes[0, 0].set_ylabel('Number of Books')
for i, v in enumerate(rating_counts.values):
    axes[0, 0].text(rating_counts.index[i], v + 0.5, str(v), ha='center', fontweight='bold')

# Chart 2: Price Distribution (Histogram)
axes[0, 1].hist(df['Price (£)'], bins=20, color='#2E86AB', edgecolor='white')
axes[0, 1].set_title('Price Distribution', fontweight='bold')
axes[0, 1].set_xlabel('Price (£)')
axes[0, 1].set_ylabel('Number of Books')
axes[0, 1].axvline(df['Price (£)'].mean(), color='red', linestyle='--', label=f"Avg: £{df['Price (£)'].mean():.2f}")
axes[0, 1].legend()

# Chart 3: Avg Price per Rating (Bar)
avg_price = df.groupby('Rating (1-5)')['Price (£)'].mean()
axes[1, 0].bar(avg_price.index, avg_price.values, color='#A8DADC', edgecolor='gray')
axes[1, 0].set_title('Average Price per Rating', fontweight='bold')
axes[1, 0].set_xlabel('Rating (Stars)')
axes[1, 0].set_ylabel('Average Price (£)')
for i, v in enumerate(avg_price.values):
    axes[1, 0].text(avg_price.index[i], v + 0.3, f"£{v:.1f}", ha='center', fontweight='bold')

# Chart 4: Rating Pie Chart
axes[1, 1].pie(rating_counts.values, labels=[f"{i} Star" for i in rating_counts.index],
               autopct='%1.1f%%', colors=colors, startangle=90)
axes[1, 1].set_title('Rating Share (%)', fontweight='bold')

plt.tight_layout()
plt.savefig("eda_charts.png", dpi=150, bbox_inches='tight')
plt.show()
print("\n✅ Charts saved as 'eda_charts.png'")

# ── 5. Anomalies / Issues ────────────────────────
print("\n⚠️  5. DATA ISSUES / ANOMALIES")
print(f"   Duplicate titles  : {df['Title'].duplicated().sum()}")
print(f"   Missing prices    : {df['Price (£)'].isnull().sum()}")
print(f"   Missing ratings   : {df['Rating (1-5)'].isnull().sum()}")
print(f"   Price below £10   : {len(df[df['Price (£)'] < 10])} books")
print(f"   Price above £50   : {len(df[df['Price (£)'] > 50])} books")

print("\n✅ EDA Complete!")