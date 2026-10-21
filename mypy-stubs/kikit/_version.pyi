import typing

_Versions = typing.TypedDict(
    "_Versions",
    {
        "version": str,
        "full-revisionid": str | None,
        "dirty": bool | None,
        "error": str | None,
        "date": str | None,
    },
)

def get_versions() -> _Versions: ...
