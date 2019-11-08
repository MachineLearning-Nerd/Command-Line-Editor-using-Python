import math
import unittest
from test_common import *
import task3

testcontent1 = [
"This is what I've been doing.",
"Code for atleast an Hour daily.",
"Dont miss anything about Python.",
"Pick up a project.",
"learn what is (which topic) bothering you the most."]
class TestTask3(unittest.TestCase):
  def test_read_file(self):
    test_lines = task3.read_text_file('TestFile.txt')
    self.assertEqual([ l.strip('\n') for l in ToList(test_lines) ], test_content, msg = "File not correctly read.")
    
  # This is for new file 
  def test_read_file1(self):
    test_lines = task3.read_text_file('testtask3.txt')
    self.assertEqual([ l.strip('\n') for l in ToList(test_lines) ], testcontent1, msg = "File not correctly read.")
if __name__ == '__main__':
  unittest.main()
