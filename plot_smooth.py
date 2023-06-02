# plot_smooth.py ### smooth coloring
# tried out by me, Jun 02, 2023, miro holec
# source: https://www.codingame.com/playgrounds/2358/how-to-plot-the-mandelbrot-set/mandelbrot-set
# author:
# date:
# additional explanation: https://goo.gl/D8Z3Mg Dr Holly Krieger from MIT

from PIL import Image, ImageDraw
from mandelbrot_smooth import mandelbrot, MAX_ITER

WIDTH=600
HEIGHT=400
#plot window
RE_START = -2
RE_END = 1
IM_START = -1
IM_END = 1

palette = []

im = Image.new('HSV', (WIDTH, HEIGHT), (0,0,0))
draw = ImageDraw.Draw(im)

for x in range(0,WIDTH):
    for y in range(0,HEIGHT):
        # convert pixel coordinate to a complex number
        c = complex(RE_START + (x/WIDTH) * (RE_END-RE_START),
                    IM_START + (y/HEIGHT)* (IM_END-IM_START))
        # Compute the number of iterations
        m = mandelbrot(c)
        # the color depends on the number of iterations
        hue = 255 - int (m * 255 / MAX_ITER)
        saturation = 255
        value = 255 if m< MAX_ITER else 0
        # plot the point
        draw.point([x,y], (hue,saturation,value))
im.convert('RGB').save('codin_smooth.png','PNG')

