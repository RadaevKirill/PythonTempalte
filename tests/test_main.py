from pytest import CaptureFixture

from src.main import MESSAGE, main


def test_main(capsys: CaptureFixture[str]) -> None:
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == MESSAGE
