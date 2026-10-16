# takes the word and scrambles the letters
W = "COURTAB"
c = ""
for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    if i not in "COURTAB":
        c += i
x = W + c
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
b = ""
k = input("Enter the word: ")
j = k.upper()
for i in j:
    l = a.index(i)
    b += x[l]
print("Encrypted text letters:", b)

# takes the scrambled letters and then converts them to randomly assigned numbers
q = []
d = {'A':16,'B':5,'C':6,'D':23,'E':19,'F':3,'G':1,'H':15,'I':12,'J':4,'K':20,'L':2,'M':0,'N':9,'O':7,'P':8,'Q':21,'R':13,'S':10,'T':14,'U':25,'V':18,'W':11,'X':24,'Y':22,'Z':17}


for n in b:
    if n in d:
        q.append(d[n])
print("encrypted text's equivalent number version: ",q)
sequence=q

# BIDFID cipher
# Put everything into a 2-round loop
for round_num in range(2):
    
    # 1. FORWARD CHAIN
    new_list = []
    new_list.append(sequence[0])
    for i in range(1, len(sequence)):
        o = (sequence[i] + new_list[i-1]) % 26 # Added % 26 to keep numbers 0-25
        new_list.append(o)

    # 2. PERMUTATION 
    top_row = []
    bottom_row = []
    for g in range(len(new_list)):
        if g % 2 == 0:
            top_row.append(new_list[g])
        else:
            bottom_row.append(new_list[g]) 
    final_list = top_row + bottom_row

    # 3. BACKWARD CHAIN    
    for i in range(len(final_list) - 2, -1, -1):
        final_list[i] = (final_list[i] + final_list[i+1]) % 26

    # 4. PREPARE FOR NEXT ROUND
    sequence = final_list

print("Final Custom Avalanche Encrypted Numbers:", sequence)

list1=[]
s_box = [14, 2, 20, 17, 10, 18, 5, 15, 19, 7, 16, 9, 24, 3, 23, 1, 13, 12, 8, 22, 0, 25, 6, 11, 21, 4]
for l in sequence:
    list1.append(s_box[l])
print("the final encrypted message is: ",list1)