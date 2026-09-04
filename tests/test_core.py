import unittest
from urlprobe.core import normalize
class Tests(unittest.TestCase):
 def test_default_scheme(self): self.assertEqual(normalize('example.com'),'https://example.com/')
if __name__=='__main__': unittest.main()
