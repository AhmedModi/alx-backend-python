#!/usr/bin/env python3
"""Unit test for access_nested_map"""

import unittest
from unittest.mock import patch, Mock

class TestMemoize(unittest.TestCase):
    """Tests for the memoize decorator."""

    def test_memoize(self):
        """Ensure the method is only called once due to memoization."""

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            obj = TestClass()

            # First call (should call a_method)
            result1 = obj.a_property

            # Second call (should NOT call a_method again)
            result2 = obj.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()
