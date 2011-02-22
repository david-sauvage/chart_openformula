import unittest

from objects import LogicalExpression, Number
from logic import AND, OR, TRUE, FALSE, NOT, IF

class TestOpenFormulaFunctions(unittest.TestCase):
    
#Logicals operations
    def test_of_and(self):
        expression = AND(LogicalExpression("1>2"))
        self.assertEqual(str(expression), "AND(1>2)")
        expression = AND(LogicalExpression("2=2"), LogicalExpression("3>2"))
        self.assertEqual(str(expression), "AND(2=2 ; 3>2)")
        self.assertRaises(TypeError, AND, 2, 3)

    def test_of_or(self):
        expression = OR(LogicalExpression("1>2"))
        self.assertEqual(str(expression), "OR(1>2)")
        expression = OR(LogicalExpression("2=2"), LogicalExpression("3>2"))
        self.assertEqual(str(expression), "OR(2=2 ; 3>2)")
        self.assertRaises(TypeError, OR, 2, 3)

    def test_of_true(self):
        self.assertEqual(str(TRUE()), "TRUE()")

    def test_of_false(self):
        self.assertEqual(str(FALSE()), "FALSE()")

    def test_of_not(self):
        expression = NOT(LogicalExpression("1>2"))
        self.assertEqual(str(expression), "NOT(1>2)")
        self.assertRaises(TypeError, OR, 2)

    def test_of_if(self):
        expression = IF(LogicalExpression("1>2"), Number("3"), Number("4"))
        self.assertEqual(str(expression), "IF(1>2;3;4)")
        self.assertRaises(TypeError, IF, "1>2", 1, 2)

if __name__ == '__main__':
    unittest.main()


                          


                          
