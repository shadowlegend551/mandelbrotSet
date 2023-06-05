def mandelbrot(c, pixel_resolution):
    z = c

    for i in range(pixel_resolution):
        z = z**2+c
        # If z is guaranteed to escape to infinity.
        if z.real > 2 or z.imag > 2:
            return str(i+1)

    return False
