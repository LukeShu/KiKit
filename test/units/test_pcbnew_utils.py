import importlib

import pcbnew
import pytest

import kikit
from kikit.pcbnew_utils import duplicateZone


def testMissingSwigIteratorNext(monkeypatch: pytest.MonkeyPatch) -> None:
    board = pcbnew.BOARD()
    board.Add(pcbnew.PCB_SHAPE(board))
    monkeypatch.delattr(pcbnew.SwigPyIterator, "next")

    importlib.reload(kikit)

    assert len(board.GetDrawings()) == 1


def testDuplicateZoneUsesNewSignature() -> None:
    duplicate = object()

    class BoardItem:
        def Cast(self) -> object:
            return duplicate

    class Zone:
        def Duplicate(self, addToParentGroup: bool) -> BoardItem:
            assert addToParentGroup is False
            return BoardItem()

    assert duplicateZone(Zone()) is duplicate  # type: ignore


def testDuplicateZoneFallsBackToOldSignature() -> None:
    duplicate = object()

    class Zone:
        def Duplicate(self) -> object:
            return duplicate

    assert duplicateZone(Zone()) is duplicate  # type: ignore


def testDuplicateZoneCanBeAddedToZoneContainer() -> None:
    board = pcbnew.BOARD()
    zone = pcbnew.ZONE(board)
    zones = pcbnew.ZONES()

    zones.append(duplicateZone(zone))

    assert len(zones) == 1
