# coding: utf-8
"""
Thanks to palettable. https://jiffyclub.github.io/palettable/
"""
from __future__ import absolute_import, print_function

from palettable.palette import Palette

url = 'http://www.trump.com'
palette_type = 'qualitative'

palette_names = [
    'my_hands_are_normal_hands_6',
    'i_love_hispanics_6',
    'neck_6',
    'the_wall_6',
    'this_is_true_6',
    'believe_me_7',
    'just_the_best_really_6',
    'fired_6',
    'orange_5',
]

# Dictionary from name or short name to index.
lookup = dict((name.lower(), i) for i, name in enumerate(palette_names))

colors_rgb = [
    #myhandsarenormalhands
    [[25,19,19],
    [84,83,140],
    [158,76,62],
    [180,112,77],
    [253,179,144],
    [202,122,99]],
    #ilovehispanics
    [[59,64,86],
    [210,123,44],
    [249,196,142],
    [80,15,35],
    [153,79,68],
    [156,141,134]],
    #neck
    [[138,93,64],
    [207,147,111],
    [141,105,53],
    [238,231,205],
    [56,70,107],
    [10,13,30]],
    #thewall
    [[24,22,35],
    [11,26,69],
    [85,114,194],
    [216,157,125],
    [175,90,59],
    [195,177,137]],
    #thisistrue
    [[46,67,94],
    [221,250,246],
    [163,152,132],
    [192,178,90],
    [208,187,196],
    [155,103,107]],
    #believeme
    [[21,16,22],
    [239,210,202],
    [190,41,17],
    [107,55,34],
    [208,122,75],
    [214,138,112],
    [239,175,104]],
    #justthebestreally
    [[22,35,43],
    [216,186,188],
    [206,202,167],
    [209,145,109],
    [179,96,64],
    [119,74,43]],
    #fired
    [[127,150,181],
    [120,85,81],
    [255,169,149],
    [227,87,60],
    [234,159,102],
    [255,230,171]],
    #orange
    [[26,25,30],
    [247,148,29],
    [150,73,1],
    [76,89,82],
    [229,83,0]],
]


class TerrificMap(Palette):
    """
    Representation of a color map with matplotlib compatible
    views of the map.

    Parameters
    ----------
    name : str
    colors : list
        Colors as list of 0-255 RGB triplets.

    Attributes
    ----------
    name : str
    type : str
    number : int
        Number of colors in color map.
    colors : list
        Colors as list of 0-255 RGB triplets.
    hex_colors : list
    mpl_colors : list
    mpl_colormap : matplotlib LinearSegmentedColormap

    """
    url = url

    def __init__(self, name, colors):
        super(TerrificMap, self).__init__(name, palette_type, colors)


def print_maps():
    """
    Print a list of Terrific palettes.

    """
    namelen = max(len(name) for name in palette_names)
    fmt = '{0:' + str(namelen + 4) + '}{1:16}{2:}'

    for i, name in enumerate(palette_names):
        print(fmt.format(name, palette_type, len(colors_rgb[i])))


def get_map(name, reverse=False):
    """
    Get a Terrific palette by name.

    Parameters
    ----------
    name : str
        Name of map. Use `print_maps` to see available names. If `None`, then
        return a list of all colormaps.
    reverse : bool, optional
        If True reverse colors from their default order.

    Returns
    -------
    palette : TerrificMap

    """
    try:
        index = lookup[name.lower()]
    except KeyError:
        msg = "{0!r} is an unknown Terrific palette."
        raise KeyError(msg.format(name))

    colors = colors_rgb[index]
    if reverse:
        name = name + '_r'
        colors = list(reversed(colors))

    return TerrificMap(name, colors)


def _get_all_maps():
    """
    Returns a dictionary of all Terrific palettes, including reversed ones.

    """
    d = dict((name, get_map(name)) for name in palette_names)
    d.update(dict(
        (name + '_r', get_map(name, reverse=True)) for name in palette_names))
    return d
