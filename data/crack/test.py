from PIL import Image

def get_msg(name_couv):
    im = Image.open(name_couv)
    r, g, b, a = im.split()
    r = list(r.getdata())
    
    p = [str(x%2) for x in r[0:8]]
    q = "".join(p)
    q = int(q,2)
    
    n = [str(x%2) for x in r[8:8*(q+1)]]
    
    b = "".join(n)
    message = ""
    
    for k in range(0,q):
        l = b[8*k:8*k+8]
        message += chr(int(l,2))
        
    return message

print(get_msg("labyrinthe.png"))