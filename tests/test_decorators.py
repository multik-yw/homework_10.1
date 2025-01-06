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


def test_log_error(capsys: Any) -> Any:
    function(1, 'a')
    output = capsys.readouterr()
    assert "function error:" in output.out


def test_function_error() -> None:
    assert ValueError("Test error")


def test_log_error_2() -> None:
    with pytest.raises(Exception):
        assert function()


def test_log_error_3(capsys: Any) -> Any:
    @log(filename= None)
    def function(x=1, y=2):
        captured = capsys.readouterr()
        assert captured.out == "2024-12-23 18:50:48,463 - function ок, result =3"
