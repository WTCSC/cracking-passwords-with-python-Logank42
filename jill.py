import argparse, hashlib

def main():


    # INITATES THE PARSE
    parser = argparse.ArgumentParser(description = 'open_file')
    parser.add_argument('passwords')
    parser.add_argument('dictionary')
    args = parser.parse_args()


    # READS WORDLIST AND PASSWORDS
    passwordsfile = open(args.passwords, 'r') # opens the password file
    wordlistfile = open(args.dictionary, 'r') # opens the wordlist file
    username = []
    password = []

    for listedpassword in passwordsfile.readlines(): # reads through the passwords file
        UserPass = listedpassword.strip().split(':') # strips and splits the passwords
        username.append(UserPass[0]) # appends userpass to username
        password.append(UserPass[1]) # appends userpass to password

    wordlistlines = wordlistfile.readlines() # reads through the wordlist file


    # HASHES PASSWORDS AND COMPARES
    for i, Comparedpassword in enumerate(password): # gives index index to i and value to comparedpasswords
        for wordlist in wordlistlines: # starts the for loop
            Correctpassword = wordlist.strip() # assigning word from wordlist to correctpassword and striping
            sha256_hash = hashlib.sha256() # defines sha256_hash
            sha256_hash.update(Correctpassword.encode()) # encodes password using sha256_hash
            HashedPassword = sha256_hash.hexdigest() # gives back value in hexadecimal

            if Comparedpassword == HashedPassword: # compares the hashed passwords seeing if they match
                print(username[i] + ":" + Correctpassword) # prints our username followed by the correct password

if __name__ == "__main__":
    main()