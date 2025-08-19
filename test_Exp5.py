import unittest
from PS_IV_Exp5 import Exp5
class TestExp5(unittest.TestCase):
    def setUp(self):
        self.app = Exp5.test_client()

    def test_hello(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
    
if __name__ == '__main__':
    unittest.main()