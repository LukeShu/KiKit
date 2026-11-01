from . import _version

__version__ = _version.get_versions()["version"]

import pcbnew

# Work around KiCad's SWIG iterator bug until its generated bindings are fixed:
# https://gitlab.com/kicad/code/kicad/-/work_items/25423
# https://github.com/yaqwsx/KiKit/issues/938
if not hasattr(pcbnew.SwigPyIterator, "next"):
    pcbnew.SwigPyIterator.next = pcbnew.SwigPyIterator.__next__  # type: ignore[method-assign]


# Work around SWIG's broken refcounting when transfering ownership (as
# of SWIG v4.5.1).  By not setting `item.thisown=1` we'll cause memory
# leaks, but will avoid prematurely de-initializing the _pcbnew
# capsule, which would cause crashes.
#
# (Also, I'm confused about IsActionRunning() being part of the
# decision.)
if True:

    def _board_item_container_Remove(
        self: pcbnew.BOARD_ITEM_CONTAINER, item: pcbnew.BOARD_ITEM
    ) -> None:
        self.RemoveNative(item)
        if not pcbnew.IsActionRunning():
            # item.thisown = 1
            pass

    pcbnew.BOARD_ITEM_CONTAINER.Remove = _board_item_container_Remove  # type: ignore[method-assign]
    del _board_item_container_Remove


# .Delete() is ".Remove() and then free", but that's a silly thing to
# expose to Python; there should be no explicit frees, and we should
# let the Python garbage collector free things.  Otherwise there might
# be use-after-free bugs, which is surprising to Python programmers.
if True:
    pcbnew.BOARD_ITEM_CONTAINER.Delete = pcbnew.BOARD_ITEM_CONTAINER.Remove  # type: ignore[method-assign]
