class Dictionary(object):
    dict={'Name':'Micheal', 'Age':19, 'sex': 'Male'}
    def print_Dict(self):
        del self.dict['sex']
        self.dict['Age']= 20
        print(self.dict)
        x =self.dict['Age']*2
        print(self.dict['Name'])
        print(x)

DT = Dictionary()
DT.print_Dict()
