import PySimpleGUI as sg

alphabetBase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['.', '?', '!', '@', '#', '$', '%', '*', '&', '+', '-', '/', '=']

# Function to generate the encrypted alphabet


def generateEncryptedAlphabet(position):
    newAlphabet = alphabetBase.copy()
    for i in range(0, position+1):
      letter = newAlphabet.pop()
      newAlphabet.insert(0, letter)
    return newAlphabet

# Function to decipher the menssage
def decipherString(position, msg, option):
  newAlphabet = []
  newAlphabet = generateEncryptedAlphabet(position)
  # print(newAlphabet)
  decipheredString = ""
  for letter in msg:
    if (letter.isnumeric()):
      decipheredString += letter
    elif (letter in symbols):
      decipheredString += letter
    elif (letter in alphabetBase):
      if (option == "encrypted"):
        decipheredString += alphabetBase[newAlphabet.index(letter)]
      elif(option == "decrypted"):
        decipheredString += newAlphabet[alphabetBase.index(letter)]
    else:
      decipheredString += " "
  return decipheredString

layout = [
  [sg.T("Texto DECRIPTADO", font="Arial"), sg.Checkbox("All position", font="Arial", key="-ALL-")],
  [sg.Multiline(size=(58,10), font="Arial 10", key='-DEC-')], 
  [sg.T("Texto CRIPTOGRAFADO", font="Arial")],
  [sg.Multiline(size=(58,10), font="Arial 10", key='-CRI-')],
  [ sg.Slider(range=(0, 24), orientation="h", size=(38.5, 10), default_value=0, font="Arial 12", key="-POSITION-")],
  [sg.B("Criptografar", font="Arial", size=(20, 1)), sg.B("Decriptar",font="Arial", size=(20, 1))]
]

window = sg.Window("Criptogafia", layout)

while True:
  event, values = window.read()
  if (event == sg.WINDOW_CLOSED):
      break
  if (event):
    if (event == "Criptografar"):
      
      if (values["-ALL-"]):
        decipheredList = []
        for position in range(0, 25):
          encryptedText = values["-DEC-"].replace('\n','').lower()
          decipheredString = decipherString(position, encryptedText, 'decrypted')
          decipheredList.append(decipheredString)
        
        decipheredList.reverse()
        decipheredString = ""
        for string in decipheredList:
          decipheredString += string+"\n"
          
        window["-CRI-"].update(decipheredString)
      else:
        position = int(values["-POSITION-"])    
        encryptedText = values["-DEC-"].replace('\n','').lower()
        decipheredString = decipherString(position, encryptedText, 'encrypted')
        window["-CRI-"].update(decipheredString) 
        
    if (event == "Decriptar"):
      if (values["-ALL-"]):
        decipheredList = []
        for position in range(0, 25):
          encryptedText = values["-CRI-"].replace('\n','').lower()
          decipheredString = decipherString(position, encryptedText, 'decrypted')
          decipheredList.append(decipheredString)
        
        decipheredList.reverse()
        decipheredString = ""
        for string in decipheredList:
          decipheredString += string+"\n"
          
        window["-DEC-"].update(decipheredString)
      
      else:
        position = int(values["-POSITION-"])
        encryptedText = values["-CRI-"].replace('\n','').lower()
        decipheredString = decipherString(position, encryptedText, 'decrypted')
        window["-DEC-"].update(decipheredString)
window.close()
