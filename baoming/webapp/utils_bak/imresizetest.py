from PIL import Image


def aa():
    root = 'mv0111.jpg'
    img = Image.open(root)
    img = img.convert('RGB')
    resized = img.resize((400, 600))

    resized.save("1111111111111.jpg")

if __name__ == '__main__':
    aa()
