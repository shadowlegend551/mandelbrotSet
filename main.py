from raster import generate_raster
from pixelconvert import hex_to_int
from PIL import Image

def main():
    array = generate_raster('settings.json')
    img = Image.fromarray(array)
    img.save('hello.png')

if __name__ == '__main__':
    main()
