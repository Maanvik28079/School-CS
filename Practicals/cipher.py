def encryptMenu():
    print("")
    print("-------- MENU --------", end="\n\n")
    print("1. Encrypt")
    print("2. Decrypt", end="\n\n")
    func = int(input("Please choose one of the above: "))

    if func == 1:
        return "Encrypt"
    else:
        return "Decrypt"
    
def mainMenu():
    process = encryptMenu()
    print('')
    str_to_process = input(f"What is the string you would like to {process}? ")
    print('')
    rot = input("Please enter rotational value: ")
    
    try:
        rot = int(rot)
    except Exception as e:
        rot = 13    
    
    rot = rot % 26
    
    return process, str_to_process, rot

def encryptString(str, rot):
    f_list = []
    for s in str:
            
            if s.isalpha():
                
                if ord(s) >= 97:
                    
                    if ord(s) + rot > 122:
                        final = ord(s) + rot - 26
                        
                    else:
                        final = ord(s) + rot
                        
                else:
                    
                    if ord(s) + rot > 90:
                        final = ord(s) + rot - 26
                        
                    else:
                        final = ord(s) + rot
                
            else:
                final = ord(s)
            
            f_list.append(chr(final))
            
    return f_list
    
def decryptString(str, rot):
    f_list = []
    for s in str:
            
            if s.isalpha():
                
                if ord(s) >= 97:
                    
                    if ord(s) - rot < 97:
                        final = ord(s) - rot + 26
                        
                    else:
                        final = ord(s) - rot
                        
                else:
                    
                    if ord(s) - rot < 65: 
                        final = ord(s) - rot + 26
                        
                    else:
                        final = ord(s) - rot
                
            else:
                final = ord(s)
            
            f_list.append(chr(final))  
    
    return f_list

def main():
    
    process, str_to_process, rot = mainMenu()
    
    if process == "Encrypt":
        processed_list = encryptString(str_to_process, rot)
        
    else:
        processed_list = decryptString(str_to_process, rot)
        
        
        
    processed_string = "".join(processed_list)
    print(f"Output: {processed_string}")


if __name__ == "__main__":
    main()
