from operator import *
from math import*

poly_vector=["1011","111010101","11000000000000101","100000100110000010001110110110111"]
hex_dict={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
bin_dict={"0000":0,"0001":1,"0010":2,"0011":3,"0100":4,"0101":5,"0110":6,"0111":7,"1000":8,"1001":9,"1010":"A","1011":"B","1100":"C","1101":"D","1110":"E","1111":"F"}
def what(string):
        '''
        (str)->str
        Find Input Type
'''
        length=len(string)
        hex_string=[]
        bin_string=[]
        error_flag=0
        for i in range(length):
                if string[i] in ["0","1"]:
                        hex_string.append(1)
                        bin_string.append(1)
                elif string[i] in hex_dict.keys():
                        hex_string.append(1)
                        bin_string.append(0)
                else:
                        error_flag=1
        if error_flag==0 and all(bin_string):
                return "bin"
        elif error_flag==0 and all(hex_string):
                return "hex"
        else:
                return "None"
                
def bin_2_hex(bin_input):
        '''
        (Str)->Str
        Bin Input To Hex
        '''
        try:
                length=len(bin_input)
                temp=[]
                temp_2=[]
        
                for i in range(4-length%4):
                        temp.append("0")
                temp="".join(temp)
                temp=temp+bin_input
                for i in range(0,len(temp),4):
                        if i+3<len(temp):
                                temp_2.append(str(bin_dict[temp[i:i+4]]))
                temp_2="".join(temp_2);
                return temp_2
        except:
                print("Something Wrong In Input")
                return None
                
                
                
                        
                
def hex_2_bin(hex_input):
        '''
        hex_2_bin(str)-> str
        '''
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
        '''
        bin_2_dec(str)-> str
        '''
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
        parity_even_gen(error_detect)-> str
        This Function Get an Error_Object As Input And Return A String That Modified By Even Parity Code
        Default Input In This Mehtod Is Binary
        '''
        

        try:
                new_str=""      #Empty String
                if what(error_object.str)=="bin":  # Condition For Checking Binary Or Hex (Default Is Binary)
                        new_str=error_object.str
                elif what(error_object.str)=="hex":
                        new_str=hex_2_bin(error_object.str)
                temp=0    #Temp Variable(Default Zero For XOR Operation)
                length=len(new_str)   # Length Of Input String
                for i in range(length):    # Loop For Calculate XOR Of All Bits
                    temp=xor(int(new_str[i]),temp)
                output=new_str+str(temp)   # Adding Parity Bit To End Of The Original Message
                return output #Return Output In Binary For For transmit
        except:
                print("Error In Generating Even Parity")
                return None

        
def parity_even_det(error_object):
        '''
        parity_even_det(error_detect)-> Boolean
        This Function Get an Error_Object As input and return a boolean value that represent that this string has error or not
        Default Input Format Is Binary
        '''
        try:
                new_str=error_object.str   # Copy Error Object String In New String Variable
                temp=0   # Temp Variable (Default Zero For XOR)
                length=len(new_str) # Length of Input String
                for i in range(length-1):     # Loop For Calculate Of XOR Of All Bits - Last
                    temp=xor(int(new_str[i]),temp) 
                if xor(temp,int(new_str[-1]))==0: # Compare Loop result With last Bit And Return Boolean
                        return True
                else:
                        return False
        except:
                print("Error In Detecting Even Parity")
                return None




def parity_odd_gen(error_object):
        '''
        parity_odd_gen(error_detect)-> str
        This Function Get an Error_Object As Input And Return A String That Modified By Odd Parity Code
        Default Input In This Mehtod Is Binary
        '''

        try:
                new_str="" # Empty String
                if what(error_object.str)=="bin":  # Condition For Checking Binary Or Hex (Default Is Binary)
                        new_str=error_object.str
                elif what(error_object.str)=="hex":
                        new_str=hex_2_bin(error_object.str)
                temp=0 # Temp Variable (Default Zero For XOR)
                length=len(new_str) # Length Of Input String
                for i in range(length):  # Loop For Calculate XOR Of Bits
                        temp=xor(int(new_str[i]),temp)
                result=new_str+str(int(not(temp))) #Convert To XNOR
                return result # Return Binary Output
        except:
                print("Error In Generating Odd parity")
                return None




        
def parity_odd_det(error_object):
        '''
        parity_odd_det(error_detect)-> Boolean
        This Function Get an Error_Object As input and return a boolean value that represent that this string has error or not
        Default Input Format Is Binary
        '''
        try:
                new_str=error_object.str  # Copy Error Object String In New String Variable 
                temp=0 # Temp Variable (Default Zero For XOR)
                length=len(new_str)-1 # Length Of Input String -1 (To Ignore Last Bit)
                for i in range(length): # Loop For Calculate XOR Of Bits
                        temp=xor(temp,int(new_str[i]))
                if xor(temp,int(new_str[-1]))==1: # Comapre Loop Result And Parity Bit And Return Boolean Value
                        return True
                else:
                        return False
        except:
                print("Error In Detectting Odd Parity")
                return None
        
def repeat_gen(error_object):
        '''
        repeat_gen(error_object) -> String
        This Function Get An Error_Object As Input And Return Modified String As Output , Default Input Is Hex
        '''
        try:
                new_str="" # Empty String
                if what(error_object.str)=="hex": # Condition For Checking Binary Or Hex (Default Is Hex)
                        new_str=error_object.str
                elif what(error_object.str)=="bin":
                        new_str=bin_2_hex(error_object.str)
                
                return new_str*error_object.flag  #Return flag number of input string that cat together
        except:
                print("Error In repeat Generation")
                return None

def repeat_det(error_object):
        '''
        repeat_det(error_object) -> Boolean
        This Function Get An Error_object As Input And Return A Boolean Value As Output , Default Output Is Hex
        '''
        try:
                new_str=error_object.str  # Copy Error Object String In New String Variable 
                temp=None # Temp Variable With Default None 
                length=len(new_str) #Length Of Input String
                repeat_number=int(error_object.flag) #Number Of Repeat That Extract From Method
                message_length=length//repeat_number # Calc Orignal Message
                original_message=new_str[0:message_length] # Extract Orignal Message From Input String
                for i in range(repeat_number): # Loop For Compare Orignal Message With Each Of Repeated
                        temp=new_str[i*message_length:(i+1)*message_length]
                        if temp!=original_message: # If One Of The Compare Result Is False Break And Return False Else True
                                return False
                return True
        except:
                print("Error In Repeat Detection")
                return None

def hamming_gen(error_object):
        '''
        hamming_gen(error_object) -> String
        This Function Get An Error_object As Input and Return Modified String By Hamming Code Method As Output , Default Input Is Binary
        '''
        try:
                new_str="" # Empty String
                if what(error_object.str)=="bin": # Condition For Checking Binary Or Hex (Default Is Bin)
                        new_str=error_object.str
                elif what(error_object.str)=="hex":
                        new_str=hex_2_bin(error_object.str)
                length=len(new_str) # Length Of Input String
                parity_number=int(log(length,2))+1 # Calc Number Of Needed Parity Code
                parity_index=[] # Empty List Of Parity Index 
                message=[] # Empty List As Message
                p1=[0,2,4,6,8,10,12,14,16,18] # Parity-1 Indexs
                p2=[1,2,5,6,8,9,13,14,17,18] # Parity-2 Indexs
                p4=[3,4,5,6,11,12,13,14,19] # Parity-4 Indexs
                p8=[7,8,9,10,11,12,13,14] # Parity-8 Indexs
                p16=[15,16,17,18,19] # Parity-16 Indexs
                k=0 # Iteration Number
                parity_number_index=1 # Parity Number Index
                for i in range(length): # Loop For Extract available parity index in input message and added to parity _index
                        if int(2**i)<=length and parity_number_index<=parity_number:
                                parity_index.append(int(2**i)-1)
                                parity_number_index=parity_number_index+1 # nubmer of total parity in string
                for i in range(length+len(parity_index)): # Modified A Init List For Hamming Code Output
                        if i in parity_index:   # By Inserting 0 in Parity Location
                                message.append("0")
                        else:
                                message.append(new_str[k]) # And Insert Original Message Between them
                                k=k+1 # Iter
                for i in range(length+len(parity_index)): # Calc Each Parity Bit In Message And Generate Hamming Output
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
                result="".join(message) # Use Join Method to Convert List To String
                return result
        except:
                print("Something Wrong In Generating Hamming Code")
                return None
                      
def hamming_det(error_object):
        '''
        hamming_det(error_object) -> Boolean
        This Function Get An Error_Object As Input And Return Boolean Value As Output (Default Input In Binary)
        '''
        try:
                new_str=error_object.str # Copy Error Object String In New String Variable 
                length=len(new_str) # Length Of Input String
                parity_index=[] # Empty List As Parity Index
                message=list(new_str) # Convert Input String To List
                parity_value=[] # Empty List As Parity Bit Values
                p1=[2,4,6,8,10,12,14,16,18] # Parity-1 Indexs-Modified
                p2=[2,5,6,8,9,13,14,17,18] # Parity-2 Indexs-Modified
                p4=[4,5,6,11,12,13,14,19] # Parity-4 Indexs-Modified
                p8=[8,9,10,11,12,13,14] # Parity-8 Indexs-Modified
                p16=[16,17,18,19] # Parity-16 Indexs-Modified
                for i in range(length): #Loop For Extract Parity Index And Added To Parity_Index
                        if int(2**i)<=length:
                                parity_index.append(int(2**i)-1)
                                parity_value.append(new_str[int(2**i)-1])
                        else:
                                break

                for i in range(length): # Loop For Calc Each Parity Bit And Store In Parity Value
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
                
                if bin_2_dec(parity_value)==0: # If Parity Bits Represent 0 Return True (Without One Bit Error)
                        return True
                else:
                        output="Error Bit Number : "+str(bin_2_dec(parity_value)) # Else Return The Number Of Error Bits
                        print(output)
                        return False
        except:
                print("Something Wrong With Hamming Code")
                return None
                
def checksum_gen(error_object):
        '''
        checksum_gen(error_object) -> String
        This Function Get An Error_Object As Input And Return Modified String By Checksum (Default Input Is Hex)
        '''
        try:
                new_str="" # Empty String
                if what(error_object.str)=="hex":  # Condition For Checking Binary Or Hex (Default Is Bin)
                        new_str=error_object.str
                elif what(error_object.str)=="bin":
                        new_str=bin_2_hex(error_object.str)
                length=len(new_str) # Length Of Input String
                temp=0 # Temp Variable 
                for i in new_str: # Calc Sum Of Bits And Store In Temp
                        temp=temp+hex_dict[i]
                temp=hex(temp) # Convert Decimal To Hex
                temp=temp[2:] # Delete Python Hex Sign
                final_string=new_str+temp # Add temp To the end of Orignal Message
                return final_string # Return Modified String
        except:
                print("Error In Checksum Generator")
                return None
        
def checksum_det(error_object):
        '''
        checksum_det(error_object) -> Boolean
        This Function Get An Error Obejct As Input And Return A Boolean Value As Output (Default Input Is Hex)
        '''
        try:
                new_str=error_object.str # Copy Error Object String In New String Variable 
                checksum=new_str[-2:]  # Extract Checksum number
                temp=0 # Temp Variable 
                for i in new_str[:-2]: # Calc Sum Of The Bits - Checksum
                        temp=temp+hex_dict[i]
                temp=hex(temp) # Convert Decimal to Hex
                temp=temp[2:] # Delet Python Hex Sign
                if temp==checksum: # Compare To Checksum Value If Its Identical Return True Else False
                        return True
                else:
                        return False
        except:
                print("Error in Checksum Detector")
                return None
def crc_gen(error_object,poly):
        '''
        crc_gen(error_object , str) -> String
        This Function Get An Error_object And Polynomial Coef As Input And Return Modified String By CRC Method And That Poly As Output
        '''
        try:
                new_str="" # Empty String
                if what(error_object.str)=="bin": # Condition For Checking Binary Or Hex (Default Is Bin)
                        new_str=error_object.str
                elif what(error_object.str)=="hex":
                        new_str=hex_2_bin(error_object.str)
                divider_len=len(poly) # Length Of Divider (Length Of Polynomial)
                extra_bit_len=divider_len-1 # Extra Bits  = Polynomial Degree
                message=new_str+(extra_bit_len)*"0" # Add Zero At The End Of The Orignal Message 
                length=len(message) # Length Of Modified Message
                length_init=len(new_str) # length Of Original Message
                message=list(message) # Convert Message String tO lIST
                start_index=0 # start_index variable default zero
                cond_list=["0"]*length_init # Generate Stop Condition Of CRC Method
                while(message[0:length-(extra_bit_len)]!=cond_list ): # Main Codition For Continue Divide
                        temp=message[start_index:start_index+divider_len] # Subset Message By Divider Length
                        for i in range(divider_len): # XOR Subset By Divider And Replace In Message
                                temp[i]=str(xor(int(temp[i]),int(poly[i])))
                        message[start_index:start_index+divider_len]=temp
                        for j in range(length): # Find Next Bit 1 And Update strat_index
                                if message[j]=="1":
                                        start_index=j
                                        break
                result="".join(message[length-(extra_bit_len):]) # Convert List To String
                return new_str+result # Return Modified String
        except:
                print("Something Wrong In Generating Error_Detection Object!!")
                return None
                        
                
        
def crc_det(error_object,poly):

        '''
        crc_det(error_object) -> Boolean
        This Function Get An Error_Object And Return Boolean Value As Output ( Default Input Is Hex)
        '''
        try:
                new_str=error_object.str # Copy Error Object String In New String Variable 
                divider_len=len(poly) # Length Of Divider
                extra_bit_len=divider_len-1 # Length Of Extra Bits (Polynomial Degree)
                message=list(new_str) # Conert Input Message To List
                length=len(message) # Length Of Message
                start_index=0 # Start Index
                cond_list=["0"]*(length-extra_bit_len) # Stop Conditional
                while(message[0:length-extra_bit_len]!=cond_list): # Main Condition For Continue CRC Method
                        temp=message[start_index:start_index+divider_len] # Subset Message By Divider Length
                        for i in range(divider_len): # Calc XOR Of Poly And Subset And Replace In Message
                                temp[i]=str(xor(int(temp[i]),int(poly[i])))
                        message[start_index:start_index+divider_len]=temp
                        for j in range(length): # Find Next 1 Bit And Update Start_index
                                if message[j]=="1":
                                        start_index=j
                                        break
                if "".join(message[length-extra_bit_len:])==(divider_len-1)*"0": # Check If Reminder Is Equal Zero Return True Else Return False
                        return True
                else:
                        return False
        except:
                print("Something Wrong In Detecting Error In Object")
                return None
        
        

        
