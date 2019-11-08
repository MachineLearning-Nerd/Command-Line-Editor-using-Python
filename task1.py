#!/usr/bin/python3
class ListADT:
    def __init__(self, size=10):
        # This defines the length of array 
        # and initialize the array with no size
        self.length = size 
        self.the_array = list()

    # def __repr__(self):
        # return self.the_array

    def __str__(self):
        # This will joint every element of the array 
        # after converting into string. 
        # map will convert [1,2,3] into ['1','2','3']
        # and then we will able to join it
        return '\n'.join(map(str,self.the_array))

    def __len__(self):
        # It will just find the length of the array
        # and returns that value
        return len(self.the_array)

    def __getitem__(self,index):
        """
            This function returns the element of the array 
            for the given index.
        """
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
        if index<0 and index < ((-1)*len(self.the_array)-1):
            raise IndexError("Invalid Index")
        # Here it will check whether indes is valid for positive values or
        # not
        elif  index>0 and (index > len(self.the_array)):
            raise IndexError("Invalid Index")
        # if index is larger then the length of the array then 
        # it will be invalid index
        elif  index>self.length:
            raise IndexError("Invalid Index")
        # This part will insert the value at the given index.
        else:  
            self.the_array.insert(index, item)

    def delete(self, index):
        """
            This function will delete the item from given index.
        """
        # if index is negative then the -len(self.the_array)
        # Then it is invalid index
        if index<0 and index < (-1)*len(self.the_array):
            raise IndexError("Invalid Index")
        # if index is positive and having larger then the length of
        # array then that index is invalid
        elif  index>0 and (index > len(self.the_array)-1):
            raise IndexError("Invalid Index")
        # This will delete the item from the given index
        else:       
            del self.the_array[index] 

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
