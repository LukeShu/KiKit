#!/usr/bin/env python3

import collections.abc
import io
import json
import typing
from collections import OrderedDict

import click

_JSONValue = typing.Union[
    typing.Dict[str, "_JSONValue"],
    typing.List["_JSONValue"],
    str,
    int,
    float,
    bool,
    None,
]


def setKey(obj: _JSONValue, path: list[str], value: _JSONValue) -> None:
    if not isinstance(obj, (dict, list)):
        raise TypeError(f"{obj.__class__.__name__!r} is not subscriptable")
    if len(path) == 1:
        if isinstance(obj, dict):
            obj[path[0]] = value
        if isinstance(obj, list):
            obj[int(path[0])] = value
        return
    if isinstance(obj, dict):
        setKey(obj[path[0]], path[1:], value)
    if isinstance(obj, list):
        setKey(obj[int(path[0])], path[1:], value)


@click.command()
@click.argument("input", type=click.File("r"))
@click.argument("output", type=click.File("w"))
@click.option("--property", "-s", type=str, multiple=True, help="<path>=<value>")
def run(input: "io.Reader[str]", output: "io.Writer[str]", property: str) -> None:
    """
    Set a key to a value in JSON.
    """
    obj = json.load(input, object_pairs_hook=OrderedDict)
    for p in property:
        _path, value = tuple(p.split("="))
        path = _path.split(".")
        value = json.loads(value, object_pairs_hook=OrderedDict)
        setKey(obj, path, value)

    json.dump(obj, output, indent=4)


if __name__ == "__main__":
    run()
