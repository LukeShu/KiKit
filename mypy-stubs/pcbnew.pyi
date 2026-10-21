import typing

class SwigPyIterator:  # line 58
    next: typing.Callable[[SwigPyIterator], typing.Any]  # missing in 10.0.7
    def __next__(self) -> typing.Any: ...  # line 92
