# Converts a hexadecimal pixel value (#FFFFFF) into RGB-format:
# (255, 255, 255)
# Useful when using Image.fromarray()

def hex_to_int(hex_pixel):
    hex_pixel = hex_pixel[1:]
    int_pixel = [int(hex_pixel[i:i+2], 16) for i in range(0, len(hex_pixel), 2)]
    return int_pixel
