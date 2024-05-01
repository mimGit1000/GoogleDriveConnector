import unittest
import DriveConn

class TestDriveConnector(unittest.TestCase):
    def setUp(self):
        self.conn = DriveConn.GSheetsConnector(doc_id='1RJZDp4indHYcGfPx0qkgsSdK4HpywhfEu2uaqgXV6Jk', service_name='sheets', service_ver='v4', client_secret='windtower-rework.json')

    def test_get_service(self):
        self.assertIsNotNone(self.conn.get_service(), "Service connect exisits")

if __name__ == '__main__':
    unittest.main()
