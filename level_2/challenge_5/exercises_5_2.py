import pandas as pd
import os
import glob

# panderas and pandas to work with dataframes directly

# To perform a simple ETL (Extract, Transform, Load) using Python and the Pandas library,
# we will follow these steps:

# Extract:
# Read the data from a JSON file.

# Transform:
# Concatenate the extracted data into a single DataFrame
# and apply a transformation. The specific transformation
# will depend on the data, but we will assume a simple operation as an example.

# Load:
# Save the resulting DataFrame into a CSV or PARQUET file.


# Extract function
def extract_data(folder: str) -> pd.DataFrame:
    # List all json files in folder
    json_files = glob.glob(os.path.join(folder, "*.json"))
    # print(json_files)

    # Read json files
    df_list = [pd.read_json(file) for file in json_files]
    # print(df_list)

    # Concat df in pandas
    df = pd.concat(df_list, ignore_index=True)
    print(df.head())

    return df


# Transform function
def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    print(df.head())
    return df


# Load function
def load_data(df: pd.DataFrame, output_file: str, format: str = "csv") -> None:
    if format == "csv":
        df.to_csv(output_file, index=False)
    elif format == "parquet":
        df.to_parquet(output_file, index=False)
    else:
        raise ValueError("Invalid format. Choose 'csv' or 'parquet'.")
    print(f"Data loaded to {output_file}")


def pipeline(folder, output_file, format):
    data = extract_data(folder)
    transformed_data = transform_data(data)
    load_data(transformed_data, output_file, format)
    print("ETL completed successfully")


if __name__ == "__main__":
    folder = "data"
    output_file = "output.parquet"
    format = "parquet"
    pipeline(folder, output_file, format)
