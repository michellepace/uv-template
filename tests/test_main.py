from typing import TYPE_CHECKING

from uv_package_template import main

if TYPE_CHECKING:
    import pytest


def test_main_runs(capsys: pytest.CaptureFixture[str]) -> None:
    main()
    assert capsys.readouterr().out == "Hello from uv-package-template!\n"
