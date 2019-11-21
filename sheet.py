import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import bitly_api
import settings

abs_path_of_current_file = os.path.dirname(os.path.realpath(__file__))

class Sheet:
	def __init__(self, workspace, sheet_name):
		scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
		credentials = ServiceAccountCredentials.from_json_keyfile_name(abs_path_of_current_file+settings.CREDENTIALS, scope)
		gc = gspread.authorize(credentials)
		wks = gc.open(workspace)
		self.sheets = wks.worksheets()
		self.worksheet = wks.worksheet(sheet_name)
		# Gets non empty cells in first row
		self.columns = [col for col in self.worksheet.row_values(1) if col]

	def write(self, ilan):
		existing_row = self.is_exist(ilan["ilan_no"], 1)
		if(existing_row):
			# Bu ilanno ile bir kayıt var.
			#print("Found something at R%sC%s" % (cell.row, cell.col))
			print("Something found: ", existing_row)
	
			# Fiyat farklı ise update et
		else:
			# Tabloda yok. insert new row
			row = []
			# son kolon, FARK(%) kolonunu dışarıda bırakıyoruz.
			for column in self.columns[:-1]:
				row.append(ilan[column])
			
			# Bir satır yazmadan önce bir tane boş satır oluşturuyor
			# self.worksheet.add_rows(1)
			self.worksheet.append_row(row)

	def is_exist(self, aranacak_sey, hangi_kolonda):
		# aranacak seyi hangi kolonda aramak istiyorsan
		try:
			for sheet in self.sheets:
				# hangi_kolonda kolonundaki bütün verileri ilk satırdakini hariç tutarak alıyoruz. İntegera çeviriyoruz.
				values_list = list(map(int, sheet.col_values(hangi_kolonda)[1:]))
				print("ARANACAKSEY: ",type(aranacak_sey), aranacak_sey)
				print("LEN_VALUESLIST: ",len(values_list))
				if aranacak_sey in values_list:
					row_number = values_list.index(aranacak_sey)+1
					row = self.worksheet.row_values(row_number)
					return row
			return False
		except gspread.exceptions.CellNotFound as e:
			print(e)
			return True

	def get_row(self, starting_row=2):
		# list_of_lists = table.worksheet.get_all_records()
		# print(list_of_lists)
		row = self.worksheet.row_values(starting_row)
		return row

	def get_value_from(self, column_name):
		column_index = self.columns.index(column_name) + 1
		row_index = 2
		return self.worksheet.cell(row_index, column_index).value


	def first_empty_row(self, column_name):
		"""
		column_name kolonundaki ilk boş hücrenin satır numarasını döndürür
		"""
		list_of_cells = self.worksheet.col_values(self.columns.index(column_name)+1)
		return len(list_of_cells)+1

	def update_one_cell(self, row_number, column_name, update_value):
		column_number = self.columns.index(column_name)+1
		self.worksheet.update_cell(row_number, column_number, update_value)


