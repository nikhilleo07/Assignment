import unittest
import os
import sys

sys.path.append("..")
from Source.createcsv import create_csv_file

class TestDhcp(unittest.TestCase):
    def test_find_mac(self):
        """Test method to check the vendor is returned correctly for a give OUI number"""
        get_mac_vendor_result = find_mac("18:68:cb:45:1a:ae")
        self.assertEqual(get_mac_vendor_result, "HANGZHOU")
    
    def test_open_dhcpd_log(self):
        """Test method to check if file can be opened and read"""
        open_file_result = open_dhcpd_log("./dhcpd.log")
        assert open_file_result != None    

    def test_to_csv_file(self):
        """Test method that checks whether a csv file is created as expected"""
        MAC_DETAILS = "luffy_zoro.csv"
        row_header =[('Anime', 'Main Character', 'Devil Fruit', 'Vice Captian')]
        to_csv_file_result = to_csv_file(MAC_DETAILS, row_header)
        assert os.path.exists(MAC_DETAILS) == True
        
if __name__ == '__main__':
    unittest.main()