import math
import unittest
from test_common import *
import task2
import task6

class TestTask6(unittest.TestCase):
  def test_undo(self):
    ed = task6.Editor()
    
    extra_lines = [ "These are some extra lines.", "They are will be added to the string." ]

    ed.read_filename('TestFile.txt')
    ed.delete_num("")
    ed.insert_num_strings("1", ToListADT(task2.ListADT, extra_lines))
    ed.undo()
    self.assertTrue(equal_lines(ed, []))
    ed.undo()
    self.assertTrue(equal_lines(ed, test_content))
    with self.assertRaises(Exception, msg = "Undoing past the beginning of history should have failed."):
      ed.undo()

  def test_undo1(self):
    ed = task6.Editor()
    ed.read_filename('BigTextFile.txt')
    ed.delete_num("")
    ed.insert_num_strings("1", ToListADT(task2.ListADT, ['Extra lines', 'Well work']))
    ed.undo()
    self.assertTrue(equal_lines(ed, []))
    ed.undo()
    self.assertTrue(ed.text_lines[0], "Title: The Trial Trip of the Flying Cloud")

  def test_undo2(self):
    ed = task6.Editor()
    extra_lines = [ "These are some extra lines.", "They are will be added to the string." ]
    ed.read_filename('BigTextFile.txt')
    ed.delete_num("1")
    self.assertTrue(ed.text_lines[0], "Author: J.R. Orton")
    ed.delete_num("1")
    self.assertTrue(ed.text_lines[0], "* A Project Gutenberg of Australia eBook *")
    ed.delete_num("1")
    self.assertTrue(ed.text_lines[0], "eBook No.: 0602221.txt")
    ed.undo()
    self.assertTrue(ed.text_lines[0], "* A Project Gutenberg of Australia eBook *")
    ed.undo()
    self.assertTrue(ed.text_lines[0], "Author: J.R. Orton")
if __name__ == '__main__':
  unittest.main()
