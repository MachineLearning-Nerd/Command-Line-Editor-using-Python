import math
import unittest
from test_common import *
import task2
import task4

class TestTask4(unittest.TestCase):
  def test_read(self):
    ed = task4.Editor()
    ed.read_filename('TestFile.txt')
    self.assertTrue(equal_lines(ed, test_content), msg =  "File not correctly read.")

  def test_print(self):
    ed = task4.Editor()
    ed.read_filename('TestFile.txt')
    ed.print_num("1")

  def test_delete(self):
    ed = task4.Editor()
    ed.read_filename('TestFile.txt')
    ed.delete_num("1")
    self.assertTrue(equal_lines(ed, test_content[1:]), msg =  "Failed to delete first line.")
   
    for index in ["-5"]:
      with self.assertRaises(IndexError, msg = "Deleting out-of-bounds lines should fail."):
        ed.read_filename('TestFile.txt')
        ed.delete_num(index)

  # This function will delete first line from the BigTextFile.txt
  def test_delete1(self):
    ed = task4.Editor()
    ed.read_filename('BigTextFile.txt')
    ed.delete_num("1")
    temptext = "Author: J.R. Orton"
    self.assertTrue(ed.text_lines[0], temptext)
   
  def test_insert(self):
    ed = task4.Editor()
    ed.insert_num_strings("1", ToListADT(task2.ListADT, [test_content[0]]))
    self.assertTrue(equal_lines(ed, [test_content[0]]), msg =  "Failed to insert single line.")

    ed = task4.Editor()
    ed.insert_num_strings("-1", ToListADT(task2.ListADT, [test_content[2], test_content[3]]))
    self.assertTrue(equal_lines(ed, [test_content[2], test_content[3]]), msg =  "Incorrect handling of negative insertion")

  def test_insert1(self):
    ed = task4.Editor()
    ed.read_filename('BigTextFile.txt')
    temptext = "Author: J.R. Orton"
    ed.insert_num_strings("1", ToListADT(task2.ListADT, [temptext]))
    self.assertTrue(ed.text_lines[0], temptext)

    ed.insert_num_strings("10", ToListADT(task2.ListADT, [temptext]))
    self.assertTrue(ed.text_lines[9], temptext)
if __name__ == "__main__":

  unittest.main()
