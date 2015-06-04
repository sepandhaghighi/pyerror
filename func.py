from operator import *
from math import*
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
def hamming_gen(error_object):
        '''
hamming_gen(error_object) -> String
'''
        length=len(error_object)
        number_parity=int(log(length,2))+1
        parity_location=[]
        for i in range(number_parity):
                parity_location.append(int(2**i))
        init_vector=[]
        k=0
        for i in range(number_parity+length):
                if (i+1) in parity_location:
                        init_vector.append("0")
                else:
                        init_vector.append(error_object.str[k])
                        k=k+1
        print(init_vector)
        p1=[3,5,7,9,11,13,15,17,19]
        p2=[3,6,7,10,11,14,15,18,19]
        p4=[5,6,7,12,13,14,15,20,21,22,23]
        p8=[9,10,11,12,13,14,15]
        p16=[16,17,18,19,20,21]
        for i in range(number_parity+length):
                if ((i+1) in p1) and (i+1)<(length+number_parity) and number_parity>=1:
                        init_vector[0]=str(xor(int(init_vector[i+1]),int(init_vector[0])))
                if (i+1) in p2 and (i+1)<(length+number_parity) and number_parity>=2:
                        init_vector[1]=str(xor(int(init_vector[i+1]),int(init_vector[1])))
                if (i+1) in p4 and (i+1)<(length+number_parity) and number_parity>=3 :
                        init_vector[3]=str(xor(int(init_vector[i+1]),int(init_vector[3])))
                if (i+1) in p8 and (i+1)<(length+number_parity) and number_parity>=4 :
                        init_vector[7]=str(xor(int(init_vector[i+1]),int(init_vector[7])))
                if (i+1) in p16 and (i+1)<(length+number_parity) and number_parity>=5 :
                        init_vector[15]=str(xor(int(init_vector[i+1]),int(init_vector[15])))
        final_string = "".join(init_vector)
        return final_string
def hamming_det(error_object):
        length=len(error_object)
        p1=[3,5,7,9,11,13,15,17,19]
        p2=[3,6,7,10,11,14,15,18,19]
        p4=[5,6,7,12,13,14,15,20,21,22,23]
        p8=[9,10,11,12,13,14,15]
        p16=[16,17,18,19,20,21]
        parity_index=[0,1,3,7,15,31,63,127]
        parity_value=[]
        number_parity=int(log(length,2))
        for i in range(len(parity_index)):
                if i<number_parity:
                        parity_value.append(int(error_object[parity_index[i]]))
        print(parity_value)
        parity_value=[0,0,0]
        for i in range(length):
                if ((i+1) in p1) and (i+1)<(length) and number_parity>=1:
                        parity_value[0]=xor(int(error_object[i+1]),int(parity_value[0]))
                if ((i+1) in p2) and (i+1)<(length) and number_parity>=2 :
                        parity_value[1]=xor(int(error_object[i+1]),int(parity_value[1]))
                if ((i+1) in p4) and (i+1)<(length) and number_parity>=3 :
                        parity_value[2]=xor(int(error_object[i+1]),int(parity_value[2]))
                if ((i+1) in p8) and (i+1)<(length) and number_parity>=4:
                        parity_value[3]=xor(int(error_object[i+1]),int(parity_value[3]))
                if ((i+1) in p16) and (i+1)<(length) and number_parity>=5 :
                        parity_value[4]=xor(int(error_object[i+1]),int(parity_value[4]))
        return parity_value

        
        
                        
                        
                        
                
                                
                
                
                
                
                
                
        
         
                
                        
                
        
               
        

        
