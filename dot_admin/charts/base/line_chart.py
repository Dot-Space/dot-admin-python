from fontTools.misc.bezierTools import Intersection

from ..serializer import BaseChartSerializer
from typing import Iterable, Sized
from numbers import Number


class LineChart:
    """
    Линейный график
    """

    _x: Intersection[Iterable[Number], Sized] # Ось абсцисс
    _y: Iterable
    _name: str


    def __init__(self, x: Intersection[Iterable[Number], Sized], y: Iterable=None, name: str=None, x_label: str=None, y_label: str=None):
        self._x = x
        if y is not None:
            self._y = y
        else:
            self._y = range(len(x))
        self._name = name
        self._x_label = x_label
        self._y_label = y_label









