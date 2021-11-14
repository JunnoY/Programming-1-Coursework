import os, argparse, re, sys

#Terminal
parser = argparse.ArgumentParser(description='spellcheck_test')
parser.add_argument('englishtxtdirectory',help='Path to the englishtxt directory.')
parser.add_argument('inputDirectory',help='Path to the input directory.')
parser.add_argument('outputDirectory',help='Path to the output directory.')
args = parser.parse_args()
engtxtpath =args.englishtxtdirectory
inputpath = args.inputDirectory
outputpath = args.outputDirectory

def perform():
    file = open(inputcompleteName,"r")
    contents = file.read()
    text = ""
    global str0, str1, str2, str3, str4, str5, str6, str7, str8
    uppercase = 0
    punctuation = 0
    number = 0
    word = 0
    correctwords = 0
    incorrectwords = 0
    #remove number from content
    i=0
    while i < len(contents):
        if contents[i].isalpha() or contents[i]=="@" or contents[i]=="#":
            text = text + contents[i]
            if contents[i].isupper():
                uppercase += 1
                i += 1
            else:
                i += 1

        elif contents[i].isalnum():
            number += 1
            i += 1
        elif contents[i].isspace():
            text = text + " "
            i += 1
        # # elif not contents[i].isalpha() and not contents[i].isalnum() and not contents[i].isspace() and not contents[i]=="#" and not contents[i]=="@":
        elif contents[i:i+3]=="...":
            punctuation += 1
            i += 3
        else:
            punctuation += 1
            i+=1



    text = text.lower()
    print("text: " + str(text))
    print("Number of numbers removed: " + str(number))
    print("Number of punctuations removed: " + str(punctuation))

    #spell check
    words = text.split()
    word = len(words)
    file1 = open(engtxtpath, "r")
    checksheet =[]
    for line in file1:
        stripped_line = line.strip()
        checksheet.append(stripped_line)
    file1.close()
    for i in words:
        if i in checksheet:
            correctwords += 1
        else:
            print( i + " is wrong")
            incorrectwords += 1
    str0 = "d07769jy"
    str1 = "Formatting ###################"
    str2 = "Number of upper case letters changed: "+ str(uppercase)
    str3 = "Number of punctuations removed: " + str(punctuation)
    str4 = "Number of numbers removed: " + str(number)
    str5 = "Spellchecking ###################"
    str6 = "Number of words: " + str(word)
    str7 = "Number of correct words: " + str(correctwords)
    str8 = "Number of incorrect words: " + str(incorrectwords)


for inputfilename in os.listdir(inputpath):
    print(inputfilename)
    dot_index = int(inputfilename.find("."))
    inputcompleteName = os.path.join(inputpath, inputfilename)
    perform()
    outputfilename = (str(inputfilename[0:dot_index])+"_d07769jy.txt")
    outputcompleteName = os.path.join(outputpath, outputfilename)
    output = open(outputcompleteName,"w")  # think how to make an output file for every input file, maybe put this instruction in the loop
    output.write(str0+ "\n"+ str1 + "\n" + str2 + "\n" + str3 + "\n" + str4 + "\n" + str5 + "\n" + str6 + "\n" + str7 + "\n" + str8)
    output.close()












