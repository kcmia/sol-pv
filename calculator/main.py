from screen import *
import colorama

_BOLD_ON = 1
_UNDERLINE_ON = 4
_FORMAT_OFF = 0
ops = ('+', '-', 'x', '/', '%', '//', '^')
calcParams = {
    'op1': None,
    'op2': None,
    'funcion': '',
    'solucion': 0
}
register = []

def displayLayout():
    clear()
    Format(_UNDERLINE_ON)
    Format(_BOLD_ON)
    Print("Sol  :",2 ,1)
    Print("op1:", 2, 28)
    Print("op2:", 3, 28)
    Print("f:", 4, 30)
    Print("Input:", 5)
    Format(_FORMAT_OFF)

def fValue(valor):
    try:
        return float(valor)
    except:
        return None

def retrieveNumber(number, format="{:8.2f}"):
    return format.format(number) if number != None else ''

def opera():
    if calcParams['funcion'] ==   '+':
        solucion = calcParams['op1']  + calcParams['op2']  
    elif calcParams['funcion'] ==   '-':
        solucion = calcParams['op1']  - calcParams['op2']  
    elif calcParams['funcion'] ==   'x':
        solucion = calcParams['op1']  * calcParams['op2']  
    elif calcParams['funcion'] ==   '/':
        solucion = calcParams['op1']  / calcParams['op2']  
    elif calcParams['funcion'] ==   '//':
        solucion = calcParams['op1']  // calcParams['op2']  
    elif calcParams['funcion'] ==   '%':
        solucion = calcParams['op1']  % calcParams['op2']  
    elif calcParams['funcion'] ==   '^':
        solucion = calcParams['op1']  ** calcParams['op2']  
    else:
        return None
    return solucion

def appendLinea():
    linea = "{} {} {} = {}\n".format(retrieveNumber(calcParams['op1']), calcParams['funcion'], retrieveNumber(calcParams['op2']), retrieveNumber(calcParams['solucion']))
    register.append(linea)

def showData():
    Print(retrieveNumber(calcParams['solucion']), 2, 8)
    Print(retrieveNumber(calcParams['op1']), 2, 33)
    Print(retrieveNumber(calcParams['op2']), 3, 33)
    Print(calcParams['funcion'], 4, 33)

def resetParams(all=False):
    if not all:
        calcParams['op1']  = calcParams['solucion']
    else:
        calcParams['op1']  = None
        calcParams['funcion'] = None
    calcParams['op2']  = None

def asigna(valor):
    numericValor = fValue(valor)
    if numericValor != None:
        if calcParams['funcion'] ==  '':
            calcParams['op1']  = numericValor
        elif calcParams['funcion'] in ops:
            calcParams['op2']  = numericValor
            calcParams['solucion'] = opera()
            appendLinea()
            resetParams()
    elif valor in ops:
        calcParams['funcion'] = valor
    
    showData()

def mainCycle():
    entrada = Input('', 5, 8)
    while entrada.upper() != 'FIN':
        asigna(entrada)
        entrada = Input('', 5, 8)

def saveRegister():
    fcalc = open('calculos.txt', 'w+')
    for linea in register:
        fcalc.write(linea)
    fcalc.close()

if __name__ == '__main__':
    colorama.init()
    displayLayout()
    mainCycle()

    saveRegister()
