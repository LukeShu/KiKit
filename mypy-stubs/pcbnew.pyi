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

class KIID: ...  # line 821

@typing.type_check_only
class _KICAD_T: ...

NOT_USED: typing.Final[_KICAD_T] = ...  # line 1126
TYPE_NOT_INIT: typing.Final[_KICAD_T] = ...  # line 1128
PCB_T: typing.Final[_KICAD_T] = ...  # line 1130
SCREEN_T: typing.Final[_KICAD_T] = ...  # line 1132
PCB_FOOTPRINT_T: typing.Final[_KICAD_T] = ...  # line 1134
PCB_PAD_T: typing.Final[_KICAD_T] = ...  # line 1136
PCB_SHAPE_T: typing.Final[_KICAD_T] = ...  # line 1138
PCB_REFERENCE_IMAGE_T: typing.Final[_KICAD_T] = ...  # line 1140
PCB_FIELD_T: typing.Final[_KICAD_T] = ...  # line 1142
PCB_GENERATOR_T: typing.Final[_KICAD_T] = ...  # line 1144
PCB_TEXT_T: typing.Final[_KICAD_T] = ...  # line 1146
PCB_TEXTBOX_T: typing.Final[_KICAD_T] = ...  # line 1148
PCB_TABLE_T: typing.Final[_KICAD_T] = ...  # line 1150
PCB_TABLECELL_T: typing.Final[_KICAD_T] = ...  # line 1152
PCB_TRACE_T: typing.Final[_KICAD_T] = ...  # line 1154
PCB_VIA_T: typing.Final[_KICAD_T] = ...  # line 1156
PCB_ARC_T: typing.Final[_KICAD_T] = ...  # line 1158
PCB_MARKER_T: typing.Final[_KICAD_T] = ...  # line 1160
PCB_DIMENSION_T: typing.Final[_KICAD_T] = ...  # line 1162
PCB_BARCODE_T: typing.Final[_KICAD_T] = ...  # line 1164
PCB_DIM_ALIGNED_T: typing.Final[_KICAD_T] = ...  # line 1166
PCB_DIM_LEADER_T: typing.Final[_KICAD_T] = ...  # line 1168
PCB_DIM_CENTER_T: typing.Final[_KICAD_T] = ...  # line 1170
PCB_DIM_RADIAL_T: typing.Final[_KICAD_T] = ...  # line 1172
PCB_DIM_ORTHOGONAL_T: typing.Final[_KICAD_T] = ...  # line 1174
PCB_TARGET_T: typing.Final[_KICAD_T] = ...  # line 1176
PCB_ZONE_T: typing.Final[_KICAD_T] = ...  # line 1178
PCB_ITEM_LIST_T: typing.Final[_KICAD_T] = ...  # line 1180
PCB_NETINFO_T: typing.Final[_KICAD_T] = ...  # line 1182
PCB_GROUP_T: typing.Final[_KICAD_T] = ...  # line 1184
PCB_BOARD_OUTLINE_T: typing.Final[_KICAD_T] = ...  # line 1186
PCB_POINT_T: typing.Final[_KICAD_T] = ...  # line 1188
PCB_FIELD_LOCATE_REFERENCE_T: typing.Final[_KICAD_T] = ...  # line 1190
PCB_FIELD_LOCATE_VALUE_T: typing.Final[_KICAD_T] = ...  # line 1192
PCB_FIELD_LOCATE_FOOTPRINT_T: typing.Final[_KICAD_T] = ...  # line 1194
PCB_FIELD_LOCATE_DATASHEET_T: typing.Final[_KICAD_T] = ...  # line 1196
PCB_LOCATE_STDVIA_T: typing.Final[_KICAD_T] = ...  # line 1198
PCB_LOCATE_UVIA_T: typing.Final[_KICAD_T] = ...  # line 1200
PCB_LOCATE_BLINDVIA_T: typing.Final[_KICAD_T] = ...  # line 1202
PCB_LOCATE_BURIEDVIA_T: typing.Final[_KICAD_T] = ...  # line 1204
PCB_LOCATE_TEXT_T: typing.Final[_KICAD_T] = ...  # line 1206
PCB_LOCATE_HOLE_T: typing.Final[_KICAD_T] = ...  # line 1208
PCB_LOCATE_PTH_T: typing.Final[_KICAD_T] = ...  # line 1210
PCB_LOCATE_NPTH_T: typing.Final[_KICAD_T] = ...  # line 1212
PCB_LOCATE_BOARD_EDGE_T: typing.Final[_KICAD_T] = ...  # line 1214
PCB_SHAPE_LOCATE_SEGMENT_T: typing.Final[_KICAD_T] = ...  # line 1216
PCB_SHAPE_LOCATE_RECT_T: typing.Final[_KICAD_T] = ...  # line 1218
PCB_SHAPE_LOCATE_CIRCLE_T: typing.Final[_KICAD_T] = ...  # line 1220
PCB_SHAPE_LOCATE_ARC_T: typing.Final[_KICAD_T] = ...  # line 1222
PCB_SHAPE_LOCATE_POLY_T: typing.Final[_KICAD_T] = ...  # line 1224
PCB_SHAPE_LOCATE_BEZIER_T: typing.Final[_KICAD_T] = ...  # line 1226
LIB_SYMBOL_T: typing.Final[_KICAD_T] = ...  # line 1228
SCH_SHAPE_T: typing.Final[_KICAD_T] = ...  # line 1230
SCH_FIELD_T: typing.Final[_KICAD_T] = ...  # line 1232
SCH_TEXT_T: typing.Final[_KICAD_T] = ...  # line 1234
SCH_TEXTBOX_T: typing.Final[_KICAD_T] = ...  # line 1236
SCH_PIN_T: typing.Final[_KICAD_T] = ...  # line 1238
SCH_MARKER_T: typing.Final[_KICAD_T] = ...  # line 1240
SCH_JUNCTION_T: typing.Final[_KICAD_T] = ...  # line 1242
SCH_NO_CONNECT_T: typing.Final[_KICAD_T] = ...  # line 1244
SCH_BUS_WIRE_ENTRY_T: typing.Final[_KICAD_T] = ...  # line 1246
SCH_BUS_BUS_ENTRY_T: typing.Final[_KICAD_T] = ...  # line 1248
SCH_LINE_T: typing.Final[_KICAD_T] = ...  # line 1250
SCH_BITMAP_T: typing.Final[_KICAD_T] = ...  # line 1252
SCH_TABLE_T: typing.Final[_KICAD_T] = ...  # line 1254
SCH_TABLECELL_T: typing.Final[_KICAD_T] = ...  # line 1256
SCH_LABEL_T: typing.Final[_KICAD_T] = ...  # line 1258
SCH_GLOBAL_LABEL_T: typing.Final[_KICAD_T] = ...  # line 1260
SCH_HIER_LABEL_T: typing.Final[_KICAD_T] = ...  # line 1262
SCH_RULE_AREA_T: typing.Final[_KICAD_T] = ...  # line 1264
SCH_DIRECTIVE_LABEL_T: typing.Final[_KICAD_T] = ...  # line 1266
SCH_SYMBOL_T: typing.Final[_KICAD_T] = ...  # line 1268
SCH_GROUP_T: typing.Final[_KICAD_T] = ...  # line 1270
SCH_SHEET_PIN_T: typing.Final[_KICAD_T] = ...  # line 1272
SCH_SHEET_T: typing.Final[_KICAD_T] = ...  # line 1274
SCH_FIELD_LOCATE_REFERENCE_T: typing.Final[_KICAD_T] = ...  # line 1276
SCH_FIELD_LOCATE_VALUE_T: typing.Final[_KICAD_T] = ...  # line 1278
SCH_FIELD_LOCATE_FOOTPRINT_T: typing.Final[_KICAD_T] = ...  # line 1280
SCH_FIELD_LOCATE_DATASHEET_T: typing.Final[_KICAD_T] = ...  # line 1282
SCH_ITEM_LOCATE_WIRE_T: typing.Final[_KICAD_T] = ...  # line 1284
SCH_ITEM_LOCATE_BUS_T: typing.Final[_KICAD_T] = ...  # line 1286
SCH_ITEM_LOCATE_GRAPHIC_LINE_T: typing.Final[_KICAD_T] = ...  # line 1288
SCH_LABEL_LOCATE_ANY_T: typing.Final[_KICAD_T] = ...  # line 1290
SCH_LABEL_LOCATE_WIRE_T: typing.Final[_KICAD_T] = ...  # line 1292
SCH_LABEL_LOCATE_BUS_T: typing.Final[_KICAD_T] = ...  # line 1294
SCH_SYMBOL_LOCATE_POWER_T: typing.Final[_KICAD_T] = ...  # line 1296
SCH_LOCATE_ANY_T: typing.Final[_KICAD_T] = ...  # line 1298
SCH_SCREEN_T: typing.Final[_KICAD_T] = ...  # line 1300
SCHEMATIC_T: typing.Final[_KICAD_T] = ...  # line 1302
GERBER_LAYOUT_T: typing.Final[_KICAD_T] = ...  # line 1304
GERBER_DRAW_ITEM_T: typing.Final[_KICAD_T] = ...  # line 1306
GERBER_IMAGE_T: typing.Final[_KICAD_T] = ...  # line 1308
WSG_LINE_T: typing.Final[_KICAD_T] = ...  # line 1310
WSG_RECT_T: typing.Final[_KICAD_T] = ...  # line 1312
WSG_POLY_T: typing.Final[_KICAD_T] = ...  # line 1314
WSG_TEXT_T: typing.Final[_KICAD_T] = ...  # line 1316
WSG_BITMAP_T: typing.Final[_KICAD_T] = ...  # line 1318
WSG_PAGE_T: typing.Final[_KICAD_T] = ...  # line 1320
WS_PROXY_UNDO_ITEM_T: typing.Final[_KICAD_T] = ...  # line 1322
WS_PROXY_UNDO_ITEM_PLUS_T: typing.Final[_KICAD_T] = ...  # line 1324
SYMBOL_LIB_TABLE_T: typing.Final[_KICAD_T] = ...  # line 1326
FP_LIB_TABLE_T: typing.Final[_KICAD_T] = ...  # line 1328
DESIGN_BLOCK_LIB_TABLE_T: typing.Final[_KICAD_T] = ...  # line 1330
SYMBOL_LIBS_T: typing.Final[_KICAD_T] = ...  # line 1332
SEARCH_STACK_T: typing.Final[_KICAD_T] = ...  # line 1334
S3D_CACHE_T: typing.Final[_KICAD_T] = ...  # line 1336
MAX_STRUCT_TYPE_ID: typing.Final[_KICAD_T] = ...  # line 1338

class EDA_ITEM:  # line 1386
    def GetBoundingBox(self) -> BOX2I: ...  # line 1564
    def GetPosition(self) -> VECTOR2I: ...  # line 1568
    def GetItemDescription(
        self, aUnitsProvider: UNITS_PROVIDER, aFull: bool
    ) -> str: ...  # line 1596

class EDA_IU_SCALE: ...  # line 1680

@typing.type_check_only
class _EDA_UNITS: ...

EDA_UNITS_INCH: typing.Final[_EDA_UNITS] = ...  # line 1731
EDA_UNITS_MM: typing.Final[_EDA_UNITS] = ...  # line 1733
EDA_UNITS_UNSCALED: typing.Final[_EDA_UNITS] = ...  # line 1735
EDA_UNITS_DEGREES: typing.Final[_EDA_UNITS] = ...  # line 1737
EDA_UNITS_PERCENT: typing.Final[_EDA_UNITS] = ...  # line 1739
EDA_UNITS_MILS: typing.Final[_EDA_UNITS] = ...  # line 1741
EDA_UNITS_UM: typing.Final[_EDA_UNITS] = ...  # line 1743
EDA_UNITS_CM: typing.Final[_EDA_UNITS] = ...  # line 1745
EDA_UNITS_FS: typing.Final[_EDA_UNITS] = ...  # line 1747
EDA_UNITS_PS: typing.Final[_EDA_UNITS] = ...  # line 1749
EDA_UNITS_PS_PER_INCH: typing.Final[_EDA_UNITS] = ...  # line 1751
EDA_UNITS_PS_PER_CM: typing.Final[_EDA_UNITS] = ...  # line 1753
EDA_UNITS_PS_PER_MM: typing.Final[_EDA_UNITS] = ...  # line 1755

gerbIUScale: typing.Final[EDA_IU_SCALE] = ...  # line 1937
pcbIUScale: typing.Final[EDA_IU_SCALE] = ...  # line 1938
drawSheetIUScale: typing.Final[EDA_IU_SCALE] = ...  # line 1939
schIUScale: typing.Final[EDA_IU_SCALE] = ...  # line 1940
unityIUScale: typing.Final[EDA_IU_SCALE] = ...  # line 1941

class EDA_TEXT:  # line 2532
    def GetText(self) -> str: ...  # line 2560

def GetMajorMinorVersion() -> str: ...  # line 2974
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

class SHAPE(SHAPE_BASE):  # line 5997
    def Cast(
        self,
    ) -> (
        SHAPE_ARC
        | SHAPE_CIRCLE
        | SHAPE_COMPOUND
        | SHAPE_LINE_CHAIN
        | SHAPE_POLY_SET
        | SHAPE_RECT
        | SHAPE_SEGMENT
        | SHAPE_SIMPLE
    ): ...  # line 6094

class SHAPE_LINE_CHAIN_BASE(SHAPE): ...  # line 6119
class SHAPE_ARC(SHAPE): ...  # line 6178
class SHAPE_CIRCLE(SHAPE): ...  # line 6314
class SHAPE_COMPOUND(SHAPE): ...  # line 6368

class SHAPE_LINE_CHAIN(SHAPE_LINE_CHAIN_BASE):  # line 6461
    def PointCount(self) -> int: ...  # line 6535
    def CPoint(self, aIndex: int) -> VECTOR2I: ...  # line 6555

class SHAPE_POLY_SET(SHAPE):  # line 6774
    def OutlineCount(self) -> int: ...  # line 6888
    def Outline(self, aIntex: int, /) -> SHAPE_LINE_CHAIN: ...  # line 6904

class SHAPE_RECT(SHAPE): ...  # line 7244
class SHAPE_SEGMENT(SHAPE): ...  # line 7328
class SHAPE_SIMPLE(SHAPE_LINE_CHAIN_BASE): ...  # line 7394
class UTF8: ...  # line 7652

class LIB_ID:  # line 7778
    def GetLibNickname(self) -> UTF8: ...  # line 7795
    def GetLibItemName(self) -> UTF8: ...  # line 7807

@typing.type_check_only
class _DXF_UNITS: ...

DXF_UNITS_INCH: typing.Final[_DXF_UNITS] = ...  # line 8789
DXF_UNITS_MM: typing.Final[_DXF_UNITS] = ...  # line 8791

class BOARD_ITEM(EDA_ITEM):  # line 10252
    def GetLayer(self) -> _PCB_LAYER_ID: ...  # line 10378
    # # @typing.overload
    # # def Duplicate(
    # #     self, addToParentGroup: bool, aCommit: _typeshed.Incomplete | None = None
    # # ) -> BOARD_ITEM: ...  # line 10410
    def Cast(
        self,
    ) -> (
        PCB_TEXT
        | PCB_TEXTBOX
        | BOARD
        | PCB_DIM_ALIGNED
        | PCB_DIM_LEADER
        | PCB_DIM_CENTER
        | PCB_DIM_RADIAL
        | PCB_DIM_ORTHOGONAL
        | PCB_SHAPE
        | FOOTPRINT
        | PCB_GROUP
        | PAD
        | PCB_VIA
        | PCB_TRACK
        | PCB_ARC
        | PCB_TARGET
        | PCB_TABLE
        | PCB_REFERENCE_IMAGE
        | ZONE
        | PCB_BARCODE
    ): ...  # line 10501
    # # @typing.overload
    # def Duplicate(self) -> typing.Self: ...  # line 10551

class UNITS_PROVIDER:  # line 10664
    def __init__(
        self, aIuScale: EDA_IU_SCALE, aUnits: _EDA_UNITS
    ) -> None: ...  # line 10670

class PCB_BARCODE(BOARD_ITEM): ...  # line 10764

class BOARD_ITEM_CONTAINER(BOARD_ITEM):  # line 11095
    def Add(self, item: BOARD_ITEM) -> None: ...  # line 11116
    def Remove(self, item: BOARD_ITEM) -> None: ...  # line 11126

class BOARD_CONNECTED_ITEM(BOARD_ITEM): ...  # line 11150

class ZONES:  # line 12527
    def iterator(self) -> _SwigPyIterator[ZONE]: ...  # line 12533
    def __iter__(self) -> _SwigPyIterator[ZONE]: ...  # line 12536
    def __bool__(self) -> bool: ...  # line 12539
    def __len__(self) -> int: ...  # line 12543
    def append(self, x: ZONE) -> None: ...  # line 12573

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

class PAD(BOARD_CONNECTED_ITEM): ...  # line 14506
class PCB_TRACK(BOARD_CONNECTED_ITEM): ...  # line 15629
class PCB_ARC(PCB_TRACK): ...  # line 15792
class PCB_VIA(PCB_TRACK): ...  # line 15895

class ZONE(BOARD_CONNECTED_ITEM):  # line 16467
    # __init__  # line 16473
    @typing.overload
    def __init__(self, parent: BOARD_ITEM_CONTAINER, /) -> None: ...
    @typing.overload
    def __init__(self, aZone: ZONE, /) -> None: ...
    def SetAssignedPriority(self, aPriority: int) -> None: ...  # line 16502
    def GetAssignedPriority(self) -> int: ...  # line 16506
    def Outline(self) -> SHAPE_POLY_SET: ...  # line 16712
    def Duplicate(
        self, addToParentGroup: bool, aCommit: _typeshed.Incomplete | None = None
    ) -> BOARD_ITEM: ...  # line 16885
    def SetDoNotAllowZoneFills(self, aEnable: bool) -> None: ...  # line 16957

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

@typing.type_check_only
class _SHAPE_T: ...

SHAPE_T_UNDEFINED: typing.Final[_SHAPE_T] = ...  # line 17504
SHAPE_T_SEGMENT: typing.Final[_SHAPE_T] = ...  # line 17506
SHAPE_T_RECTANGLE: typing.Final[_SHAPE_T] = ...  # line 17508
SHAPE_T_ARC: typing.Final[_SHAPE_T] = ...  # line 17510
SHAPE_T_CIRCLE: typing.Final[_SHAPE_T] = ...  # line 17512
SHAPE_T_POLY: typing.Final[_SHAPE_T] = ...  # line 17514
SHAPE_T_BEZIER: typing.Final[_SHAPE_T] = ...  # line 17516

class EDA_SHAPE:  # line 17585
    def SetWidth(self, aWidth: int) -> None: ...  # line 17695
    def GetWidth(self) -> int: ...  # line 17699

class PCB_SHAPE(BOARD_CONNECTED_ITEM, EDA_SHAPE):  # line 18000
    # __init__   # line 18006
    @typing.overload
    def __init__(
        self, aParent: BOARD_ITEM, aItemType: _KICAD_T, aShapeType: _SHAPE_T, /
    ) -> None: ...
    @typing.overload
    def __init__(
        self, aParent: BOARD_ITEM = ..., aShapeType: _SHAPE_T = ..., /
    ) -> None: ...

class PCB_TEXT(BOARD_ITEM, EDA_TEXT): ...  # line 18108
class PCB_TEXTBOX(PCB_SHAPE, EDA_TEXT): ...  # line 18217
class PCB_FIELD(PCB_TEXT): ...  # line 18423

@typing.type_check_only
class _DIM_UNITS_MODE: ...

DIM_UNITS_MODE_INCH: typing.Final[_DIM_UNITS_MODE] = ...  # line 18670
DIM_UNITS_MODE_ILS: typing.Final[_DIM_UNITS_MODE] = ...  # line 18672
DIM_UNITS_MODE_MM: typing.Final[_DIM_UNITS_MODE] = ...  # line 18674
DIM_UNITS_MODE_AUTOMATIC: typing.Final[_DIM_UNITS_MODE] = ...  # line 18676

class PCB_DIMENSION_BASE(PCB_TEXT): ...  # line 18690
class PCB_DIM_ALIGNED(PCB_DIMENSION_BASE): ...  # line 18941
class PCB_DIM_ORTHOGONAL(PCB_DIMENSION_BASE): ...  # line 19011
class PCB_DIM_RADIAL(PCB_DIMENSION_BASE): ...  # line 19053
class PCB_DIM_LEADER(PCB_DIMENSION_BASE): ...  # line 19099
class PCB_DIM_CENTER(PCB_DIMENSION_BASE): ...  # line 19141
class PCB_TARGET(BOARD_ITEM): ...  # line 19234
class PCB_TABLE(BOARD_ITEM_CONTAINER): ...  # line 19305
class EDA_GROUP: ...  # line 20832
class PCB_GROUP(BOARD_ITEM, EDA_GROUP): ...  # line 20895
class PCB_REFERENCE_IMAGE(BOARD_ITEM): ...  # line 20978

class BOARD(BOARD_ITEM_CONTAINER):  # line 21424
    def Zones(self) -> ZONES: ...  # line 21470
    def ResolveItem(
        self, aID: KIID, aAllowNullptrReturn: bool = False
    ) -> BOARD_ITEM: ...  # line 21683
    def GetFootprints(self) -> list[FOOTPRINT]: ...  # line 22253
    def GetDrawings(self) -> list[BOARD_ITEM]: ...  # line 22254

class FOOTPRINT(BOARD_ITEM_CONTAINER):  # line 22599
    def GraphicalItems(self) -> DRAWINGS: ...  # line 22681
    def GetOrientation(self) -> EDA_ANGLE: ...  # line 22724
    def GetFPID(self) -> LIB_ID: ...  # line 22740
    def GetReference(self) -> str: ...  # line 23066
    def Duplicate(
        self, addToParentGroup: bool, aCommit: _typeshed.Incomplete | None = None
    ) -> BOARD_ITEM: ...  # line 23298
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
