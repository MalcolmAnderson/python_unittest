import io
import contextlib
import unittest
import caesar_cipher as cipher
import string

f = None

class Encryption_Test(unittest.TestCase):
    def setUp(self):
        self.longMessage = True
        self.my_message = ""
        f = io.StringIO()

    def test_inputs_should_exist(self):
        self.assertIsNotNone(self.my_message)
    
    def test_input_should_be_string(self):
        self.assertIsInstance(self.my_message, str)

    def test_cipher_should_return_something(self):
        self.assertIsNotNone(cipher.engine("encode", "a", 1))
    
    def test_eng_should_return_same_len_str(self):
        term = "banana"
        self.assertEqual(len(term), len(cipher.engine("encode", "banana", 1)))
    
    def test_encode_1_a_should_return_b(self):
        expected = "b"
        actual = cipher.engine("encode", "a", 1)
        self.assertEqual(expected, actual)
    
    def test_output_should_be_string(self):
        #expected = "b"
        actual = cipher.engine("encode", "a", 1)
        self.assertIsInstance(actual, str)

    def test_shiftedCipher(self):
        abc = string.ascii_letters + string.punctuation + string.digits + " "
        actual  = abc[abc.find("c") + 1]
        expected = "d"
        self.assertEqual(expected, actual)
                                       

if __name__ == "__main__":
    unittest.main()
