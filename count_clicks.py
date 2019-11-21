from sheet import Sheet
import bitly_api
from dotenv import load_dotenv
import os
import sys
load_dotenv()

access_token = os.getenv("access_token")
c = bitly_api.Connection(access_token = access_token)

table = Sheet("arac-tel","Sheet1")
row_count = len(table.worksheet.get_all_records())

for row_number in range(2, row_count):
	row = table.get_row(row_number)
	if row[3].isdigit() and int(row[3])>0 :
		table.update_one_cell(row_number, "clicked", c.clicks(shortUrl=row[1])[0]["global_clicks"])
	else:
		sys.exit("Dolu satırlar bitti.")
