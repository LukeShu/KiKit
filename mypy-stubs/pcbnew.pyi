import typing

import _typeshed

class SwigPyIterator:  # line 58
    next: typing.Callable[[SwigPyIterator], typing.Any]  # missing in 10.0.7
    def __next__(self) -> typing.Any: ...  # line 92

class VECTOR2I: ...  # line 4986
class BOX2I: ...  # line 5363

@typing.type_check_only
class _EDA_ANGLE_T: ...

TENTHS_OF_A_DEGREE_T: typing.Final[_EDA_ANGLE_T] = ...  # line 17343
DEGREES_T: typing.Final[_EDA_ANGLE_T] = ...  # line 17345
RADIANS_T: typing.Final[_EDA_ANGLE_T] = ...  # line 17347

class EDA_ANGLE:  # line 17349
    # __init__  # line 17355
    @typing.overload
    def __init__(self, aValue: float, aAngleType: _EDA_ANGLE_T, /) -> None: ...
    @typing.overload
    def __init__(self, aAngleInDegrees: float, /) -> None: ...
    @typing.overload
    def __init__(self, aVector: _typeshed.Incomplete, /) -> None: ...
    @typing.overload
    def __init__(self, /) -> None: ...
    # value
    def AsDegrees(self) -> float: ...  # line 17364
    def AsTenthsOfADegrees(self) -> int: ...  # line 17368
    def AsRadians(self) -> float: ...  # line 17372
    # arithmetic
    def __mul__(self, other: float) -> EDA_ANGLE: ...  # line 17488
    def __rmul__(self, other: float) -> EDA_ANGLE: ...  # line 17491
