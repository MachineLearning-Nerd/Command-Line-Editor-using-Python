import math
import unittest
from test_common import *
import task2

class TestTask2(unittest.TestCase):

  # First test for the __str__ in task 2
  def test_str1(self):
    # Check str for non-empty lists
    x = task2.ListADT(10)
    append(x, [1, 2, 3])
    expected_output = '1\n2\n3' + '\n0'*(37)
    self.assertEqual(str(x).strip('\n'), expected_output)
  # Second test for the __str__ in task 2
  def test_str2(self):
    # Check str for non-empty lists
    x = task2.ListADT(10)
    append(x, ['eq1', 'eq2', 'eq3'])
    expected_output = 'eq1\neq2\neq3' + '\n0'*(37)
    self.assertEqual(str(x).strip('\n'), expected_output)
  
  # First test for the __len__ in task 2
  def test_len1(self):
    x = task2.ListADT(10)
    append(x, [1, 2, 3])
    self.assertEqual(len(x), 3)
  # second test for the __len__ in task 2
  def test_len2(self):
    x = task2.ListADT(10)
    append(x, ['eq1', 'eq2', 'eq3'])
    append(x, [1, 2, 3])
    self.assertEqual(len(x), 6)


  # First test for the __getitem__ in task 2
  def test_getitem1(self):
    x = task2.ListADT(10)
    append(x, [1, 2, 3])
    self.assertEqual(x[2], 3)
  # second test for the __getitem__ in task 2
  def test_getitem2(self):
    x = task2.ListADT(10)
    append(x, ['eq1', 'eq2', 'eq3'])
    append(x, [1, 2, 3])
    self.assertEqual(x[2], 'eq3')


  # First test for the __setitem__ in task 2
  def test_setitem1(self):
    x = task2.ListADT(10)
    append(x, [1, 2, 3])
    x[2] = 5
    self.assertEqual(x[2], 5)
  # second test for the __setitem__ in task 2
  def test_setitem2(self):
    x = task2.ListADT(10)
    append(x, ['eq1', 'eq2', 'eq3'])
    x[2] = 'val'
    self.assertEqual(x[2], 'val')

  # First test for the __eq__
  def test_eq1(self):
    x = task2.ListADT(10)
    y = task2.ListADT(10)
    self.assertEqual((x==y), True)
  # Second test for the __eq__
  def test_eq2(self):
    x = task2.ListADT(10)
    y = [2.5,6,7] 
    self.assertEqual((x==y), False)


  # First test case for the insert and delete
  def test_insert1(self):
    x = task2.ListADT(10)
    
    ## This should not fail.
    append(x, [1 for i in range(1000)])
    
    ## If the ListADT has renamed the underlying array, or used some other
    ## representation, we can't realy test whether resizing is handled correctly.
    if not hasattr(x, "the_array"):
      raise AttributeError("could not identify underlying array for the ListADT.")

    y = task2.ListADT(10)

    # If we gave a smaller constant, should have become 40.
    self.assertEqual(len(y.the_array), 40, "Allocated array below threshold.")

    # ... and with rounding
    y = task2.ListADT(44)
    for i in range(45):
      y.insert(i, i)
    self.assertEqual(len(y.the_array), 84, "Incorrect grow.") # math.ceil(44 * 1.9)

    # Check shrinking
    for i in range(25):
      y.delete(len(y)-1)
    self.assertTrue(len(y.the_array) == 42, "Incorrect shrink.")

  # Second test case for the insert and delete
  def test_insert2(self):
    y = task2.ListADT(50)
    # If we gave a smaller constant, should have become 40.
    self.assertEqual(len(y.the_array), 50, "Allocated array below threshold.")

    # ... and with rounding
    y = task2.ListADT(80)
    for i in range(81):
      y.insert(i, i)
    self.assertEqual(len(y.the_array), 152, "Incorrect grow.") # math.ceil(44 * 1.9)

    # Check shrinking
    for i in range(45):
      y.delete(len(y)-1)
    self.assertTrue(len(y.the_array) == 75, "Incorrect shrink.")


if __name__ == '__main__':
  unittest.main()
