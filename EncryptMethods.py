from Ceasarscipher import caesar_cipher
from AbtashCipher import atbash
from ColumnarTranspositionCipher import transpositionCipher
ch=1
while ch!=0:
    print("(1) Ceasar's Cipher")      #Do not forget to add the encryption method option
    print("(2) Atbash Cipher")        # in the menu
    print("(3) ColumnarTranspositionCipher")
    print("(0) Exit Menu")
    ch=int(input("Enter Encryption choice (1/2/3/0): ")) #Also update the choices here
    if ch==1:
        s=input("Enter String: ")
        k=int(input("Enter the shift value: "))
        s=caesar_cipher(s, k)
        print(s)
    
    elif ch==2:
        string=input("Enter String: ")
        string=atbash(string)
        print(string)

    elif ch==3:
        message = input("Enter Message: ")
        key = int(input("Enter key: "))
        message = transpositionCipher(key,message) 
        print(message)
    
       
