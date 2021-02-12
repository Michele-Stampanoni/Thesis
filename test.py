### Testing graph functions:


import unittest 
import functions
import excel_data

class Test(unittest.TestCase):
    
        
    def test_nvf_reed(self):
        self.assertEqual(functions.nvf_reed(9), 512)
        
    def test_nvf_metcalfe(self):
        self.assertEqual(functions.nvf_metcalfe(7), 49)
           
if __name__ == '__main__':
    unittest.main()
    
    
    
        
        
        
        
