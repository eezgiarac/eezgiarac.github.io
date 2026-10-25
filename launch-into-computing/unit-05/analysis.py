from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


# File locations
base_folder = Path(__file__).parent
data_file = base_folder / "data" / "electric-car-sales-share.csv"
output_folder = base_folder / "outputs"

# Create the output folder if it does not exist
output_folder.mkdir(exist_ok=True)


# 1. LOAD THE DATASET
data = pd.read_csv(data_file)

print("Original columns:")
print(data.columns.tolist())

print("\nFirst five rows:")
print(data.head())


# Find the measurement column automatically
standard_columns = ["Entity", "Code", "Year"]
value_columns = [
    column for column in data.columns
    if column not in standard_columns
]

if len(value_columns) != 1:
    raise ValueError(
        "The electric vehicle value column could not be identified."
    )

value_column = value_columns[0]

# Give the measurement column a shorter name
data = data.rename(columns={value_column: "EV_Sales_Share"})


# 2. CLEAN THE DATASET
original_rows = len(data)

# Convert the year and EV share columns to numeric values
data["Year"] = pd.to_numeric(data["Year"], errors="coerce")
data["EV_Sales_Share"] = pd.to_numeric(
    data["EV_Sales_Share"],
    errors="coerce"
)

# Remove rows with missing essential values
clean_data = data.dropna(
    subset=["Entity", "Year", "EV_Sales_Share"]
).copy()

# Remove duplicate rows
clean_data = clean_data.drop_duplicates()

# Convert Year to an integer
clean_data["Year"] = clean_data["Year"].astype(int)

removed_rows = original_rows - len(clean_data)

print("\nData cleaning:")
print(f"Original rows: {original_rows}")
print(f"Clean rows: {len(clean_data)}")
print(f"Removed rows: {removed_rows}")


# Save the cleaned dataset
clean_data.to_csv(
    output_folder / "cleaned-ev-data.csv",
    index=False
)


# 3. BASIC ANALYSIS
selected_countries = [
    "China",
    "Germany",
    "Italy",
    "Norway",
    "United States"
]

selected_data = clean_data[
    clean_data["Entity"].isin(selected_countries)
].copy()

summary = (
    selected_data
    .groupby("Entity")["EV_Sales_Share"]
    .agg(["mean", "median", "min", "max"])
    .round(2)
)

print("\nSummary statistics:")
print(summary)

summary.to_csv(
    output_folder / "summary-statistics.csv"
)


# Calculate the relationship between year and EV sales share
correlations = (
    selected_data
    .groupby("Entity")
    .apply(
        lambda group: group["Year"].corr(
            group["EV_Sales_Share"]
        ),
        include_groups=False
    )
    .rename("Year_EV_Share_Correlation")
    .round(3)
)

print("\nCorrelation between year and EV sales share:")
print(correlations)

correlations.to_csv(
    output_folder / "correlations.csv"
)


# 4. LINE CHART: EV SALES SHARE OVER TIME
plt.figure(figsize=(10, 6))

for country in selected_countries:
    country_data = selected_data[
        selected_data["Entity"] == country
        ].sort_values("Year")

    plt.plot(
        country_data["Year"],
        country_data["EV_Sales_Share"],
        marker="o",
        label=country
    )

plt.title("Share of New Cars Sold That Are Electric")
plt.xlabel("Year")
plt.ylabel("Electric Car Sales Share (%)")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()

plt.savefig(
    output_folder / "ev-sales-trend.png",
    dpi=300
)

plt.close()


# 5. BAR CHART: TOP COUNTRIES IN THE LATEST YEAR
country_data = clean_data.dropna(subset=["Code"]).copy()
latest_year = country_data["Year"].max()

latest_data = country_data[
    country_data["Year"] == latest_year
    ]

top_countries = (
    latest_data
    .nlargest(10, "EV_Sales_Share")
    .sort_values("EV_Sales_Share")
)

plt.figure(figsize=(10, 6))

plt.barh(
    top_countries["Entity"],
    top_countries["EV_Sales_Share"],
    color="seagreen"
)

plt.title(
    f"Countries with the Highest Electric Car Sales Share ({latest_year})"
)
plt.xlabel("Electric Car Sales Share (%)")
plt.ylabel("Country")
plt.tight_layout()

plt.savefig(
    output_folder / "top-countries.png",
    dpi=300
)

plt.close()


print("\nAnalysis completed successfully.")
print("The results and charts are in the outputs folder.")