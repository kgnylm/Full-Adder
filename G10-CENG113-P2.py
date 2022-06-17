"""
Authors:
270201090-Mustafa Kağan Yalım
290201031-Arda Polat
"""
anahtar=True
Flag1=True
Flag2=True
while Flag1:
#We defined Flag1 and Flag2 to not to use while True loops because using "break" was ground for penalty. 
    choose=input("Welcome to Full Adder!\n(1) Compute and Display the Outputs\n(2) Quit\nYou choose: ")
    
    if choose=="2":
        print("You have chosen option 2\nByee!!")
        Flag1=False
    
    elif choose=="1":
        Flag2=True
        base_choose=input("You have chosen option 1\nWhich base will you use to enter data lines (base 16/8/2)? ")
        liste=["2","8","16"]
        
        if base_choose not in liste:
            #We printed an error message when the user types any input other than 2,4 and 16.
            Flag2=False
            print("-"*32)
            print("You entered the wrong base type.")
            print("-"*32)
            
        while Flag2:
            
            anahtar=True
            deger=input("Please enter input: ")
            if deger.isalnum():
                #We used isalnum for our program to not to accept inputs like "-,space,_,blablabla"
            
                if base_choose=="2":
                    alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                    anahtar=True
                    
                    for i in deger:
                        if i.isalpha():
                            #When the user selects base type and types any string which we can't represent in binary(for ex. 43),anahtar returns False and prints error message
                            anahtar=False
                    
                    if anahtar:                        
                        for i in deger:
                            
                            if not i.isalpha():
                                
                                if len(deger)<3:
                                    #We created this part because the user can write 11,01,10,00 and we should calculate them
                                    #If input's lenght is shorter then 3, program will add 0 to input's left until input's lenght is equal to 3
                                    deger="0"*(3-len(deger))+deger

                                a,b,c_in=int(deger[0]),int(deger[1]),int(deger[2])
                                liste2=["2","3","4","5","6","7","8","9"]
                                #If the user type 56(for ex.),this block works and prints error message
                                for i in deger:
                                    if i in liste2:
                                        anahtar=False
                                
                                for i in deger[:-3]:
                                    if i=="1":
                                        #This block checks if the length of the input is more than 3 the digits and prints an error message if it includes any number other than 0
                                        anahtar=False
                                                                
                                if a == 0:
                                    #and,or,xor checks without bitwise operators
                                    if b == 0:
                                        if c_in == 0:
                                            sum = 0
                                            c_out = 0
                                        if c_in == 1:
                                            sum = 1
                                            c_out = 0
                                    if b == 1:
                                        if c_in == 0:
                                            sum = 1
                                            c_out = 0
                                        if c_in == 1:
                                            sum = 0
                                            c_out = 1
                                if a == 1:
                                    if b == 0:
                                        if c_in == 0:
                                            sum = 1
                                            c_out = 0
                                        if c_in == 1:
                                            sum = 0
                                            c_out = 1
                                    if b == 1:
                                        if c_in == 0:
                                            sum = 0
                                            c_out = 1
                                        if c_in == 1:
                                            sum = 1
                                            c_out = 1
                    
                    if anahtar==True :
                        #If everything is normal, our program shows sum and c_out.
                        print(f"Sum is {sum} C_out is {c_out}")
                        Flag2=False
                    
                    elif anahtar==False :
                        #If the input is not as we asked for user to type in, program prints error message.
                        print(f"Binary {deger} can not be represented with 3 bits! Please try again!")
                        #After this step, we will write comments for specific codes because some codes are very similar to the codes above.
                    
                elif base_choose=="8":
                    alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                    anahtar==True
                    
                    for i in deger:
                        if i.isalpha():
                            anahtar=False
                    
                    if anahtar:
                        
                        for i in deger:
                            
                            if i not in alphabet:                        
                                deger_decimal=0
                                #We wrote this code for octal to binary conversation.
                                for i in range(len(deger)):
                                    deger_decimal+=int(deger[::-1][i])*(8**i)
                                #Firstly, we convert octal to decimal and secondly, convert decimal to binary.
                                binary=""
                                
                                while deger_decimal !=0:
                                    
                                    binary=binary+str(deger_decimal%2)
                                    deger_decimal=deger_decimal//2
                                binary=binary[::-1]
                                
                                if len(binary)<3:
                                    binary="0"*(3-len(binary))+binary

                                a,b,c_in=int(binary[0]),int(binary[1]),int(binary[2])
                                                                
                                if "1" in binary[:-3]:
                                    anahtar=False
                                
                                if "1" not in binary[:-3]:
                                    anahtar=True
                                
                                if a == 0:
                                    if b == 0:
                                        if c_in == 0:
                                            sum = 0
                                            c_out = 0
                                        if c_in == 1:
                                            sum = 1
                                            c_out = 0
                                    if b == 1:
                                        if c_in == 0:
                                            sum = 1
                                            c_out = 0
                                        if c_in == 1:
                                            sum = 0
                                            c_out = 1
                                if a == 1:
                                    if b == 0:
                                        if c_in == 0:
                                            sum = 1
                                            c_out = 0
                                        if c_in == 1:
                                            sum = 0
                                            c_out = 1
                                    if b == 1:
                                        if c_in == 0:
                                            sum = 0
                                            c_out = 1
                                        if c_in == 1:
                                            sum = 1
                                            c_out = 1
                    
                    if anahtar==True:
                        print(f"Sum is {sum} C_out is {c_out}")
                        Flag2=False
                    
                    elif anahtar==False:
                        print(f"Octal {deger} can not be represented with 3 bits!Please try again!")

                elif base_choose=="16":
                    alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                    anahtar==True
                    
                    for i in deger:
                        if i.isalpha():
                            anahtar=False
                    
                    if anahtar:
                        
                        for i in deger:
                            if i not in alphabet:
                                deger_decimal=0
                                #Hexademical to binary conversation.
                                
                                for i in range(len(deger)):
                                    deger_decimal+=int(deger[::-1][i])*(16**i)
                                
                                binary=""
                                
                                while deger_decimal !=0:
                                    
                                    binary=binary+str(deger_decimal%2)
                                    deger_decimal=deger_decimal//2
                                binary=binary[::-1]
                                
                                if len(binary)<3:
                                    binary="0"*(3-len(binary))+binary

                                a,b,c_in=int(binary[0]),int(binary[1]),int(binary[2])
                                
                                if "1" in binary[:-3]:
                                    anahtar=False
                                
                                if "1" not in binary[:-3]:
                                    anahtar=True
                                
                                if a == 0:
                                    if b == 0:
                                        if c_in == 0:
                                            sum = 0
                                            c_out = 0
                                        if c_in == 1:
                                            sum = 1
                                            c_out = 0
                                    if b == 1:
                                        if c_in == 0:
                                            sum = 1
                                            c_out = 0
                                        if c_in == 1:
                                            sum = 0
                                            c_out = 1
                                if a == 1:
                                    if b == 0:
                                        if c_in == 0:
                                            sum = 1
                                            c_out = 0
                                        if c_in == 1:
                                            sum = 0
                                            c_out = 1
                                    if b == 1:
                                        if c_in == 0:
                                            sum = 0
                                            c_out = 1
                                        if c_in == 1:
                                            sum = 1
                                            c_out = 1
                    
                    if anahtar==True:
                        print(f"Sum is {sum} C_out is {c_out}")
                        Flag2=False
                    
                    elif anahtar==False:
                        print(f"Hexademical {deger} can not be represented with 3 bits!Please try again!")
            
            else:
                #Error message when the user doesn't type 2 or 8 or 16 while selecting the base.
                print("-"*14)
                print("Invalid input!")
                print("-"*14)
    
    else:
        #Error message when the user doesn't type 1 or 2 in the menu of the program.
        print("-"*14)
        print("Invalid input!")  
        print("-"*14)              