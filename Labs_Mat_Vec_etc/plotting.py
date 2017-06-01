# Copyright 2013 Philip N. Klein
"""
This file contains a simple plotting interface, which uses a browser with SVG to
present a plot of points represented as either complex numbers or 2-vectors.

"""

import webbrowser
from numbers import Number

import tempfile
import os
import atexit
from math import pi, e
_browser = None

def plot(L, scale=4, dot_size = 3, browser=None):
    """ plot takes a list of points, optionally a scale (relative to a 200x200 frame),
        optionally a dot size (diameter) in pixels, and optionally a browser name.
        It produces an html file with SVG representing the given plot,
        and opens the file in a web browser. It returns nothing.
    """
    scalar = 200./scale
    origin = (210, 210)
    hpath = create_temp('.html')
    with open(hpath, 'w') as h:
        h.writelines(
            ['<!DOCTYPE html>\n'
            ,'<head>\n'
            ,'<title>plot</title>\n'
            ,'</head>\n'
            ,'<body>\n'
            ,'<svg height="420" width=420 xmlns="http://www.w3.org/2000/svg">\n'
            ,'<line x1="0" y1="210" x2="420" y2="210"'
            ,'style="stroke:rgb(0,0,0);stroke-width:2"/>\n'
            ,'<line x1="210" y1="0" x2="210" y2="420"'
            ,'style="stroke:rgb(0,0,0);stroke-width:2"/>\n'])
        for pt in L:
            if isinstance(pt, Number):
                x,y = pt.real, pt.imag
            else:
                if isinstance(pt, tuple) or isinstance(pt, list):
                    x,y = pt
                else:
                    raise ValueError
            h.writelines(['<circle cx="%d" cy="%d" r="%d" fill="red"/>\n'
                          % (origin[0]+scalar*x,origin[1]-scalar*y,dot_size)])
        h.writelines(['</svg>\n</body>\n</html>'])
    if browser is None:
        browser = _browser
    webbrowser.get(browser).open('file://%s' % hpath)

def setbrowser(browser=None):
    """ Registers the given browser and saves it as the module default.
        This is used to control which browser is used to display the plot.
        The argument should be a value that can be passed to webbrowser.get()
        to obtain a browser.  If no argument is given, the default is reset
        to the system default.

        webbrowser provides some predefined browser names, including:
        'firefox'
        'opera'

        If the browser string contains '%s', it is interpreted as a literal
        browser command line.  The URL will be substituted for '%s' in the command.
        For example:
        'google-chrome %s'
        'cmd "start iexplore.exe %s"'

        See the webbrowser documentation for more detailed information.

        Note: Safari does not reliably work with the webbrowser module,
        so we recommend using a different browser.
    """
    global _browser
    if browser is None:
        _browser = None  # Use system default
    else:
        webbrowser.register(browser, None, webbrowser.get(browser))
        _browser = browser

def getbrowser():
    """ Returns the module's default browser """
    return _browser

# Create a temporary file that will be removed at exit
# Returns a path to the file
def create_temp(suffix='', prefix='tmp', dir=None):
    _f, path = tempfile.mkstemp(suffix, prefix, dir)
    os.close(_f)
    remove_at_exit(path)
    return path

# Register a file to be removed at exit
def remove_at_exit(path):
    atexit.register(os.remove, path)
    
    



"""
from plotting import plot

plot({1j * (2+1j)} | {2+1j}, 10)

s = {2+1j, 3+2j.......}

plot(s)

T = {2*z for z in s}

plot(T)

plot(T, 10)

plot(T|s, 10)

t = {2j+z for z in s}

plot{t|s}

s = {2 +2j, 3+2j, 1.75+1j, 2+1j, 2.25 + 1j, 2.5+1j, 2.75 +1j, 3+1j, 3.25+1j}

plot (s)

T = {2*z for z in s}

plot (T|s, 10)

x = {z*e**(pi/4*1j) for z in s} rotate 45

     f = {z*(1/2) for z in s} half points
     
     f = {z*(1/2j) for z in s} rotate 90, scale by half
"""

def transform(L,a,b): return {a*z+b for z in L}

# Define S
S = {2+2j, 3+2j, 1.75+1.15j, 2+1j, 2.25+1j, 2.5+1j, 2.75+1j, 3+1j, 3.25+1.15j}
# Define T
T = {(e**(2*pi*1j/30))**x for x in range(30)}
# Transform S
z = transform(S,.75,(-1.9+-1.15j))
nose = transform(T,0.15,0)
# Plot T with transformed S
plot(z|T|nose)

"""
from image import file2image as f2i
from plotting import plot
data = f2i("./img01.png")
pts = {(x+y*ij) for x in range(len(data)) for y in range(len(data[0])) if data[x][y][0] < 120}
plot(pts, len(data))
"""