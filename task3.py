"""
    There read_text_file function which take the 
    name of the text and and read the lines from that
    text and save it to the list (That list is the object
    of the ListADT that we have already implemented in the
    task2 )
"""
from task2 import ListADT
def read_text_file(filename):
    # This line will open the filename
    f = open(filename,"r")
    # This line will read the lines
    f1 = f.readlines()
    # This will close the file
    f.close()
    # This will initialize the list with ListADT format
    listadt = ListADT(40)
    # This will iterate over each line from the file
    for i, lines in enumerate(f1):
        # This will insert the lines to the the list
        listadt.insert(i, lines)
        # This will return the meaning full data from the line.
        # Meaning full means used elements from the list
    return listadt.the_array[:len(f1)]
