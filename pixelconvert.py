# Converts a hexadecimal pixel string (e.g. "#FFFFFF") into RGB-format:
# ([255, 255, 255])
# Useful when using Image.fromarray().

def hex_to_int(pixel_as_hex):

    # Remove the heading hashtag.
    pixel_as_hex = pixel_as_hex[1:]

    # Some list comprehension magic.
    pixel_as_int = [int(pixel_as_hex[i:i+2], 16) \
                    for i in range(0, len(pixel_as_hex), 2)]

    return pixel_as_int
