class palindrome (object):
    text = ""
    x = []

    def create_List (self):
        self.text = input ("Enter a word: ")
        for letter in self.text:
            self.x.append(letter)

    def reverse_list(self):
        self.x.reverse()

    def print_list(self):
        for letter in self.x:
            print(letter)

PAL = palindrome()
PAL.create_List()
PAL.reverse_list()
PAL.print_list()
