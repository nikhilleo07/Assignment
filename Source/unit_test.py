import unittest
import os
from createcsv import create_csv_file
from openfile import open_log_file
from dict import find_vend

class TestDhcp(unittest.TestCase):
    
    def test_open_log_file(self):
        """Test method to check if file can be opened and read"""
        open_log_file_result = open_log_file("dhcpd.log")
        assert open_log_file_result != None    

    def test_create_csv_file(self):
        """Test method that checks whether a csv file is created as expected"""
        MAC_DETAILS = "luffy_zoro.csv"
        row_header =[('Anime', 'Main Character', 'Devil Fruit', 'Vice Captian')]
        to_csv_file_result = create_csv_file(MAC_DETAILS, row_header)
        assert os.path.exists(MAC_DETAILS) == True
    
    def test_find_vend(self):
        """Test method to vendor details check"""
        find_mac_result = find_vend("bc:5f:f4")
        self.assertEqual(find_mac_result, "ASROCK")
        
if __name__ == '__main__':
    unittest.main()
