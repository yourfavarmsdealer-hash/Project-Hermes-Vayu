import math

# Ask for the final encrypted list 
cipher_input = eval(input("Enter the final encrypted numeric list: "))

# Setup your keys and tables 
s_box = [14, 2, 20, 17, 10, 18, 5, 15, 19, 7, 16, 9, 24, 3, 23, 1, 13, 12, 8, 22, 0, 25, 6, 11, 21, 4]

#  Undoing the final S-Block lookup
sequence = []
for num in cipher_input:
    # Find where the number sits inside your s_box list to find its original index
    original_val = s_box.index(num)
    sequence.append(original_val)


# THE REVERSE ROUNDS LOOP

for round_num in range(1, -1, -1):
    
    # UNDO THE BACKWARD CHAIN
    for i in range(len(sequence) - 1):
        sequence[i] = (sequence[i] - sequence[i+1]) % 26

    # RAIL SEPARATION CODE
    decrypted_list = sequence  # Links your variable name to the sequence data
    top_row = []
    bottom_row = []
    mid_point = math.ceil(len(decrypted_list) / 2)
    top_row = decrypted_list[:mid_point]
    bottom_row = decrypted_list[mid_point:]

    #  WEAVING POINTER CODE
    q_original = []
    k = 0
    l = 0
    for i in range(len(decrypted_list)):
        if i % 2 == 0:
            q_original.append(top_row[k])
            k += 1
        else:
            q_original.append(bottom_row[l])
            l += 1
            
    # FORWARD CHAIN SUBTRACTION CODE
    # reverse the forward chain,by counting backwards through the indices
    for i in range(len(q_original) - 1, 0, -1):
        q_original[i] = (q_original[i] - q_original[i-1]) % 26
        
    # Hands the data back to sequence so the loop can run the next round
    sequence = q_original


# DICTIONARY LOOKUP CODE
d = {'A':16,'B':5,'C':6,'D':23,'E':19,'F':3,'G':1,'H':15,'I':12,'J':4,'K':20,'L':2,'M':0,'N':9,'O':7,'P':8,'Q':21,'R':13,'S':10,'T':14,'U':25,'V':18,'W':11,'X':24,'Y':22,'Z':17}
scrambled_word = ""
for i in sequence:  
    for j in d:
        if i == d[j]:
            scrambled_word += j
print("The scrambled word is: ", scrambled_word)

# ALPHABET CONVERSION CODE
W = "COURTAB"
c = ""
for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    if i not in "COURTAB":
        c += i
x = W + c
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
b = ""
for i in scrambled_word:
    l = x.index(i)
    b += a[l]

print("The original coded message is: ", b)
print("Thank you for using PROJECT HERMES VAYU!!!! :) ")
