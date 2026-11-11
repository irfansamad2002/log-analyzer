import unittest
from src.analyzer import filter_log_entries
from src.analyzer import count_log_levels

class TestLogAnalyzer(unittest.TestCase):

    def test_count_log_levels(self):
        sample = """
[INFO] Application started
[WARNING] Disk space low
[ERROR] Database failed
[ERROR] Payment failed
"""

        result = count_log_levels(sample)

        expected = {
            "INFO": 1,
            "WARNING": 1,
            "ERROR":2
        }

        self.assertEqual(result, expected)

    def test_empty_logs(self):
        result = count_log_levels("")

        expected = {
            "INFO":0,
            "WARNING":0,
            "ERROR":0
        }

        self.assertEqual(result, expected)

    def test_filter_error_entries(self):
        sample = """
[INFO] Application started
[ERROR] Database failed
[WARNING] Disk space low
[ERROR] Payment failed
"""

        result = filter_log_entries(sample, "ERROR")

        expected = [
            "[ERROR] Database failed",
            "[ERROR] Payment failed"
        ]

        self.assertEqual(result, expected)

    def test_invalid_log_level(self):
        with self.assertRaises(ValueError):
            filter_log_entries("[ERROR] Database failed", "DEBUG")

if __name__ == "__main__":
    unittest.main()