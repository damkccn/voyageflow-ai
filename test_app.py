import unittest
from app import classify

class TestClassification(unittest.TestCase):
    def test_budget(self):
        self.assertEqual(classify("Quero um orçamento para viajar")["categoria"], "orcamento")
    def test_urgent(self):
        self.assertEqual(classify("Meu voo é amanhã")["prioridade"], "alta")
    def test_empty(self):
        with self.assertRaises(ValueError):
            classify("")

if __name__ == "__main__":
    unittest.main()
