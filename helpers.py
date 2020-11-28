"""Helper functions"""
import unittest


def to_str(bytes_or_str):
    """Take bytes or str instance and always return a str"""
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value # Instance of str


def to_bytes(bytes_or_str):
    """Take bytes or str instance and always return a bytes"""
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value # Instance of bytes


class TestMethods(unittest.TestCase):
    """Assert correctness"""

    def test_to_str(self):
        """to_str should always return string instances"""
        self.assertEqual(to_str(b'bytes'), 'bytes', msg=None)
        self.assertEqual(to_str('string'), 'string', msg=None)

    def test_to_bytes(self):
        """to_bytes should always return bytes instances"""
        self.assertEqual(to_bytes(b'bytes'), b'bytes', msg=None)
        self.assertEqual(to_bytes('string'), b'string', msg=None)


if __name__ == '__main__':
    unittest.main()
