from PIL import Image

# Open the image file
with Image.open('image test couleurs.png') as image:
    # Load the pixel data
    pixel_data = image.load()

    # Create an empty string to store the alphabet
    alphabet = ""

    # Iterate over the pixels in the image
    for x in range(image.width):
        for y in range(image.height):
            # Get the pixel color
            pixel = pixel_data[x, y]

            # Add the corresponding letter to the alphabet based on the pixel color
            if pixel == (255, 0, 0): #rouge
                alphabet += "A"
            elif pixel == (0, 255, 0): #vert
                alphabet += "B"
            elif pixel == (0, 0, 255): #bleu
                alphabet += "C"
            elif pixel == (255,255,255): #blanc
                alphabet += "D"

    # Print the alphabet
    print(alphabet)
alphabet=[]
def selec(liste):
    for i in range(liste):
        if liste[i]==liste[i+1]:
            