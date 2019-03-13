# --------------
##File path for the file 

def read_file(path):
    file = open(path,'r')
    sentence = file.readline()
    file.close()
    return sentence
sample_message = read_file(file_path)
#Code starts here


# --------------
#Code starts here
file_path_1 
file_path_2

def read_file(path):  
    #Opening of the file located in the path in 'read' mode
    file = open(path, 'r')
    #Reading of the first line of the file and storing it in a variable
    sentence=file.readline()
    #Closing of the file
    file.close()
    #Returning the first line of the file
    return sentence

def fuse_msg(message_a, message_b):
    quotient = (int(message_b)//int(message_a))
    return str(quotient)
#Calling the function to read file
message_1 = read_file(file_path_1)
message_2 = read_file(file_path_2)

secret_msg_1 =fuse_msg(message_1,message_2)

#Printing the line of the file
print(secret_msg_1)

#Code ends here



# --------------
#Code starts here
file_path_3

def read_file(path):
    file = open(path, 'r')
    sentence = file.readline()
    file.close
    return sentence

def substitute_msg(message_c):
    if(message_c == 'Red'):
        sub = 'Army General'
    elif(message_c == 'Green'):
        sub = 'Data Scientist'
    elif(message_c == 'Blue'):
        sub = 'Marine Biologist'
    return sub

message_3 = read_file(file_path_3)

secret_msg_2 = substitute_msg(message_3)

print(secret_msg_2)




# --------------
# File path for message 4  and message 5
file_path_4
file_path_5

#Code starts here

def read_file(path):
    file = open(path, 'r')
    sentence = file.readline()
    file.close()
    return sentence

def compare_msg(message_d, message_e):
    a_list = message_d.split()
    b_list = message_e.split()
    c_list= [i for i in a_list if i not in b_list]
    final_msg = " ".join(c_list)
    return final_msg

message_4 = read_file(file_path_4)
message_5 = read_file(file_path_5)
print(message_4)
print(message_5)

secret_msg_3 = compare_msg(message_4,message_5)







# --------------
#Code starts here
a_list = []
file_path_6
def read_file(path):
    file = open(path, 'r')
    sentence = file.readline()
    file.close()
    return sentence



def extract_msg(message_f):
    
    a_list = message_f.split()
    even_word = lambda x: bool(len(x) % 2==0)
    b_list = filter(even_word , a_list)
    final_msg=" ".join(b_list)
    
    #Returning the sentence
    return final_msg

message_6=read_file(file_path_6)

#Calling the function 'filter_msg'
secret_msg_4=extract_msg(message_6)

#Printing the secret message
print(secret_msg_4)




# --------------
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]

secret_msg = ' '.join(message_parts)

final_path= user_data_dir + '/secret_message.txt'


#Code starts here
message_part = []

def write_file(secret_msg, path):
    file = open(path, 'a+')
    file.write(secret_msg)
    file.close()

write_file(secret_msg, final_path)
print(secret_msg)


