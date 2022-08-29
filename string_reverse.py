import string

class string_reverse(object):

    str1 = input("Enter a multi-word string: ")
    list1 = []
    str2 = ""

    def split_string(self):
        self.str1 = self.str1.translate(self.str1.maketrans(",'\"!", "    ", string.punctuation))
        self.list1 = self.str1.split()

    def reverse_list(self):
        self.list1.reverse()

    def join_string(self):
        self.str2 = " ".join(self.list1)

    def print_string(self):
        print (self.str2)

sr = string_reverse()
sr.split_string()
sr.reverse_list()
sr.join_string()
sr.print_string()

        

        
        
        
