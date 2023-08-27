def encode_lzw(data):
    letter=[]
    position=[]
    dicSize=128
    dictionary = {}
    for i in range(0,dicSize):
        c=chr(i)
        dictionary[c]=i
    foundChars=""
    result=[]
    for char in data:
        charsToAdd=foundChars+char
        if charsToAdd in dictionary:
            foundChars=str(dictionary[charsToAdd])
        else:
            result.append(foundChars)
            dictionary[charsToAdd]=dicSize
            dicSize=dicSize+1
            foundChars=str(dictionary[char])
    if (foundChars!=""):
        result.append(foundChars)
    return result



def decode_lzw(encodedNums):
    dictSize=128
    dictionary = {}
    for i in range(0,dictSize):
        c=chr(i)
        dictionary[i]=c
    characters=dictionary[int(encodedNums[0])]
    decodedString=""
    decodedString=decodedString+characters
    for i in range(1,len(encodedNums)):
        if int(encodedNums[i]) in dictionary:
            string=dictionary[int(encodedNums[i])]
        else:
            string=characters+characters[0]
        decodedString=decodedString+string
        dictionary[dictSize]=characters+string[0]
        dictSize=dictSize+1
        characters=string

    return decodedString





file = input("Enter the filename you want to compress: ")
with open(file, 'r') as f:
    stringToEncode = f.read()

result=encode_lzw(stringToEncode)
print(result)

   
output = open("encoded.txt","w+")
size = len(result)
for i in range(size):
    word =   str(result[i]) + ','
    output.write(word)
print("Compressed file generated as encoded.txt")


    
file = input("Enter the filename you want to decompress:")
f = open(file, "r").readline()
newList = f[1:len(f)-1].split(",")
encodedNums = []
for word in newList:
    if word == '':
        break
    encodedNums.append(int(word))
s=decode_lzw(encodedNums)
print(s)


