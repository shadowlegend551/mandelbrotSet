from algorithm import mandelbrot
from pixelconvert import hex_to_int
from pson import load_json

import numpy as np

def pixel_increment(maximum: int, minimum: int, denominator:int) -> float:
    return abs(maximum - minimum) / denominator

def get_dynamic_height(width: int, screen_width_multiplier: float,
                       screen_height_multiplier: float) -> int:
    return int(width / screen_width_multiplier * screen_height_multiplier)

def get_dynamic_max_y(start_y: int, max_x: int, start_x: int,
                      screen_width_multiplier: float,
                      screen_height_multiplier: float) -> float:
    return start_y + (max_x - start_x) / screen_width_multiplier * screen_height_multiplier

def generate_raster(settings_file: str) -> np.ndarray:
    settings = load_json(settings_file)

    WIDTH = settings['width']
    START_X = settings['start_x']
    START_Y = settings['start_y']
    MAX_X = settings['max_x']
    SAF = settings['screen_auto_format']

    if SAF:
        WIDTH_MULTIPLIER, HEIGHT_MULTIPLIER = settings['aspect_ratio']

        HEIGHT = get_dynamic_height(WIDTH, WIDTH_MULTIPLIER, HEIGHT_MULTIPLIER)
        MAX_Y = get_dynamic_max_y(START_Y, MAX_X, START_X, WIDTH_MULTIPLIER, HEIGHT_MULTIPLIER)

    else:
        HEIGHT = settings['height']
        MAX_Y = settings['max_y']

    PIXEL_RESOLUTION = settings['resolution']
    fractal_color = hex_to_int(settings['fractal_color'])
    colormode = settings['color_mode']

    if colormode:
        color_scheme = settings['color_scheme']
        for colour in color_scheme:
            color_scheme[colour] = hex_to_int(color_scheme[colour])

    iterable_min_x = START_X
    iterable_min_y = START_Y
    raster = []

    for i in range(HEIGHT):
        raster.append([])

        for j in range(WIDTH):
            c = complex(iterable_min_x, iterable_min_y)
            z = c

            pixel_value = mandelbrot(c, PIXEL_RESOLUTION)

            if pixel_value and colormode:
                raster[i].append(color_scheme[pixel_value])
            elif pixel_value and not colormode:
                raster[i].append([255, 255, 255])
            else:
                raster[i].append(fractal_color)

            iterable_min_x += pixel_increment(MAX_X, START_X, WIDTH)

        iterable_min_x = START_X
        iterable_min_y += pixel_increment(MAX_Y, START_Y, HEIGHT)

    return np.array(raster, dtype=np.uint8)

