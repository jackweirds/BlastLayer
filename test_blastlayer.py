# test_blastlayer.py
"""
Tests for BlastLayer module.
"""

import unittest
from blastlayer import BlastLayer

class TestBlastLayer(unittest.TestCase):
    """Test cases for BlastLayer class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlastLayer()
        self.assertIsInstance(instance, BlastLayer)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlastLayer()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
