 
#The main purpose of a constructor is to initialize or

# assign values to the data members of that class. 
#It cannot return any value other than none.

def create_an_empty_list():
    return []
#We'll use the literal constructor to make a new list with nothing in it:
# Constructors are generally used for instantiating an object. The task of constructors is to initialize(assign values) to the data members of the class when an object of the class is created.

def create_a_list():
    return [1, 2, 3, 4]
#This function should use the literal constructor to create a new list, just like we did above. This time, however, create a list that contains four elements. The four elements can be any elements of your choosing, as long as there are only four of them.
#literals are a data type and can hold any value type, such as strings, numbers, and more.
def add_element_to_end_of_list(lst, element):
    lst.append(element)
    return lst

def add_element_to_start_of_list(lst, element):
    lst.insert(0, element)
    return lst
#The insert() method inserts the specified value at the specified position.

def remove_element_from_end_of_list(lst):
    lst.pop()
    return lst
# List pop is pre-defined, in-built function that removes an item at the specified index from the list.

def remove_element_from_start_of_list(lst):
    del lst[0]
    return lst
#The del keyword is used to delete objects
#so the del keyword can also be used to delete variables, lists

def retrieve_first_element_from_list(lst):
    return lst[0]

#takes in one argument, the list from which we want to retrieve an element. 
# Use [] notation to return the value stored at the first index of the lis
def retrieve_element_from_index(lst, index):
    return lst[index]
# This function takes in two arguments, a list and the index number whose element we want to retrieve. 

def retrieve_last_element_from_list(lst):
    return lst[-1]