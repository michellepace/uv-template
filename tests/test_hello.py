from typing import TYPE_CHECKING

from uv_template.hello import greet, main

if TYPE_CHECKING:
    import pytest


def test_greet_uses_the_given_name() -> None:
    assert greet("Michelle") == "Hello, Michelle!"


def test_main_prints_the_greeting(capsys: pytest.CaptureFixture[str]) -> None:
    main()
    assert capsys.readouterr().out == "Hello, world!\n"
