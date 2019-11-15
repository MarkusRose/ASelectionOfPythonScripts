import numpy as np
import matplotlib.pyplot as plt
from cycler import cycler


xr = (np.arange(100)-49.5)/10.

'''
def setAxLinesBW(ax):
    """
    Take each Line2D in the axes, ax, and convert the line style to be 
    suitable for black and white viewing.
    """
    MARKERSIZE = 3

    COLORMAP = {
        'b': {'marker': None, 'dash': (None,None)},
        'g': {'marker': None, 'dash': [5,5]},
        'r': {'marker': None, 'dash': [5,3,1,3]},
        'c': {'marker': None, 'dash': [1,3]},
        'm': {'marker': None, 'dash': [5,2,5,2,5,10]},
        'y': {'marker': None, 'dash': [5,3,1,2,1,10]},
        'k': {'marker': 'o', 'dash': (None,None)} #[1,2,1,10]}
        }


    lines_to_adjust = ax.get_lines()
    try:
        lines_to_adjust += ax.get_legend().get_lines()
    except AttributeError:
        pass

    for line in lines_to_adjust:
        origColor = line.get_color()
        line.set_color('black')
        line.set_dashes(COLORMAP[origColor]['dash'])
        line.set_marker(COLORMAP[origColor]['marker'])
        line.set_markersize(MARKERSIZE)

def setFigLinesBW(fig):
    """
    Take each axes in the figure, and for each line in the axes, make the
    line viewable in black and white.
    """
    for ax in fig.get_axes():
        setAxLinesBW(ax)

'''

monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
                      cycler('linestyle', ['-', '--', ':', '-.']))

plt.rc('axes', prop_cycle=monochrome)


plt.plot(xr,np.sin(xr),label='sine')
plt.plot(xr,np.cos(xr),label='cosine')
plt.plot(xr,np.exp(-1)*np.exp(xr/(5.)),label='exponential')
plt.plot(xr,(np.sin(xr)/xr)**2,label='airy disk')
plt.plot(xr,(np.sin(xr)/xr),label='sinc function',markevery=0.1)
plt.legend()
plt.ylim([-1,1])
plt.show()
