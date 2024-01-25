"""
Class for managing Google Sheet!
"""
import pygsheets

class GoogleSheet:
    """Manpulates Google Sheet"""
    def __init__(self):
        self.gc = pygsheets.authorize(service_file="credential.json")

    def blood_serum_manpulate(self, row_data):
        """Manpulates blood_serum sheet"""
        survey_url = 'https://docs.google.com/spreadsheets/d/1_Ss_aeXdhgw8DBfgv0pxv1zagu3XYRtlAX3iU5373ac/'
        sh = self.gc.open_by_url(survey_url)
        wks = sh[0]
        first_column = wks.get_col(1, include_tailing_empty=False)
        next_row = len(first_column) + 1
        wks.update_row(next_row, row_data)

    def health_monitor_manpulate(self, row_data):
        """Manpulates health_monitor sheet"""
        survey_url = 'https://docs.google.com/spreadsheets/d/1PUGV02AGF3ucyxD52xW85LVXGDtWBFHgqp1G0a21ZEE/'
        sh = self.gc.open_by_url(survey_url)
        wks = sh[0]
        first_column = wks.get_col(1, include_tailing_empty=False)
        next_row = len(first_column) + 1
        wks.update_row(next_row, row_data)    
    
    def section_insch_manpulate(self, search_value, value_to_update):
        """
        Manpulates section_insch sheet
        param row_data: list of data to be inserted
        param search_value: value to be searched in the sheet
        """
        survey_url = 'https://docs.google.com/spreadsheets/d/1WJxorIvfUh1ooBDwBTxp-xNypXk2e6WQk1lFyHatPg0/'
        sh = self.gc.open_by_url(survey_url)
        wks = sh[0]
        column_values = wks.get_col(1, include_tailing_empty=False)
        try:
            row_number = column_values.index(search_value) + 1  # 加 1 因為 index 從 0 開始但是行號從 1 開始
        except ValueError:
            return
        cells_to_update = []
        for col_letter, value in value_to_update.items():
            if value is None:
                value = '' 
            cell_pos = f'{col_letter}{row_number}'
            cell = pygsheets.Cell(cell_pos, value)
            cells_to_update.append(cell)
        wks.update_cells(cells_to_update)