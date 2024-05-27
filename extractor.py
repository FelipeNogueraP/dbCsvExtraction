import os
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import exc

# Load environment variables
load_dotenv()

# Get the database URL from the env variable
DATABASE_URL = os.getenv("DATABASE_URL")

# Debugging: Print the DATABASE_URL to ensure it's being read correctly
print(f"Database URL: {DATABASE_URL}")

# # Remove any surrounding quotes or extra spaces from the DATABASE_URL
# DATABASE_URL = DATABASE_URL.strip().strip('"').strip("'").strip('>')

# # Debugging: Print the cleaned DATABASE_URL
# print(f"Cleaned Database URL: {DATABASE_URL}")

try:
    # Create a connection to the database
    engine = create_engine(DATABASE_URL)

    # Query the database to extract data
    query = "SELECT * FROM defaultdb;"

    # Execute the query and load the data into pandas DataFrame
    df = pd.read_sql_query(query, engine)

    # Specify the output file
    output_file = "dataDB.csv"

    # Write the data to a CSV file
    df.to_csv(output_file, index=False)

    print(f"Data extracted and saved to {output_file}")

except exc.SQLAlchemyError as e:
    print(f"An error occurred while connecting to the database or executing the query: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")