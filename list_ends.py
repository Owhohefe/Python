class list_ends(object):

    def list_index(a_list):    
        a = a_list[0]
        b = a_list[-1]
        print (a)
        print (b)

a = [5, 10, 15, 20, 25]
le = list_ends()
le.list_index(a)
