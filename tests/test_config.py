import tempfile
import unittest
from pathlib import Path

from src.main import load_config

class TestConfig(unittest.TestCase):

    def test_missing_config_uses_default(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "missing.json"

            result = load_config(path)

            self.assertEqual(
                result,
                {"default_level": "ALL"}
            )

    def test_load_valid_config(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "config.json"

            path.write_text(
                '{"default_level": "ERROR"}',
                encoding="utf-8"
            )

            result = load_config(path)

            self.assertEqual(
                result,
                {"default_level": "ERROR"}
            )

    def test_reject_invalid_level(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "config.json"

            path.write_text(
                '{"default_level": "DEBUG"}',
                encoding="utf-8"
            )

            with self.assertRaises(ValueError):
                load_config(path)

    def test_invalid_json(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "config.json"

            path.write_text(
                '{"default_level": ',
                encoding="utf-8"
            )

            with self.assertRaises(ValueError):
                load_config(path)

if __name__ == "__main__":
    unittest.main()