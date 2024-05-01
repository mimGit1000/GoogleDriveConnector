import sys
from DriveConn import DriveConnector

class GSheetsConnector(DriveConnector):

    def __init__(self, doc_id, conn_type='service_acct', conn_json='client_secret.json', scopes=['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive'], service_name='sheets', service_ver='v4'):
        super().__init__(service_name, service_ver, conn_type, conn_json, scopes)
        self.sheet_id = doc_id
        self.service = self.get_service()
        self.sheet = self.service.spreadsheets()

    @property
    def sheet_id(self):
        return self._sheet_id
    
    @sheet_id.setter
    def sheet_id(self, value):
        self._sheet_id = value

    def get_data_from_range(self, cell_range):
        try:
            result = self.service.spreadsheets().values().get(spreadsheetId=self.sheet_id, range=cell_range).execute()
            read_values = result.get('values', [])
        except:
            sys.exit()

        if not read_values:
            print('No data found in the Google Sheet')

        return read_values

    def write_to_single_range(self, cell_range, new_value):
        body = {}
        body['range'] = cell_range
        body['values'] = [ [new_value], ]

        try:
            self.service.spreadsheets().values().update(spreadsheetId=self.sheet_id, range=body['range'], valueInputOption='RAW', body=body).execute()
        except:
            print("Sheet not updated")

    def write_to_multiple_ranges(self, cell_range, cell_values, dimension='ROWS'):
        data = []
        for i in range(len(cell_ranges)):
            ValueRangeObject = {'range': cell_range[i],
                                'values': [[cell_values[i]]],
                                'majorDimension': dimension}
            data.append(ValueRangeObject)

        body = {}
        body['valueInputOption'] = 'RAW'
        body['data'] = data

        try:
            self.service.spreadsheets().values().batchUpdate(spreadsheetId=self.sheet_id, body=body).execute()
            print ('<p style="color:green">Google Sheet batch updated successfully.</p>')
        except:
            print ('<p style="color:red">Error batch updating the Google Sheet! {0}</p>'.format(sys.exc_info()))

    def append_sheet(self,data_range,values):
        body = {}
        body['range'] = data_range
        body['values'] = [values]

        try:
            self.service.spreadsheets().values().append(spreadsheetId=self.sheet_id, range=body['range'], valueInputOption='RAW', body=body).execute()
        except:
            print("Error updating Sheet")
    
    def get_last_row(self, sheet_range):
        last_row = 1 #set last row as row 1
        try:
            result = self.service.spreadsheets().values().get(spreadsheetId=self.sheet_id, range=sheet_range).execute()
            read_values = result.get('values', [])
            last_row = len(read_values)
    
        except:
            last_row = 1 #if exception return row 1
        
        return last_row
            
                