import io
import csv

def store_records(records: list):
    # Create an in-memory file
    output = io.StringIO()

    # Write to the in-memory file as you would a normal file
    writer = csv.writer(output)
    writer.writerow(['Description', 'Price', 'Rating', 'Amount of reviews', 'Url'])
    writer.writerows(records)

    # Move to the start of the in-memory file before returning
    output.seek(0)

    return output  # Return the in-memory file object