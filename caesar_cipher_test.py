import unittest
import caesar_cipher as cipher


class Encryption_Test(unittest.TestCase):
    def setUp(self):
        self.my_message = ""

    def test_inputs_should_exist(self):
        self.assertIsNotNone(self.my_message)
    
    def test_input_should_be_string(self):
        self.assertIsInstance(self.my_message, str)

    def test_cipher_should_return_something(self):
        self.assertIsNotNone(cipher.cipher("encode", "a", 1))

if __name__ == "__main__":
    unittest.main()
