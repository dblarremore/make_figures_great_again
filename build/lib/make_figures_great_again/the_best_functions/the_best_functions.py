# coding: utf-8
"""
Thanks to palettable. https://jiffyclub.github.io/palettable/
"""
from __future__ import absolute_import, print_function

def make_figure_great_again(ax):
    # Strengthen the borders
    print 'Strengthening the borders...'
    for spine_name in ax.spines:
        spine = ax.spines[spine_name]
        current_width = spine.get_linewidth()
        spine.set_linewidth(5*current_width)
