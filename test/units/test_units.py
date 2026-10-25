from copy import deepcopy

import pytest
from pcbnew import FromMils, FromMM

from kikit.units import UnitError, readAngle, readLength


def test_readLength() -> None:
    assert readLength("4.24mm") == FromMM(4.24)
    assert readLength("4.24 mm") == FromMM(4.24)
    assert readLength("4mm") == FromMM(4)

    assert readLength("1m") == FromMM(1000)
    assert readLength("1cm") == FromMM(10)

    assert readLength("1mil") == FromMils(1)
    assert readLength("1inch") == FromMils(1000)


def test_baseValue_deepcopy() -> None:
    a = readLength("1.23mm")
    b = deepcopy(a)

    assert a.__dict__ == b.__dict__
