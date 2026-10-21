import collections.abc
import typing

import _typeshed

_SWIGPY_SLICEOBJECT = slice[typing.SupportsIndex | None]

class SwigPyIterator:  # line 58
    next: typing.Callable[[SwigPyIterator], typing.Any]  # missing in 10.0.7
    def __next__(self) -> typing.Any: ...  # line 92
    def __iter__(self) -> typing.Self: ...  # line 130

@typing.type_check_only
class _SwigPyIterator[T]:  # line 58
    def next(self) -> T: ...  # missing in 10.0.7
    def __next__(self) -> T: ...  # line 92
    def __iter__(self) -> typing.Self: ...  # line 130

class wxSize: ...  # line 548

class wxPoint:  # line 603
    def __getitem__(self, index: int) -> int: ...  # line 640

class EDA_ITEM:  # line 1386
    def GetBoundingBox(self) -> BOX2I: ...  # line 1564
    def GetPosition(self) -> VECTOR2I: ...  # line 1568

class EDA_TEXT: ...  # line 2532

@typing.type_check_only
class _PCB_LAYER_ID(int): ...

UNDEFINED_LAYER: typing.Final[_PCB_LAYER_ID] = ...  # line 3009
UNSELECTED_LAYER: typing.Final[_PCB_LAYER_ID] = ...  # line 3011
F_Cu: typing.Final[_PCB_LAYER_ID] = ...  # line 3013
B_Cu: typing.Final[_PCB_LAYER_ID] = ...  # line 3015
In1_Cu: typing.Final[_PCB_LAYER_ID] = ...  # line 3017
In2_Cu: typing.Final[_PCB_LAYER_ID] = ...  # line 3019
In3_Cu: typing.Final[_PCB_LAYER_ID] = ...  # line 3021
In4_Cu: typing.Final[_PCB_LAYER_ID] = ...  # line 3023
In5_Cu: typing.Final[_PCB_LAYER_ID] = ...  # line 3025
In6_Cu: typing.Final[_PCB_LAYER_ID] = ...  # line 3027
In7_Cu: typing.Final[_PCB_LAYER_ID] = ...  # line 3029
In8_Cu: typing.Final[_PCB_LAYER_ID] = ...  # line 3031
In9_Cu: typing.Final[_PCB_LAYER_ID] = ...  # line 3033
In10_Cu: typing.Final[_PCB_LAYER_ID] = ...  # line 3035
In11_Cu: typing.Final[_PCB_LAYER_ID] = ...  # line 3037
In12_Cu: typing.Final[_PCB_LAYER_ID] = ...  # line 3039
In13_Cu: typing.Final[_PCB_LAYER_ID] = ...  # line 3041
In14_Cu: typing.Final[_PCB_LAYER_ID] = ...  # line 3043
In15_Cu: typing.Final[_PCB_LAYER_ID] = ...  # line 3045
In16_Cu: typing.Final[_PCB_LAYER_ID] = ...  # line 3047
In17_Cu: typing.Final[_PCB_LAYER_ID] = ...  # line 3049
In18_Cu: typing.Final[_PCB_LAYER_ID] = ...  # line 3051
In19_Cu: typing.Final[_PCB_LAYER_ID] = ...  # line 3053
In20_Cu: typing.Final[_PCB_LAYER_ID] = ...  # line 3055
In21_Cu: typing.Final[_PCB_LAYER_ID] = ...  # line 3057
In22_Cu: typing.Final[_PCB_LAYER_ID] = ...  # line 3059
In23_Cu: typing.Final[_PCB_LAYER_ID] = ...  # line 3061
In24_Cu: typing.Final[_PCB_LAYER_ID] = ...  # line 3063
In25_Cu: typing.Final[_PCB_LAYER_ID] = ...  # line 3065
In26_Cu: typing.Final[_PCB_LAYER_ID] = ...  # line 3067
In27_Cu: typing.Final[_PCB_LAYER_ID] = ...  # line 3069
In28_Cu: typing.Final[_PCB_LAYER_ID] = ...  # line 3071
In29_Cu: typing.Final[_PCB_LAYER_ID] = ...  # line 3073
In30_Cu: typing.Final[_PCB_LAYER_ID] = ...  # line 3075
F_Mask: typing.Final[_PCB_LAYER_ID] = ...  # line 3077
B_Mask: typing.Final[_PCB_LAYER_ID] = ...  # line 3079
F_SilkS: typing.Final[_PCB_LAYER_ID] = ...  # line 3081
B_SilkS: typing.Final[_PCB_LAYER_ID] = ...  # line 3083
F_Adhes: typing.Final[_PCB_LAYER_ID] = ...  # line 3085
B_Adhes: typing.Final[_PCB_LAYER_ID] = ...  # line 3087
F_Paste: typing.Final[_PCB_LAYER_ID] = ...  # line 3089
B_Paste: typing.Final[_PCB_LAYER_ID] = ...  # line 3091
Dwgs_User: typing.Final[_PCB_LAYER_ID] = ...  # line 3093
Cmts_User: typing.Final[_PCB_LAYER_ID] = ...  # line 3095
Eco1_User: typing.Final[_PCB_LAYER_ID] = ...  # line 3097
Eco2_User: typing.Final[_PCB_LAYER_ID] = ...  # line 3099
Edge_Cuts: typing.Final[_PCB_LAYER_ID] = ...  # line 3101
Margin: typing.Final[_PCB_LAYER_ID] = ...  # line 3103
B_CrtYd: typing.Final[_PCB_LAYER_ID] = ...  # line 3105
F_CrtYd: typing.Final[_PCB_LAYER_ID] = ...  # line 3107
B_Fab: typing.Final[_PCB_LAYER_ID] = ...  # line 3109
F_Fab: typing.Final[_PCB_LAYER_ID] = ...  # line 3111
Rescue: typing.Final[_PCB_LAYER_ID] = ...  # line 3113
User_1: typing.Final[_PCB_LAYER_ID] = ...  # line 3115
User_2: typing.Final[_PCB_LAYER_ID] = ...  # line 3117
User_3: typing.Final[_PCB_LAYER_ID] = ...  # line 3119
User_4: typing.Final[_PCB_LAYER_ID] = ...  # line 3121
User_5: typing.Final[_PCB_LAYER_ID] = ...  # line 3123
User_6: typing.Final[_PCB_LAYER_ID] = ...  # line 3125
User_7: typing.Final[_PCB_LAYER_ID] = ...  # line 3127
User_8: typing.Final[_PCB_LAYER_ID] = ...  # line 3129
User_9: typing.Final[_PCB_LAYER_ID] = ...  # line 3131
User_10: typing.Final[_PCB_LAYER_ID] = ...  # line 3133
User_11: typing.Final[_PCB_LAYER_ID] = ...  # line 3135
User_12: typing.Final[_PCB_LAYER_ID] = ...  # line 3137
User_13: typing.Final[_PCB_LAYER_ID] = ...  # line 3139
User_14: typing.Final[_PCB_LAYER_ID] = ...  # line 3141
User_15: typing.Final[_PCB_LAYER_ID] = ...  # line 3143
User_16: typing.Final[_PCB_LAYER_ID] = ...  # line 3145
User_17: typing.Final[_PCB_LAYER_ID] = ...  # line 3147
User_18: typing.Final[_PCB_LAYER_ID] = ...  # line 3149
User_19: typing.Final[_PCB_LAYER_ID] = ...  # line 3151
User_20: typing.Final[_PCB_LAYER_ID] = ...  # line 3153
User_21: typing.Final[_PCB_LAYER_ID] = ...  # line 3155
User_22: typing.Final[_PCB_LAYER_ID] = ...  # line 3157
User_23: typing.Final[_PCB_LAYER_ID] = ...  # line 3159
User_24: typing.Final[_PCB_LAYER_ID] = ...  # line 3161
User_25: typing.Final[_PCB_LAYER_ID] = ...  # line 3163
User_26: typing.Final[_PCB_LAYER_ID] = ...  # line 3165
User_27: typing.Final[_PCB_LAYER_ID] = ...  # line 3167
User_28: typing.Final[_PCB_LAYER_ID] = ...  # line 3169
User_29: typing.Final[_PCB_LAYER_ID] = ...  # line 3171
User_30: typing.Final[_PCB_LAYER_ID] = ...  # line 3173
User_31: typing.Final[_PCB_LAYER_ID] = ...  # line 3175
User_32: typing.Final[_PCB_LAYER_ID] = ...  # line 3177
User_33: typing.Final[_PCB_LAYER_ID] = ...  # line 3179
User_34: typing.Final[_PCB_LAYER_ID] = ...  # line 3181
User_35: typing.Final[_PCB_LAYER_ID] = ...  # line 3183
User_36: typing.Final[_PCB_LAYER_ID] = ...  # line 3185
User_37: typing.Final[_PCB_LAYER_ID] = ...  # line 3187
User_38: typing.Final[_PCB_LAYER_ID] = ...  # line 3189
User_39: typing.Final[_PCB_LAYER_ID] = ...  # line 3191
User_40: typing.Final[_PCB_LAYER_ID] = ...  # line 3193
User_41: typing.Final[_PCB_LAYER_ID] = ...  # line 3195
User_42: typing.Final[_PCB_LAYER_ID] = ...  # line 3197
User_43: typing.Final[_PCB_LAYER_ID] = ...  # line 3199
User_44: typing.Final[_PCB_LAYER_ID] = ...  # line 3201
User_45: typing.Final[_PCB_LAYER_ID] = ...  # line 3203
PCB_LAYER_ID_COUNT: typing.Final[_PCB_LAYER_ID] = ...  # line 3205

class VECTOR2I:  # line 4986
    # __init__  # line 4994
    @typing.overload
    def __init__(self, /) -> None: ...
    @typing.overload
    def __init__(self, x: int, y: int, /) -> None: ...
    @typing.overload
    def __init__(self, aVec: VECTOR2I, /) -> None: ...
    # index
    def __getitem__(self, index: int) -> int: ...  # line 5105

class VECTOR2L: ...  # line 5122

class BOX2I:  # line 5363
    def GetX(self) -> int: ...  # line 5407
    def GetY(self) -> int: ...  # line 5411
    def GetWidth(self) -> int: ...  # line 5427
    def GetHeight(self) -> int: ...  # line 5431
    # __init__  # line 5602
    @typing.overload
    def __init__(self, /) -> None: ...
    @typing.overload
    def __init__(self, aPos: VECTOR2I, aSize: VECTOR2L = ..., /) -> None: ...
    @typing.overload
    def __init__(self, aPos: VECTOR2I, aSize: VECTOR2I, /) -> None: ...

class SHAPE_BASE: ...  # line 5964
class SHAPE(SHAPE_BASE): ...  # line 5997
class SHAPE_LINE_CHAIN_BASE(SHAPE): ...  # line 6119

class SHAPE_LINE_CHAIN(SHAPE_LINE_CHAIN_BASE):  # line 6461
    def PointCount(self) -> int: ...  # line 6535
    def CPoint(self, aIndex: int) -> VECTOR2I: ...  # line 6555

class SHAPE_POLY_SET(SHAPE):  # line 6774
    def OutlineCount(self) -> int: ...  # line 6888
    def Outline(self, aIntex: int, /) -> SHAPE_LINE_CHAIN: ...  # line 6904

class BOARD_ITEM(EDA_ITEM):  # line 10252
    def GetLayer(self) -> _PCB_LAYER_ID: ...  # line 10378

class BOARD_ITEM_CONTAINER(BOARD_ITEM):  # line 11095
    def Remove(self, item: BOARD_ITEM) -> None: ...  # line 11126

class BOARD_CONNECTED_ITEM(BOARD_ITEM): ...  # line 11150

class DRAWINGS:  # line 13419
    def iterator(self) -> _SwigPyIterator[BOARD_ITEM]: ...  # line 13425
    def __bool__(self) -> bool: ...  # line 13431
    def __len__(self) -> int: ...  # line 13435
    # __delitem__  # line 13439
    @typing.overload
    def __delitem__(self, i: int, /) -> None: ...
    @typing.overload
    def __delitem__(self, slice: _SWIGPY_SLICEOBJECT, /) -> None: ...
    # __getitem__  # line 13446
    @typing.overload
    def __getitem__(self, i: int, /) -> BOARD_ITEM: ...
    @typing.overload
    def __getitem__(self, slice: _SWIGPY_SLICEOBJECT, /) -> DRAWINGS: ...
    @typing.overload
    # __getitem__  # line 13453
    def __setitem__(self, slice: _SWIGPY_SLICEOBJECT, v: DRAWINGS, /) -> None: ...
    @typing.overload
    def __setitem__(self, slice: _SWIGPY_SLICEOBJECT, /) -> None: ...
    @typing.overload
    def __setitem__(self, i: int, x: BOARD_ITEM, /) -> None: ...
    def __iter__(self) -> collections.abc.Iterator[BOARD_ITEM]: ...  # line 13563

class ZONE(BOARD_CONNECTED_ITEM):  # line 16467
    def Outline(self) -> SHAPE_POLY_SET: ...  # line 16712

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

class EDA_SHAPE:  # line 17585
    def SetWidth(self, aWidth: int) -> None: ...  # line 17695
    def GetWidth(self) -> int: ...  # line 17699

class PCB_SHAPE(BOARD_CONNECTED_ITEM, EDA_SHAPE): ...  # line 18000
class PCB_TEXT(BOARD_ITEM, EDA_TEXT): ...  # line 18108
class PCB_DIMENSION_BASE(PCB_TEXT): ...  # line 18690

class BOARD(BOARD_ITEM_CONTAINER):  # line 21424
    def GetFootprints(self) -> list[FOOTPRINT]: ...  # line 22253
    def GetDrawings(self) -> list[BOARD_ITEM]: ...  # line 22254

class FOOTPRINT(BOARD_ITEM_CONTAINER):  # line 22599
    def GraphicalItems(self) -> DRAWINGS: ...  # line 22681
    def GetReference(self) -> str: ...  # line 23066
    def GetBoundingBox(
        self, aIncludeText: bool = ..., includeHiddenText: bool = ..., /
    ) -> BOX2I: ...  # line 23478

# ToMM  # line 23790
@typing.overload
def ToMM(iu: int | float) -> float: ...
@typing.overload
def ToMM(
    mm: wxPoint | wxSize | VECTOR2I | VECTOR2L,
) -> collections.abc.Sequence[float]: ...

# FromMM  # line 23798
@typing.overload
def FromMM(mm: int | float) -> int: ...
@typing.overload
def FromMM(
    mm: wxPoint | wxSize | VECTOR2I | VECTOR2L,
) -> collections.abc.Sequence[int]: ...

# FromMils  # line 23814
@typing.overload
def FromMils(mils: int | float) -> int: ...
@typing.overload
def FromMils(
    mils: wxPoint | wxSize | VECTOR2I | VECTOR2L,
) -> collections.abc.Sequence[int]: ...
