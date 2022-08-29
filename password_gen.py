import random

class password_gen(object):

    list1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    list2 = [0,1,2,3,4,5,6,7,8,9]
    list3 = ["!", "#","*", "$", "@", "%", "?","^","&","(",")"]

    list5 = []
    password1 = [random.choice(list1), str(random.choice(list2)), random.choice(list1).upper(), random.choice(list3)]
    
    a = 0

    num_password = int (input("Enter the password length - minimum is 4: "))

    def shuff_Pass1(self):
        random.shuffle(self.password1)
        

    def gen_pass(self):

        while self.a < (self.num_password - 4):
            x = random.choice(self.list1)
            y = random.choice(self.list2)
            z = random.choice(self.list1).upper()
            u = random.choice(self.list3)
            list4 = [x, y, z, u]
            char1 = str(random.choice(list4))
            self.list5.append(char1)
            self.a +=1

        self.password1.extend(self.list5)
        password = "".join(self.password1)
        print(password)


pg = password_gen()
pg.shuff_Pass1()
pg.gen_pass()
