from func import *
def convert_gen(error_object):
    '''
    Convert_gen(error_object) -> error_object
'''
    mode=None
    if error_object.code=="Parity-Even":
        mode=parity_even_gen(error_object)
    elif error_object.code=="Parity-Odd":
        mode=parity_odd_gen(error_object)
    elif error_object.code=="Repeat":
        mode=repeat_gen(error_object)
    elif error_object.code=="Hamming":
        mode=hamming_gen(error_object)
    elif error_object.code=="Checksum":
        mode=checksum_gen(error_object)
    elif error_object.code=="CRC3":
        mode=crc_gen(error_object,poly_vector[0])
    
    return error_detect(mode,error_object.code,error_object.flag)
    
def convert_det(error_object):
    '''
    Convert_det(error_object)-< Boolean
'''
    result=None
    if error_object.code=="Parity-Even":
        result=parity_even_det(error_object)
    elif error_object.code=="Parity-Odd":
        result=parity_odd_det(error_object)
    elif error_object.code=="Repeat":
        result=repeat_det(error_object)
    elif error_object.code=="Hamming":
        result=hamming_det(error_object)
    elif error_object.code=="Checksum":
        result=checksum_det(error_object)
    elif error_object.code=="CRC3":
        result=crc_det(error_object,poly_vec[0])
    return result
        
        
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
    def __add__(self,other):
        try:
            if type(other)==str:
                return error_detect(self.str+other,self.code,self.flag)
            
            elif self.code==other.code and self.flag==other.flag:
                return error_detect(self.str+other.str,self.code,self.flag)
            else:
                print("Code And Flag Of This 2 Object Are Defferent")
        except:
            print("Bad Input")
    def __mul__(self,other):
        try:
            if type(other)==int or type(other)==float:
                return error_detect((self.str)*2,self.code,self.flag)
            else:
                print("Bad Input")
        except:
            print("Bad Input")
    def __equal__(self,other):
        try:
            if self.str==other.str and self.code==other.code and self.flag==other.flag:
                return True
            else:
                return False
        except:
            print("Bad Input")
                
            
    def __str__(self):

        return ("Error_Object("+self.str+","+str(self.code)+","+str(self.flag)+")")
    def __repr__(self):
        return ("E_Object("+"Message: "+self.str+" ,"+"Method: "+str(self.code)+" ,"+"Flag: "+str(self.flag)+")") 

