from typing import Any

from src.decorators import log


@log()
def function(x: Any, y: Any) -> Any:
    return x + y


def test_log() -> Any:
    result = function(1, 2)
    assert result == 3


def test_log_console(capsys: Any) -> None:
    function(2, 3)
    output = capsys.readouterr()
    assert output.out == "function ok\n"


def test_log_console_error(capsys: Any) -> None:
    function(2, "3")
    output = capsys.readouterr()
    assert output.out == "function error: TypeError. Inputs: (2, '3'), {}\n"
