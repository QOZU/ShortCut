# test_shortcut.py
"""
Tests for ShortCut module.
"""

import unittest
from shortcut import ShortCut

class TestShortCut(unittest.TestCase):
    """Test cases for ShortCut class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ShortCut()
        self.assertIsInstance(instance, ShortCut)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ShortCut()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
