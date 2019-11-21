from sheet import Sheet
import bitly_api
from dotenv import load_dotenv
import os
load_dotenv()

access_token = os.getenv("access_token")
c = bitly_api.Connection(access_token = access_token)

table = Sheet("arac-tel","Sheet1")

raw_video_url = table.get_value_from("youtube_url")
print(raw_video_url)
starting_row = table.first_empty_row("shortened-video-url")
end_row = starting_row + 30

for i in range(end_row-starting_row):
	phone_col_number = table.columns.index("phone")+1
	phone = table.worksheet.cell(starting_row+i, phone_col_number).value
	shortened_dict = c.shorten(raw_video_url+"&r="+phone, preferred_domain = "j.mp")
	print(shortened_dict["url"])
	table.update_one_cell(starting_row+i, "shortened-video-url", shortened_dict["url"])

