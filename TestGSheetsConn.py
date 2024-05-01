import unittest
from GSheetsConn import GSheetsConnector

class TestGSheetsConnector(unittest.TestCase):
    def setUp(self):
        self.sheet_conn = GSheetsConnector(doc_id='1RJZDp4indHYcGfPx0qkgsSdK4HpywhfEu2uaqgXV6Jk', conn_type='service_acct', conn_json='windtower-rework.json')

    def test_get_data_from_range(self):
        pass

    def test_write_to_single_range(self):
        self.sheet_conn.write_to_single_range(cell_range='Test!C3', new_value=55)
        self.assertEqual(self.sheet_conn.get_data_from_range(cell_range='Test!C3')[0][0],'55')
    
    def test_get_last_row(self):
        self.assertGreaterEqual(self.sheet_conn.get_last_row(sheet_range="Test!A1:C"), 1)
    
    def test_append_sheet(self):
        self.sheet_conn.append_sheet(data_range='Test!A1:C', values=["2024-04-17 11:34:00", 128, 93])
        new_row = self.sheet_conn.get_data_from_range('Test!A1:C')[self.sheet_conn.get_last_row(sheet_range='Test!A1:C')-1]
        self.assertEqual(new_row,["2024-04-17 11:34:00", '128', '93'])
    
    
                          

if __name__ == "__main__":
    unittest.main()