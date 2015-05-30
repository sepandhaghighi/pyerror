from operator import *
# Error Check And Correction Functions In Python
def parity_gen(error_object):
        '''
parity_gen(error_object)-> String
'''
        temp=0
        length=len(error_object)
        for i in range(length):
            temp=xor(int(error_object[i]),temp)
        output=error_object.str+str(temp)
        return output
def parity_det(error_object):
        '''
parity_det(error_object)-> Boolean
'''
        temp=0
        length=len(error_object)
        for i in range(length-1):
            temp=xor(int(error_object[i]),temp)
        if str(temp)==error_object[-1]:
                return True
        else:
                return False
def repeat_gen(error_object):
        '''
repeat_gen(error_object) -> String
'''

        return error_object.str*error_object.flag
def repeat_det(error_object):
        '''
repeat_det(error_object) -> Boolean
'''
        temp=None
        length=len(error_object)
        repeat_number=int(error_object.flag)
        message_length=length//repeat_number
        original_message=error_object[0:message_length]
        for i in range(repeat_number):
                temp=error_object[i*message_length:(i+1)*message_length]
                if temp!=original_message:
                        return False
        return True
        
               
        

        
