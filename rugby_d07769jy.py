import os, argparse, re

#Terminal
parser = argparse.ArgumentParser(description='rugby_test')
parser.add_argument('inputDirectory',help='Path to the input directory.')
parser.add_argument('outputDirectory',help='Path to the output directory.')
args = parser.parse_args()
inputpath = args.inputDirectory
outputpath = args.outputDirectory

def perform():
    global T1
    global T2
    i = 0
    x = 0
    y = 3
    T1 = 0
    T2 = 0
    file = open(inputcompleteName, "r") #check how to count the number of files in the path and create a for loop to open each file
    contents = file.read()
    times = int(len(contents) / 3)
    for i in range(times):
        character_set = contents[x:y]
        if int(character_set[1]) == 1:
            if character_set[2] == "t":
                T1 = T1 + 5
            elif character_set[2] == "c":
                T1 = T1 + 2
            elif character_set[2] == "p":
                T1 = T1 + 3
            elif character_set[2] == "d":
                T1 = T1 + 3
        elif int(character_set[1]) == 2:
            if character_set[2] == "t":
                T2 = T2 + 5
            elif character_set[2] == "c":
                T2 = T2 + 2
            elif character_set[2] == "p":
                T2 = T2 + 3
            elif character_set[2] == "d":
                T2 = T2 + 3
        x = x + 3
        y = y + 3



for inputfilename in os.listdir(inputpath):
    print(inputfilename)
    dot_index = int(inputfilename.find("."))
    inputcompleteName = os.path.join(inputpath, inputfilename)
    perform()
    if T1 > T2:
        print("The winner is Team 1")
    elif T1 == T2:
        print("The teams draw")
    else:
        print("The winner is Team 2")

    print(str(T1) + ":" + str(T2))
    outputfilename = (str(inputfilename[0:dot_index]) + "_d07769jy.txt")
    outputcompleteName = os.path.join(outputpath, outputfilename)
    output = open(outputcompleteName,"w")  # think how to make an output file for every input file, maybe put this instruction in the loop
    output.write(str(T1) + ":" + str(T2))
    output.close()