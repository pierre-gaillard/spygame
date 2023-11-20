from PIL import Image


def text_to_bin(message):
    return ''.join(format(ord(i), '08b') for i in message)


def bin_to_text(message):
    return "".join([chr(int(x, 2)) for x in [message[i:i + 8]for i in range(0, len(message), 8)]])


def code(image, line=0, color=0, message=None):
    im = Image.open(image)
    
    new_im = []
    w, h = im.size

    im = im.load()
    for y in range(h):
        new_im.append([])
        for x in range(w):
            new_im[y].append([a for a in im[x, y]])

    if message is not None:
        bin_message = text_to_bin(message)
        if len(bin_message)>len(new_im):
            return "error"
        for x in range(len(bin_message)):
            if new_im[line][x][color] > 128:
                if new_im[line][x][color] % 2 != int(bin_message[x]):
                    new_im[line][x][color] = new_im[line][x][color] - 1
            else:
                if new_im[line][x][color] % 2 != int(bin_message[x]):
                    new_im[line][x][color] = new_im[line][x][color] + 1
    return new_im

        
def decode(image=None, text=None, color=0):
    if image is not None:
        bin_message = ''
        for i in range(int(((len(image[0]))//8)*8)):
            bin_message += str(image[0][i][color] % 2)
        print(bin_message)
        return bin_to_text(bin_message)


#print(text_to_bin("test"), bin_to_text(text_to_bin("test")))

a = code("profile.png")
imn = Image.new("RGBA", (len(a[0]), len(a)))
for y in range(len(a)):
    for x in range(len(a[0])):
        imn.putpixel((x,y), tuple(a[y][x]))
print(decode(image=a))
#imn.save("labyrinthe.png", "png")
imn.show()
