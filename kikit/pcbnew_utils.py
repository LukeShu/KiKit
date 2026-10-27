import typing

import pcbnew

KICAD_VERSION = tuple(int(x) for x in pcbnew.GetMajorMinorVersion().split("."))


def _attr(name: str, fallback: str) -> typing.Any:
    """Resolve a pcbnew attribute that was renamed between v9 and v10."""
    v = getattr(pcbnew, name, None)
    if v is not None:
        return v
    return getattr(pcbnew, fallback)


# KiCad 10 shortened the enum names
EDA_UNITS_MM: "pcbnew._EDA_UNITS" = _attr("EDA_UNITS_MM", "EDA_UNITS_MILLIMETRES")
EDA_UNITS_INCH: "pcbnew._EDA_UNITS" = _attr("EDA_UNITS_INCH", "EDA_UNITS_INCHES")
DXF_UNITS_MM: "pcbnew._DXF_UNITS" = _attr("DXF_UNITS_MM", "DXF_UNITS_MILLIMETERS")
DIM_UNITS_MODE_MM: "pcbnew._DIM_UNITS_MODE" = _attr(
    "DIM_UNITS_MODE_MM", "DIM_UNITS_MODE_MILLIMETRES"
)


def duplicateZone(zone: pcbnew.ZONE) -> pcbnew.ZONE:
    """
    Duplicate a zone without adding it to its parent group.

    KiCad 10.0.5 requires the addToParentGroup argument, while KiCad 9 and
    earlier KiCad 10 releases expose only the zero-argument signature.
    """
    try:
        duplicate = zone.Duplicate(False)
    except TypeError:
        return zone.Duplicate()  # type: ignore
    duplicate = duplicate.Cast()
    if typing.TYPE_CHECKING:
        assert isinstance(duplicate, pcbnew.ZONE)
    return duplicate


def resolveItem(board: pcbnew.BOARD, kiid: pcbnew.KIID) -> pcbnew.BOARD_ITEM:
    # KiCad 10 renamed GetItem to ResolveItem and added a mandatory bool arg
    if hasattr(board, "ResolveItem"):
        return board.ResolveItem(kiid, True)
    return board.GetItem(kiid)  # type: ignore


def setDoNotAllowZoneFills(zone: pcbnew.ZONE, value: bool) -> None:
    # KiCad 10 renamed SetDoNotAllowCopperPour
    fn: typing.Callable[[bool], None] = getattr(
        zone, "SetDoNotAllowZoneFills", None
    ) or getattr(zone, "SetDoNotAllowCopperPour")
    fn(value)


def getItemDescription(
    item: pcbnew.EDA_ITEM, units: typing.Optional["pcbnew._EDA_UNITS"] = None
) -> str:
    if units is None:
        units = EDA_UNITS_MM
    uProvider = pcbnew.UNITS_PROVIDER(pcbnew.pcbIUScale, units)
    return item.GetItemDescription(uProvider, True)


def increaseZonePriorities(board: pcbnew.BOARD, amount: int = 1) -> None:
    for zone in board.Zones():
        zone.SetAssignedPriority(zone.GetAssignedPriority() + amount)
