from pathlib import Path

_BASE_DIR = Path(__file__).absolute().parent
MONSTER_ART_DIR = _BASE_DIR / "ascii_art" / "monsters"
TEXT_ART_DIR = _BASE_DIR / "ascii_art" / "text"


def get_art(file_name: str, dir_path: Path) -> str:
    """
    テキストアスキーアートを返す
    :param dir_path: 対象ディレクトリ
    :param file_name: アスキーアートのファイル名
    :return: アスキーアート
    """

    with Path.open(dir_path / file_name, "r", encoding="utf-8") as f:
        return f.read()
