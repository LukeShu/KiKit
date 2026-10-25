from kikit.common import toKiCADPoint
from kikit.units import mm


def kikitPostprocess(panel, arg):
    minx, miny, maxx, maxy = panel.panelBBox()
    position = toKiCADPoint(((minx + maxx) // 2, miny + 2 * mm))
    panel.addNPTHole(position, 3 * mm)
