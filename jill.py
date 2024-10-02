import argparse, hashlib

def main():
    parser = argparse.ArgumentParser(description = 'open_file')

    parser.add_argument('passwords')

    parser.add_argument('dictionary')

    args = parser.parse_args()



    passwords = open(args.passwords, 'r')

    wordlistfile = open(args.dictionary, 'r')
    # passwordsArr = []

    for password in passwords.readlines():

        #passwordsArr.append(word.strip())

        passworD = password.strip().split(':')

        print(passworD)
        


    # password[0] => username, password[1] => hashed password
    username = []
    username.append(passworD[0])
    passWord = []
    passWord.append(passworD[1])
    finalpassword = []
    for wordlist in wordlistfile.readlines():
        #wordlistArr.append(word.strip())
        currentpassword = wordlist.encode()
        
        sha256_hash = hashlib.sha256()
        sha256_hash.update(currentpassword)
        currentPassword = sha256_hash.hexdigest()
        finalpassword.append(currentPassword)
    if currentpassword == passworD[1]:
        pass   
    
        # hashwordlistArr.append(currentpassword)
        
         #   print(password)
    print(finalpassword)
if __name__ == "__main__":
    main()