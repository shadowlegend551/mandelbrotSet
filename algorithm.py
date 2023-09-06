def mandelbrot(c: complex, pixel_resolution: int) -> str:
    ESCAPE_BOUNDARY = 2
    z = c

    for iteration_count in range(1, pixel_resolution):
        z = z**2+c

        # If the real or imaginary part is over 2,
        # the value is guaranteed to escape to infinity.
        if z.real > ESCAPE_BOUNDARY or z.imag > ESCAPE_BOUNDARY:
            return str(iteration_count)

    return False

