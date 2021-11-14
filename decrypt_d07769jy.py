import os, argparse, re, string
MORSE_CODE_DICT = {'.-':'a', '-...':'b', '-.-.':'c', '-..':'d', '.':'e',
                   '..-.':'f', '--.':'g', '....':'h', '..':'i', '.---':'j',
                   '-.-':'k', '.-..':'l', '--':'m', '-.':'n', '---':'o',
                   '.--.':'p', '--.-':'q', '.-.':'r', '...':'s', '-':'t',
                   '..-':'u', '...-':'v', '.--':'w', '-..-':'x', '-.--':'y',
                   '--..':'z',  '-----':'0', '.----':'1', '..---':'2',
                   '...--':'3', '....-':'4', '.....':'5', '-....':'6',
                   '--...':'7', '---..':'8', '----.':'9', '.-...':'&',
                   '.----.':"'", '.--.-.':'@', '-.--.':'(', '-.--.-':')',
                   '---...':':', '--..--':',', '-...-':'=', '-.-.--':'!',
                   '.-.-.-':'.', '-....-':'-', '-..-.':'/', '/':' ', '.-.-.':'+',
                   '.-..-.':'"', '..--..':'?', '-.-.-.':';'}
#Terminal
parser = argparse.ArgumentParser(description='rugby_test')
parser.add_argument('inputDirectory',help='Path to the input directory.')
parser.add_argument('outputDirectory',help='Path to the output directory.')
args = parser.parse_args()
inputpath = args.inputDirectory
outputpath = args.outputDirectory

def perform():
      global MORSE_CODE_DICT, result
      file = open(inputcompleteName, "r")
      contents = file.read()
      colon_index = int(contents.find(":"))
      if str(contents[0:colon_index]) == "Hex":
          print("Use hexadecimal method to decrypt")
          hexstring = str(contents[colon_index + 1: ])
          result = bytes.fromhex(hexstring)
          result = result.decode("utf-8") #or we can use hex for this one
          print(result.lower())

      elif str(contents[0:colon_index]) == "Morse Code":
          print("Use morse code method to decrypt")
          morsestring = str(contents[colon_index + 1: ])
          text = morsestring.split()
          list = []
          for x in range(0, len(text)):
              list += MORSE_CODE_DICT.get(text[x])
          result = "".join(list)
          print(result.lower())





      elif str(contents[0:colon_index]) == "Caesar Cipher(+3)":
          print("Use caeser cipher(+3) method to decrypt")
          caesarstring = str(contents[colon_index + 1: ])
          caesarstringPosition = 0
          alphabet = "abcdefghijklmnopqrstuvwxyz"
          result = ""
          for character in caesarstring:
                if character in alphabet:
                  position = alphabet.find(character)
                  new_position = (position - 3) % 26
                  new_character = alphabet[new_position]
                  result += new_character
                else:
                      result += character

          print(result.lower())


for inputfilename in os.listdir(inputpath):
    print(inputfilename)
    dot_index = int(inputfilename.find("."))
    inputcompleteName = os.path.join(inputpath, inputfilename)
    perform()
    outputfilename = (str(inputfilename[0:dot_index]) + "_d07769jy.txt")
    outputcompleteName = os.path.join(outputpath, outputfilename)
    output = open(outputcompleteName,"w")  # think how to make an output file for every input file, maybe put this instruction in the loop
    output.write(result.lower())
    output.close()






