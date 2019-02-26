lPuntuacion = ",;.:"
lVocales = "aeiouáéíóúü"
lConsonantes = "bcdfghjklmnñpqrstvwxyz"
lDigitos = "0123456789"
lTodos = lVocales + lConsonantes + lDigitos
lAlfabeticos = lVocales + lConsonantes
lOcultos = "\n\t"
lSeparadorPalabras = " " + lOcultos

def estadisticas(text):

    total = {
        'vocales': 0,
        'consonantes': 0,
        'digitos': 0,
        'otros': 0,
        'otros_no_espacio': 0,
        'mayúsculas': 0,
        'minúsculas': 0,
        'párrafos': 0,
        'palabras': 0,
        'caracteres': 0,
    }
    lista = {
        'vocales': [],
        'consonantes': [],
        'digitos': [],
        'otros':[],
        'otros_no_espacio': [],
        'mayúsculas': [],
        'minúsculas': [],
        'párrafos': [],
        'palabras': [],
        'caracteres': []
    }

    if len(text) == 0:
        return total, lista

    if text[-1] != '\n':
        text += '\n'
        total['caracteres'] = -1


    caracterAnt = ' '
    for caracter in text:
        minCaracter = caracter.lower()
        if minCaracter in lVocales:
            total['vocales'] += 1
            lista['vocales'].append(caracter)
        if minCaracter in lConsonantes:
            total['consonantes'] += 1
            lista['consonantes'].append(caracter)
        if minCaracter in lDigitos:
            total['digitos'] += 1
            lista['digitos'].append(caracter)
        if minCaracter not in lTodos:
            total['otros'] += 1
            lista['otros'].append(caracter)
            if minCaracter not in lSeparadorPalabras:
                total['otros_no_espacio'] += 1
                lista['otros_no_espacio'].append(caracter)
            if caracter in lSeparadorPalabras and caracterAnt not in lSeparadorPalabras:
                total['palabras'] += 1
                lista['palabras'].append(caracter)

        if caracter in lAlfabeticos:
            total['minúsculas'] += 1
            lista['minúsculas'].append(caracter)
        
        if caracter in lAlfabeticos.upper():
            total['mayúsculas'] += 1
            lista['mayúsculas'].append(caracter)

        if caracter == '\n':
            total['párrafos'] += 1
            lista['párrafos'].append(caracter)
        
        if caracter not in lOcultos:
            total['caracteres'] += 1
            lista['caracteres'].append(caracter)

        caracterAnt = caracter

    return (total, lista)

def loopReplace(txt, old, new):
    '''
    Reemplaza old por new hasta que no hay más apariciones de old
    '''
    while txt.find(old) >= 0:
        txt = txt.replace(old, new)
    return txt

def isEllipsis(txt, pos):
    '''
    Comprueba si una posición va antecedida de puntos suspensivos (han de ser tres al menos)
    '''
    if pos > 2:
        return txt[pos-3:pos] == '...'
    return False

def betweenDigitsOrPuncts(txt, pos):
    if pos > 0 and pos < len(txt)-1:
        return (txt[pos-1].isdigit() and txt[pos+1].isdigit()) or txt[pos+1] in lPuntuacion
    return False

def punctuationWithoutSpaces(txt):
    newText = ""
    caracterAnt = ""
    for caracter in txt:
        if caracter in lPuntuacion and caracterAnt == ' ':
            newText = newText[:-1]
        if caracter == ' ' and caracterAnt in lPuntuacion:
            pass
        else:
            newText += caracter
        caracterAnt = caracter
    return newText

def upperAfterPoint(txt):
    pos = 0
    newText = ""
    caracterAnt = ""
    for caracter in txt:
        newText += caracter
        if caracter in lPuntuacion and not betweenDigitsOrPuncts(txt, pos):
            newText += " "
        if caracterAnt == '.' and caracter != '.' and not isEllipsis(txt, pos):
            newText = newText[:-1] + caracter.upper()
        
        pos += 1
        caracterAnt = caracter
    return newText

def textCorrection(txt):
    if len(txt) == 0:
        return txt
    txt = loopReplace(txt, "    ", "\t")
    txt = loopReplace(txt, "  ", " ")
    txt = punctuationWithoutSpaces(txt)
    txt = upperAfterPoint(txt)
    txt = txt.strip()
    txt = txt[0].upper() + txt[1:]
    if txt[-1] != '.':
        txt += '.'
    return txt