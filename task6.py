import task2
class Editor:
    """
        This is Editor class which have function to delete whe line 
        as well as to insert whe line and to read whe text file also. 
    """
    def __init__(self):
        """ This will initialize whe textlines with 
        ListADT class (that we have implemented in the
        task2)
        """
        self.text_lines = task2.ListADT(40)
        # this previous task is to monitor the previous line which is either deleted or 
        # inserted
        self.previoustask = list()
        # This is to moniter which command is given insert or delete
        self.command = list()
        # This is to see whether we are in undo or out of undo function
        self.mode = 'notundo'

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
            self.text_lines.insert(i, lines.strip('\n'))
        # print(self.text_lines.the_array)
        
    def print_num(self, line_num):
        # This function is to print the line with given index

        # This if condition will make sure that the given line_num 
        # is valid or not.
        if int(line_num)-1 > self.text_lines.index or int(line_num)<=0:
            raise IndexError("Invalid Index")
        # Here it will print that line
        print(self.text_lines.the_array[int(line_num)-1] )


    def delete_num(self, line_num):
        """
        This function will delete the line from the list with given index.
        """
        # This will check whether the given line_num is valid or not
        if line_num != "" and (int(line_num)-1 > self.text_lines.index or int(line_num)<0):
            raise IndexError("Invalid Index")
        # This will check whether we need to delete all the lines or just one line
        # line_num = "" means delete all the lines
        if line_num == "":
            # check whether we are in undo or normal delete mode.
            if self.mode == 'notundo':
                # Here are we are appending to the command that we are going to 
                # delete all the lines and number of lines to be deleted are given 
                # by self.text_lines.index
                self.command.append(('DeleteAll',self.text_lines.index))
            # This will iterate over each line and then it will delete each line
            for i in range(self.text_lines.index):
                if self.mode == 'notundo':
                    # if the function is not in undo mode then it will append the line
                    # to the previous command so when we are in undo mode we can have those lines
                    # to do undo operation.
                    self.previoustask.append(self.text_lines[0])
                # This will delete the line
                del self.text_lines.the_array[0]
            # After deleting all the line the starting of the list will become 0th index.
            self.text_lines.index = 0 
        else:
            # This will delete the perticular line given by the line_num 
            if self.mode == 'notundo':
                # we are not in undo function then it will append the lines to the previoustask 
                # delete operation to the command.
                self.previoustask.append((self.text_lines.the_array[int(line_num)-1],int(line_num)-1 ))
                # Here 1 denote that we are going to delete only one line
                self.command.append(('Delete', 1))
            # this will delete the line
            del self.text_lines.the_array[int(line_num)-1]
            # reduce the index by one value because only one line is deleted
            self.text_lines.index -=1
    
    def insert_num_strings(self,line_num, lines):
        """
        This function will insert the lines with given line_num
        """
        # This will find the exact index to insert because line starts from 1
        # and index starts from the 0
        count = abs(int(line_num))-1
        for i in range(lines.index):
            # This will insert the lines into the list
            self.text_lines.insert(count, lines[i])
            # self.text_lines.index +=1
            count += 1
        if self.mode == 'notundo':
            # if we are in normal mode then it will store the line that we will 
            # going to insert in the previous task and insert into the command
            self.previoustask.append((line_num, count))
            self.command.append(('Insert', 1))


    def insert_num(self, line_num, lines):
        """
        This function will just insert the lines to the list
        """
        self.insert_num_strings(line_num,lines)

    def search_string(self, query):
        """
        This will find the occurance of the query in the lines of the text
        """
        catch_lines = []
        # Iterate over each line
        for i in range(self.text_lines.index):
            linetext = self.text_lines[i]
            # count how many time query occure within that line
            if (linetext.count(query)) != 0:
                catch_lines.append(i+1)
        # return the line number where the query is occured
        return catch_lines
    def undo(self):
        """
        This function will undo the operation that we have done to the list
        """
        # Set that we are in undo mode
        self.mode = 'undo'
        # This will pop up the last command that we have append or run
        (command, val) = self.command.pop() 
        # It will check whether the command is insert or not
        if command == 'Insert':
            # if the command is insert then we will pop out the previous lines that
            # we have inserted and the with the index.
            (line_num, count) = self.previoustask.pop()
            for i in range(count):
                # we will delete all the lines that we have inserted to the list 
                # using del command
                del self.text_lines.the_array[int(line_num)-1]
                # every time we will reduce the index by one value because we are deleting
                # one line at a time.
                self.text_lines.index -= 1
        elif  command == 'Delete':
            # if the command is delete then we will fetch the previous previosly deleted 
            # lines with the line number
            (line, line_num) = self.previoustask.pop()
            # print(line_num, type(line_num))
            templine = task2.ListADT(1)
            templine.insert(0,line)
            # print(templine)
            # then we will just insert those lines to the list with given line_num
            self.insert_num_strings(str(line_num+1), templine)
        elif  command== 'DeleteAll':
            # print("Text index", self.text_lines.index)
            # print(self.text_lines.index)
            # if the command is to delete all the lines then we need to iterate over
            # each line that we have deleted. 
            # val denote the number of deleted lines.
            # initialize the new list
            templine = task2.ListADT(1)
            for i in range(val):
                # print(i)
                # pop the previos line
                line = self.previoustask.pop()
                # print(line)
                # append that line 
                # templine.the_array[0] = line
                templine.insert(0,line)
                # increment the index by one 
                # templine.index += 1
                # This will insert the line to our main list
                # self.insert_num_strings(str(val - i), templine)
            # print(templine)
            self.insert_num_strings('1', templine)
        # Now we are out of undo so we have set notundo mode here
        self.mode = 'notundo'

        
if __name__ == "__main__":
    ed = Editor()
    while(1):
        print('>>', end='')
        text = input().strip().split(' ')
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
            if len(text)==1:
                for printi in range(ed.text_lines.index):
                    ed.print_num(str(printi+1))
            else:
                ed.print_num(str(int(text[1])+1))
        elif text[0] == 'read':
            ed.read_filename(text[1])
        elif text[0] == 'undo':
            ed.undo()
        elif text[0] == 'exit()' : 
            break
        # print(ed.text_lines.the_array[:ed.text_lines.index])        
