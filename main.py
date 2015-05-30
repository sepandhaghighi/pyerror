from func import *
def convert_gen(error_object):
    '''
    Convert_gen(error_object) -> error_object
'''
    if error_object.code=="Parity":
        return error_detect(parity_gen(error_object),error_object.code)
def convert_det(error_object):
    '''
    Convert_det(error_object)-< Boolean
'''
    if error_object.code=="Parity":
        return parity_det(error_object)
        
class error_detect:
 
    '''
            (String , Error Detection Method)-> Error Detection Object)
    '''  
    def __init__(self,string,method):
       
        self.str=string
        self.code=method

        
        
    def __str__(self):

        return ("Error_Detection("+self.str+","+str(self.code)+")")
    

