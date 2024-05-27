#!/bin/bash

# Database connection parameters
DATABASE_URL="postgresql://user:password@localhost:5432/dbname"

# Get the list of tables
tables=$(psql "$DATABASE_URL" -Atc "SELECT tablename FROM pg_tables WHERE schemaname = 'public';")

# Loop through the tables and export each to a CSV file
for table in $tables; do
    echo "Exporting table: $table"
    psql "$DATABASE_URL" -c "\copy (SELECT * FROM \"$table\") TO '${table}.csv' WITH CSV HEADER;"
done

echo "Export completed."

