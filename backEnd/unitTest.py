import unittest
import subprocess
import json

# Global variable to be used by Unit test
cmd_lst = ['curl' ,'http://localhost:5001/list']
nam = 'madam'

# Method to be used by Unit test
def dicts_equal(d1,d2):
    """ return True if all keys and values are the same """
    return all(k in d2 and d1[k] == d2[k]
               for k in d1) \
        and all(k in d1 and d1[k] == d2[k]
               for k in d2)

# Method to test the list api
def get_list(cmd_list):
    output = subprocess.check_output(cmd_lst)
    l =  output.decode()
    x = json.loads(l)
    return x

# Method to test if a given string is palindrom
def isPalindrom(nam):
    l = get_list(cmd_lst)
    ln = len(l)
    for i in range(ln):
        if l[i]['name'] == nam:
            if nam == nam[::-1]:
                return True
            else:
                return False

# Method to compare two list
def list_equal(x,y):
   return x == y
   
class SimpleTest(unittest.TestCase):
    # Initialize test setup data
    def setUp(self):
        self.msg = [{'name': 'madam'}, {'name': 'Raam'}, {'name': 'Ganesh'}, {'name': 'aba'}, {'name': 'sam'}]
    # Text exeectuion is completed 
    def tearDown(self):
        print("Execution Done!!\n")
    # Start testing api
    # Test the list of messages returned by api
    def testlist_api(self):
      self.assertEqual(list_equal(get_list(cmd_lst),self.msg),True)
    
    # Test if a gvime string is palindrom via pai
    def testPalindrom_api(self):
      self.assertEqual(isPalindrom(nam),True)

    # Add more test cases here


# Bebin the unit test from here
if __name__ == '__main__':
   unittest.main()
