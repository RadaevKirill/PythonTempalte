import logging

import pytest

from src.main import MESSAGE, main


def test_main(caplog: pytest.LogCaptureFixture) -> None:
    caplog.set_level(logging.INFO)

    main()
    assert MESSAGE in caplog.text
