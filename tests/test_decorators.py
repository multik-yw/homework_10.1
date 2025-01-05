from typing import Any

import pytest

from src.decorators import log


@log()
def function(x: Any, y: Any) -> Any:
    return x + y


def test_log() -> Any:
    result = function(1, 2)
    assert result == 3


def test_successful_execution(capsys: Any) -> Any:
    function(1, 2)
    output = capsys.readouterr()
    assert "function ok" in output.out


def test_error_handling(capsys: Any) -> Any:
    function(1, 'a')
    output = capsys.readouterr()
    assert "function error:" in output.out


def test_function_error() -> None:
    assert ValueError("Test error")


def test_log_2() -> None:
    with pytest.raises(Exception):
        assert function()
