#echange de variable
def echange_var(var1,var2):
    """Echzngeur de variable"""
    temp = var1
    var1 = var2
    var2 = temp
    return var1,var2


a = int(input('ecrire un chiiffre : '))
b = int(input('ecrire un chiiffre : '))

print(echange_var(a,b))

