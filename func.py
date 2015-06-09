from operator import *
from math import*
poly_vector=["1011","111010101","11000000000000101"]
hex_dict={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
def hex_2_bin(hex_input):
        try:
                init_bin=[]
                for i in hex_input:
                        init_bin.append(bin(hex_dict[i])[2:])
                result="".join(init_bin)
                return result
        except:
                print("Something Wrong")
                return None
def bin_2_dec(bin_input):
        try:
                s=0
                input_val=bin_input.reverse()
                for i in range(len(bin_input)):
                        s=s+(2**i)*int(bin_input[i])
                return s
        except:
                print("Something Wrong")
                return None
                
                        

# Error Check And Correction Functions In Python
def parity_even_gen(error_object):
        '''
parity_gen(error_object)-> String
'''
        try:
                temp=0
                length=len(error_object)
                for i in range(length):
                    temp=xor(int(error_object[i]),temp)
                output=error_object.str+str(temp)
                return output
        except:
                print("Error In Generating Even Parity")
                return None
def parity_even_det(error_object):
        '''
parity_det(error_object)-> Boolean
'''
        try:
                temp=0
                length=len(error_object)
                for i in range(length-1):
                    temp=xor(int(error_object[i]),temp)
                if xor(temp,int(error_object[-1]))==0:
                        return True
                else:
                        return False
        except:
                print("Error In Detecting Even Parity")
                return None
def parity_odd_gen(error_object):

        try:
                temp=0
                length=len(error_object)
                for i in range(length):
                        temp=xor(int(error_object[i]),temp)
                result=error_object.str+str(int(not(temp)))
                return result
        except:
                print("Error In Generating Odd parity")
                return None
def parity_odd_det(error_object):
        try:
                temp=0
                length=len(error_object)-1
                for i in range(length):
                        temp=xor(temp,int(error_object[i]))
                if xor(temp,int(error_object[-1]))==1:
                        return True
                else:
                        return False
        except:
                print("Error In Detectting Odd Parity")
                return None
        
def repeat_gen(error_object):
        '''
repeat_gen(error_object) -> String
'''
        try:
                return error_object.str*error_object.flag
        except:
                print("Error In repeat Generation")
                return None

def repeat_det(error_object):
        '''
repeat_det(error_object) -> Boolean
'''
        try:
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
        except:
                print("Error In Repeat Detection")
                return None

def hamming_gen(error_object):
        length=len(error_object)
        parity_number=int(log(length,2))+1
        parity_index=[]
        message=[]
        p1=[0,2,4,6,8,10,12,14,16,18]
        p2=[1,2,5,6,8,9,13,14,17,18]
        p4=[3,4,5,6,11,12,13,14,19]
        p8=[7,8,9,10,11,12,13,14]
        p16=[15,16,17,18,19]
        k=0
        parity_number_index=1
        for i in range(length):
                if int(2**i)<=length and parity_number_index<=parity_number:
                        parity_index.append(int(2**i)-1)
                        parity_number_index=parity_number_index+1
        for i in range(length+len(parity_index)):
                if i in parity_index:
                        message.append("0")
                else:
                        message.append(error_object[k])
                        k=k+1
        for i in range(length+len(parity_index)):
                if i in p1:
                        message[0]=str(xor(int(message[0]),int(message[i])))
                if i in p2:
                        message[1]=str(xor(int(message[1]),int(message[i])))
                if i in p4:
                        message[3]=str(xor(int(message[3]),int(message[i])))
                if i in p8:
                        message[7]=str(xor(int(message[7]),int(message[i])))
                if i in p16:
                        message[15]=str(xor(int(message[15]),int(message[i])))
        result="".join(message)
        return result
                      
def hamming_det(error_object):
        length=len(error_object)
        parity_index=[]
        message=list(error_object)
        parity_value=[]
        p1=[2,4,6,8,10,12,14,16,18]
        p2=[2,5,6,8,9,13,14,17,18]
        p4=[4,5,6,11,12,13,14,19]
        p8=[8,9,10,11,12,13,14]
        p16=[16,17,18,19]
        for i in range(length):
                if int(2**i)<=length:
                        parity_index.append(int(2**i)-1)
                else:
                        break
        for i in range(length):
                if i in parity_index:
                        parity_value.append(error_object[i])

        for i in range(length):
                if i in p1:
                        parity_value[0]=str(xor(int(parity_value[0]),int(message[i])))
                if i in p2:
                        parity_value[1]=str(xor(int(parity_value[1]),int(message[i])))
                if i in p4:
                        parity_value[2]=str(xor(int(parity_value[2]),int(message[i])))
                if i in p8:
                        parity_value[3]=str(xor(int(parity_value[3]),int(message[i])))
                if i in p16:
                        parity_value[4]=str(xor(int(parity_value[4]),int(message[i])))
                
        if bin_2_dec(parity_value)==0:
                return True
        else:
                output="Error Bit Number : "+str(bin_2_dec(parity_value))
                print(output)
                return False 
                
def checksum_gen(error_object):
        length=len(error_object)
        temp=0
        for i in error_object.str:
                temp=temp+hex_dict[i]
        temp=hex(temp)
        temp=temp[2:]
        final_string=error_object.str+temp
        return final_string
        
def checksum_det(error_object):
        checksum=error_object[-2:]
        temp=0
        for i in error_object.str[:-2]:
                temp=temp+hex_dict[i]
        temp=hex(temp)
        temp=temp[2:]
        if temp==checksum:
                return True
        else:
                return False
def crc_gen(error_object,poly):
        try:
                divider_len=len(poly)
                extra_bit_len=divider_len-1
                message=error_object.str+(extra_bit_len)*"0"
                length=len(message)
                length_init=len(error_object)
                message=list(message)
                start_index=0
                cond_list=["0"]*length_init
                while(message[0:length-(extra_bit_len)]!=cond_list ):
                        temp=message[start_index:start_index+divider_len]
                        for i in range(divider_len):
                                temp[i]=str(xor(int(temp[i]),int(poly[i])))
                        message[start_index:start_index+divider_len]=temp
                        for j in range(length):
                                if message[j]=="1":
                                        start_index=j
                                        break
                result="".join(message[length-(extra_bit_len):])
                return error_object.str+result
        except:
                print("Something Wrong In Generating Error_Detection Object!!")
                return None
                        
                
        
def crc_det(error_object):
        try:
                divider_len=len(poly)
                extra_bit_len=divider_len-1
                message=list(error_object.str)
                length=len(message)
                start_index=0
                cond_list=["0"]*(length-extra_bit_len)
                while(message[0:length-extra_bit_len]!=cond_list):
                        temp=message[start_index:start_index+divider_len]
                        for i in range(divider_len):
                                temp[i]=str(xor(int(temp[i]),int(poly[i])))
                        message[start_index:start_index+divider_len]=temp
                        for j in range(length):
                                if message[j]=="1":
                                        start_index=j
                                        break
                if "".join(message[length-extra_bit_len:])=="000":
                        return True
                else:
                        return False
        except:
                print("Something Wrong In Detecting Error In Object")
                return None
        
        

        
