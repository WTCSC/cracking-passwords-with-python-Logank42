import argparse, hashlib

def main():
    parser = argparse.ArgumentParser(description = 'open_file')
    
    parser.add_argument('dictionary')

    args = parser.parse_args()



    wordlistfile = open(args.dictionary, 'r')

    wordlistArr = []

    for word in wordlistfile.readlines():

        wordlistArr.append(word.strip())

    print(wordlistArr)

    wordlistfile.close()

    

    hashwordlistArr = []

    sha256_hash = hashlib.sha256()

    for password in wordlistArr:

        currentpassword = password.encode()

        sha256_hash.update(currentpassword)

        currentpassword = sha256_hash.hexigest()

        hashwordlistArr.append(currentpassword)



    crackedpasswords = []

    tempstr = ''

    for user in wordlistArr:

        for letter in user:

            tempstr += letter

            if letter == ':':
                crackedpasswords.append(tempstr)
                tempstr = ''
                print(crackedpasswords)
                break
    
if __name__ == "__main__":
    main()