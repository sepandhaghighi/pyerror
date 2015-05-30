from operator import *
def parity_gen(error_object):
        '''
parity_gen(error_object)-> String
'''
        temp=0
        length=len(error_object.str)
        for i in range(length):
            temp=xor(int(error_object.str[i]),temp)
        output=error_object.str+str(temp)
        return output
def parity_det(error_object):
        '''
parity_det(error_object)-> Boolean
'''
        temp=0
        length=len(error_object.str)
        for i in range(length-1):
            temp=xor(int(error_object.str[i]),temp)
        if str(temp)==error_object.str[-1]:
                return True
        else:
                return False
        
