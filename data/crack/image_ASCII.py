from PIL import Image


def text_to_bin(message):
    ord_message = [ord(letter) for letter in message]
    bin_message = [bin(letter)[2:] for letter in ord_message]
    for i in range(len(bin_message)):
        while len(bin_message[i]) <7:
            bin_message[i] = "0" + bin_message[i]
    return bin_message


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

        for x in range(len(bin_message)):
            for i in range(7*x, 7*x+7):
                if new_im[line][i][color] > 128:
                    if new_im[line][i][color] % 2 != int(bin_message[x][i % 7]):
                        new_im[line][i][color] = new_im[line][i][color] - 1
                else:
                    if new_im[line][i][color] % 2 != int(bin_message[x][i % 7]):
                        new_im[line][i][color] = new_im[line][i][color] + 1
    return new_im
    

def decode(image=None, text=None, line=0, color=0):
    if image is not None:
        text = ""
        for i in range(int(len(image[0])//7)):
            letter = ''
            for a in range(i*7, i*7+7):
                letter += str(image[line][a][color] % 2)
            text += chr(int(letter, base=2))
        return text
    ntext = ""
    for i in text:
        ntext += chr(int(i, base=2))
    return ntext


a = code("../image/theline.png")

imn = Image.new("RGBA", (len(a[0]),len(a)))
for y in range(len(a)):
    for x in range(len(a[0])):
        imn.putpixel((x,y), tuple(a[y][x]))
print(decode(image=a))
imn.show()
