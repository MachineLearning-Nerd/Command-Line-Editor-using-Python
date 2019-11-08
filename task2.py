#!/usr/bin/python3
import  math
class ListADT:
    def __init__(self, size=10):
        if size < 40 :
            size = 40
        # This is to moniter the len of the array
        self.length = size 
        self.the_array = [0]*size 
        # This variable is to moniter the meaningful data 
        self.index = 0

    def __str__(self):
        # This will be called when we use str(self)
        return '\n'.join(map(str,self.the_array))

    def __len__(self):
        # This will give the information about the length of the 
        # list 
        return self.index

    def __getitem__(self,index):
        # This will be called when we use self[index]
        # Type of expression
        # if index is negative then the -len(self.the_array)
        # Then it is invalid index
        if index<0 and index < (-1)*len(self.the_array):
            raise IndexError("Invalid Index")
        # if index is positive and having larger then the length of
        # array then that index is invalid
        elif  index>0 and (index > len(self.the_array)-1):
            raise IndexError("Invalid Index")
        # This will return the element of the array for the 
        # given index
        else:
            return self.the_array[index]

    def __setitem__(self,index, item):
        """
            This function will set the value of the array for the given 
            index and the item.
        """
        # if index is negative then the -len(self.the_array)
        # Then it is invalid index
        # This will be called when we want to set 
        # self[index] = some value
        if index<0 and index < (-1)*len(self.the_array):
            raise IndexError("Invalid Index")
        # if index is positive and having larger then the length of
        # array then that index is invalid
        elif  index>0 and (index > len(self.the_array)-1):
            raise IndexError("Invalid Index")
        # This will return the element of the array for the 
        # given index
        else:
            self.the_array[index] = item            
    def __eq__(self, other):
        """
            This function will be called when we have condition like
            self == other. 
        """
        # This if condition will check whether the other has the_array  
        # attribute or not. If it have then it will compare both self and 
        # other object and their types.
        # This will find out the whether other variable is equivalent 
        # to the self of not. 
        # This will be called when we have something like this:
        # self == other
        if hasattr(other, 'the_array'):
            return self.the_array == other.the_array and type(self) == type(other)
        else:
            return self.the_array == other and type(self) == type(other)

    def insert(self, index, item):
        """
            This function will insert the data to the array at the given 
            index and with the value of the item.
        """
        # Here it will chech whether index is valid for negative values
        # or not.
        # This if condition checks whether the list is full or not
        if self.is_full() and index == self.length-1:
            self.the_array[index] = item
            # if it is full then we will increse the length of the list
            temp =  int(math.ceil(self.length * 1.9))
            # We have appended extra zeros
            self.the_array = self.the_array + [0]*(temp-self.length)
            self.length = math.ceil(self.length * 1.9)
            self.index +=1
        
        else: 
            # if list is not full then we will just update the list
            if index < len(self.the_array) and index >= self.index:
                self.the_array[index] = item
                # self.the_array.insert(index, item)
            else: 
                self.the_array.insert(index, item)
            self.index +=1
                
        

    def delete(self, index):
            """
                This function will delete the item from given index.
            """
            # if index is negative then the -len(self.the_array)
            # This will delete the data with respect to the index
            del self.the_array[self.index] 
            self.index -=1
            if self.index <= self.length//4 :
                self.length = self.length//2
                self.the_array = self.the_array[:self.length+1]

    def is_empty(self):
        """
            This function will check whether the array is empty or not.
        """
        return self.length == 0

    def is_full(self):
        """
            This function will check whether the array is full or not.
        """
        return self.length == len(self.the_array)

    def __contains__(self, item):
        for i in range(self.length):
            if item == self.the_array[i]:
                return True
        return False
 
    def append(self, item):
        if not self.is_full():
            self.the_array[self.length] = item
            self.length +=1
        else:
            raise Exception('List is full')

    def unsafe_set_array(self,array,length):
        """
        UNSAFE: only to be used during testing to facilitate it!! DO NOT USE FOR ANYTHING ELSE
        """
        if 'test' not in __name__:
            raise Exception('Not runnable')
			
        self.the_array = array
        self.length = length