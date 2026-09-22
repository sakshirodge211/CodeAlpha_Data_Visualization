import pandas as pd
import matplotlib.pyplot as plt

# Load analyzed dataset
df = pd.read_csv("books_eda.csv")

# Convert price to numeric
df["Price_Numeric"] = (
    df["Price"]
    .str.replace("£", "", regex=False)
    .astype(float)
)

# Convert rating words to numbers
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating_Numeric"] = df["Rating"].map(rating_map)


# ==========================================
# 1. Top 10 Most Expensive Books
# ==========================================

top_10 = df.nlargest(10, "Price_Numeric").sort_values(
    "Price_Numeric"
)

plt.figure(figsize=(10, 6))

plt.barh(
    top_10["Title"],
    top_10["Price_Numeric"],
    edgecolor="black"
)

plt.title("Top 10 Most Expensive Books")
plt.xlabel("Price (£)")
plt.ylabel("Book Title")

plt.tight_layout()
plt.savefig("top_10_expensive_books.png", dpi=300)
plt.show()


# ==========================================
# 2. Rating Distribution
# ==========================================

rating_counts = (
    df["Rating_Numeric"]
    .value_counts()
    .sort_index()
)

plt.figure(figsize=(8, 5))

plt.bar(
    rating_counts.index,
    rating_counts.values,
    edgecolor="black"
)

plt.title("Book Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Books")

plt.xticks([1, 2, 3, 4, 5])

plt.tight_layout()
plt.savefig("book_rating_distribution.png", dpi=300)
plt.show()


# ==========================================
# 3. Book Price Distribution
# ==========================================

plt.figure(figsize=(8, 5))

plt.hist(
    df["Price_Numeric"],
    bins=20,
    edgecolor="black"
)

plt.title("Book Price Distribution")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")

plt.tight_layout()
plt.savefig("book_price_distribution.png", dpi=300)
plt.show()


# ==========================================
# 4. Average Price by Rating
# ==========================================

average_price = (
    df.groupby("Rating_Numeric")["Price_Numeric"]
    .mean()
)

plt.figure(figsize=(8, 5))

plt.bar(
    average_price.index,
    average_price.values,
    edgecolor="black"
)

plt.title("Average Book Price by Rating")
plt.xlabel("Rating")
plt.ylabel("Average Price (£)")

plt.xticks([1, 2, 3, 4, 5])

plt.tight_layout()
plt.savefig("average_price_rating.png", dpi=300)
plt.show()


# ==========================================
# 5. Visualization Summary
# ==========================================

print("\n" + "=" * 50)
print("TASK 3 - DATA VISUALIZATION COMPLETED")
print("=" * 50)

print("\nTotal Books:", len(df))

print("\nCharts Created:")
print("1. Top 10 Most Expensive Books")
print("2. Book Rating Distribution")
print("3. Book Price Distribution")
print("4. Average Book Price by Rating")

print("\nVisualization files saved successfully!")