
import task2
class Editor:
    """
        This is Editor class which have function to delete the line 
        as well as to insert the line and to read the text file also. 
    """

    def __init__(self):
        """ This will initialize the textlines with 
        ListADT class (that we have implemented in the
        task2)
        """
        self.text_lines = task2.ListADT(40)

    def read_filename(self, file_name):
        """
            This function will open the file and then it will insert 
            the data (lines from that file) into the list.
        """
        self.text_lines = task2.ListADT(40)
        # This is to open the file
        f = open(file_name,"r")
        # This will read the files
        f1 = f.readlines()
        # This to close the files
        f.close()
        # iterate over each line of the file
        for i, lines in enumerate(f1):
            # Insert the line into the array
            self.text_lines.insert(i, lines)
        # print(self.text_lines.the_array)
        
    def print_num(self, line_num):
        # This function is to print the line with given index

        # This if condition will make sure that the given line_num 
        # is valid or not.
        if int(line_num)-1 > self.text_lines.index or int(line_num)<=0:
            raise IndexError("Invalid Index")
        # Here it will print that line
        print(self.text_lines.the_array[int(line_num)-1])


    def delete_num(self, line_num):
        """
        This function will delete the line from the list with given index.
        """
        # This will check whether the given line_num is valid or not
        if int(line_num)-1 > self.text_lines.index or int(line_num)<=0:
            raise IndexError("Invalid Index")
        # this will delete the line from the list
        del self.text_lines.the_array[int(line_num)-1]
        # This will decrement the line pointer by on because one line 
        # is deleted
        self.text_lines.index -=1
    
    def insert_num_strings(self,line_num, lines):
        """
        This function will insert the lines at given index = line_num
        """
        # This will find the exact index to insert because line starts from 1
        # and index starts from the 0
        count = abs(int(line_num))-1
        for i in range(lines.index):
            # This will insert the lines into the list
            self.text_lines.insert(count, lines[i])
            count += 1

    def insert_num(self, line_num, lines):
        """
        This function will just insert the lines to the list
        """
        self.insert_num_strings(line_num,lines)


    def search_string(self, query):
        """For future"""
        raise NotImplementedError

    def undo(self):
        """For future"""
        raise NotImplementedError

if __name__ == "__main__":
    ed = Editor()
    while(1):
        text = input().split(' ')
        if text[0] == 'insert':
            # initialize the new list
            templine = task2.ListADT(1)
            count = 0
            line_num = text[1]
            while(1):
                text2 = input().split('\n')
                if text2[0] == '.':
                    break
                # append that line 
                templine.the_array[count] = text2[0]+ '\n'
                # increment the index by one 
                templine.index += 1
                count += 1
            ed.insert_num_strings(str(int(text[1])+1), templine)
        elif text[0] == 'delete':
            ed.delete_num(str(int(text[1])+1))
        elif text[0] == 'print' :
            ed.print_num(str(int(text[1])+1))
        elif text[0] == 'read':
            ed.read_filename(text[1])
        elif text[0] == 'exit()' : 
            break
        # print(ed.text_lines.the_array[:ed.text_lines.index])