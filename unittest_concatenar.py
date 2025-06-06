import unittest
from concatenar import concatenar

class TestConcatenar(unittest.TestCase):
    def test_concatenar(self):
        self.assertEqual(concatenar("Ho", "la Mundo"), "Hola Mundo")

if __name__ == "__main__":
    unittest.main()