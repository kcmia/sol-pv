def clear():
    print("\033[2J")

def locate(line, column=1):
    print("\033[{};{}H".format(line, column), end="")
    
def clearLine(line=None, column=None):
    if line is not None and column is not None:
        locate(line, column)
    elif line is not None:
        locate(line, 1)
        
    print("\033[K", end="")
    
def Print(cadena, line, column=1, delEnd=False):
    locate(line, column)
    if delEnd:
        clearLine()
    print(cadena, end="")
    
def Input(msg, line, column=1, delEnd=True):
    locate(line, column)
    if delEnd:
        clearLine()
    return input(msg)

def Format(style, colorText=37, colorBack=40):
    print("\033[{};{};{}m".format(style, colorText, colorBack), end="")

def Reset():
    Format(0)
