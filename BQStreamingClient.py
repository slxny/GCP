from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

# TODO(developer): Set table_id to the ID of table to append to.
table_id = "PROJECT_ID.DATASET_ID.TABLE_ID"

# Make an API request.
errors = client.insert_rows_json(table_id, rows_to_insert)  

if errors == []:
    print("New rows have been added! Nice.")

#all other cases:
else:
    print("Encountered errors while inserting rows: {}".format(errors))
