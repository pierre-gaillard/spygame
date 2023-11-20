def code_cesar(texte, cle):
    code = ""
    for lettre in texte:
        # chr transforme l'ASCII en texte et ord le texte en ASCII
        nouv_lettre = chr((ord(lettre) + cle - 97) + 97)
        code += nouv_lettre
    return code


def decode_cesar(code, cle):
    """
    texte = ""
    for lettre in code:
        nouv_lettre = chr(((ord(lettre) - cle - 97) + 97))
        texte += nouv_lettre
    #return texte
    """
    MessageClair = ""
    for i in range(len(code)):
        
        letter =ord(code[i])-cle
        while letter < 97:
            letter += 26
        MessageClair += chr(letter)
    return MessageClair

texte = "ozucfwhvaweis"
cle = 14
code = decode_cesar(texte, cle)
print("décodé:", code)

# ozucfwhvaweis
