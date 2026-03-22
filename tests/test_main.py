import unittest
from unittest.mock import patch
from io import StringIO
from Tiles import main

silence = patch("sys.stdout", new_callable=StringIO)  # Decorator to silence test prints

class TestTilesMain(unittest.TestCase):

    @silence
    def test_valid_input_no_error(self, _):
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

    @silence
    def test_output_matches_assignment_format(self, mock_stdout):
        argv = ["Tiles.py", "1", "2", "0", "3", "4", "5", "6", "7", "8"]

        main(argv)

        self.assertEqual(
            mock_stdout.getvalue().splitlines(),
            [
                "Algorithm: BFS",
                "Path: 2 1",
                "Length: 2",
                "Expanded: 2",
                "Algorithm: A*",
                "Path: 2 1",
                "Length: 2",
                "Expanded: 2",
            ],
        )

if __name__ == "__main__":
    unittest.main()
