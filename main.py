from raster import generate_raster
from pixelconvert import hex_to_int
from PIL import Image

def main():
    arr = generate_raster('settings.json')
    img = Image.fromarray(arr)
    img.save('hello.png')

if __name__ == '__main__':
    main()
