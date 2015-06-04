from func import *
def convert_gen(error_object):
    '''
    Convert_gen(error_object) -> error_object
'''
    if error_object.code=="Parity":
        return error_detect(parity_gen(error_object),error_object.code,error_object.flag)
    elif error_object.code=="Repeat":
        return error_detect(repeat_gen(error_object),error_object.code,error_object.flag)
    elif error_object.code=="Hamming":
        return error_detect(hamming_gen(error_object),error_object.code,error_object.flag)
def convert_det(error_object):
    '''
    Convert_det(error_object)-< Boolean
'''
    if error_object.code=="Parity":
        return parity_det(error_object)
    elif error_object.code=="Repeat":
        return repeat_det(error_object)
    elif error_object.code=="Hamming":
        return hamming_det(error_object)
        
class error_detect:
 
    '''
            (String , Error Detection Method)-> Error Detection Object)
    '''  
    def __init__(self,string,method,flag=2):
       
        self.str=string
        self.code=method
        self.flag=flag
        
    def __getitem__(self,i):
        return self.str[i]
    def __len__(self):
        return len(self.str)    
        
    def __str__(self):

        return ("Error_Detection("+self.str+","+str(self.code)+","+str(self.flag)+")")
    

