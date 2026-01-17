import unittest
from Tiles import main

class TestTilesMain(unittest.TestCase):
    
    def test_valid_input_no_error(self):
        argv = ["Tiles.py", "1","2","3","4","5","6","7","8","0"]
        try:
            main(argv)
        except ValueError:
            self.fail("main() raised ValueError unexpectedly")

    def test_invalid_argument_count(self):
        argv = ["Tiles.py", "1", "2"]
        with self.assertRaises(ValueError):
            main(argv)

    def test_invalid_numbers(self):
        argv = ["Tiles.py", "1","2","3","4","5","6","7","8","8"]
        with self.assertRaises(ValueError):
            main(argv)

    def test_non_integer_input(self):
        argv = ["Tiles.py", "1","2","3","4","five","6","7","8","0"]
        with self.assertRaises(ValueError):
            main(argv)

if __name__ == "__main__":
    unittest.main()