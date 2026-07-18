# the stuff to encode and decode bro.
from letter_map import CharMap
rev_CharMap = {v:k for k, v in CharMap.items()} 
    
# flips the map by assigning char1 and char2 to v and k     
# then, flip k and v's positions in the list 😲✅🔥🔥

def encode(text):
    encoded = ""
    for char in text:
        encoded += CharMap.get(char, char)
    return encoded

def decode(Etext):
    decoded = ""
    for i in range(0, len(Etext), 4): # start at 0, stop at end of Etext and jump in 4 char jumps!
        block = Etext[i:i + 4]
        decoded += rev_CharMap.get(block,"NULL") # four bit character to show something is missing!!!
    return decoded
# now the main code stuff.*insert funny comment here* hahah! (stfu comment...)

print("Welcome to PPATKF r/w systems.\n")

while True:
    file = input("File: ")
    file = file + ".PPATKF"
    rw = input("\n Read or write?")

    if rw.lower() in ["read","r"]:
        with open(file, "r") as red:
           contents = red.read()
           Dectext = decode(contents)
           print(Dectext)

    elif rw.lower() in ["write", "w"]:
        with open(file, "a") as wrt:
            content = input("Append to file: ")
            encoded = encode(content)
            wrt.write(f"{encoded}")



# remeber guys, coding on an mobile ide is PAIN.lol