from PIL import Image
from matplotlib import pyplot as plt



def openImage(image):
    imageRGB = Image.open(image)
    print("image opend")
    return imageRGB


def showImage(image):
    plt.imshow(image)
    plt.show()


def saveImage(name, image):

    plt.imsave(name, image)


def getshape0(image):

    S = image.size[0]
    return S


def getshape1(image):
    S = image.size[1]
    return S


def resize(image):
    resized_im = image.resize((round(100), round(100)))
    return resized_im


def get_position(logo, image, pos):
    if pos == "topleft": return (0, 0)
    if pos == "bottomleft": return (0, int(getshape1(image) - getshape1(logo)))
    if pos == "topright": return (int(getshape0(image) - getshape0(logo)), 0)
    if pos == "bottomright": return (int(getshape0(image) - getshape0(logo)), int(getshape1(image) - getshape1(logo)))
    if pos == "center": return ((int((getshape0(image) - getshape0(logo)) / 2), int(((getshape1(image) - getshape1(logo)) / 2))))


def watemark(image, logo, position, savename):
    image = openImage(image).convert("RGBA")
    logo = openImage(logo).convert("RGBA")
    watermark = resize(logo).convert("RGBA")
    width, height = image.size
    p = get_position(watermark, image, position)

    transparent = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    transparent.paste(image, (0, 0))
    transparent.paste(watermark, p, watermark)
    im = transparent.convert("RGB")
    im.show()
    im.save(savename)



