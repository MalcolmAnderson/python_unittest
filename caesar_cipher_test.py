import unittest


class Encryption_Test(unittest.TestCase):
    def setUp(self):
        self.my_message = 0

    def test_inputs_should_exist(self):
        self.assertIsNotNone(self.my_message)


if __name__ == "__main__":
    unittest.main()
