from pathlib import Path
from typing import TYPE_CHECKING

import libcst as cst

from .import_transformer import ImportTransformer

if TYPE_CHECKING:
    from re import Pattern


class ImportFormatter:
    def __init__(
            self,
            root_dir: Path,
            file_paths: list[Path],
            ignore_patterns: list["Pattern"],
    ):
        self.root_dir = root_dir.resolve()
        self.file_paths = file_paths
        self.ignore_patterns = list(set(ignore_patterns))

    def convert_relative_imports(self) -> tuple[int, int]:
        scanned, changed = 0, 0
        for file_path in self.file_paths:
            if not file_path.is_file() or \
                    not file_path.name.endswith(".py") or \
                    any(pat.search(str(file_path)) for pat in self.ignore_patterns):
                continue

            scanned += 1
            if self._convert_imports(file_path):
                changed += 1
        return scanned, changed

    def _convert_imports(self, file_path: Path) -> bool:
        source = file_path.read_text(encoding="utf-8")
        tree = cst.parse_module(source)

        transformer = ImportTransformer(file_path, self.root_dir)
        modified_tree = tree.visit(transformer)

        if transformer.modified:
            file_path.write_text(modified_tree.code, encoding="utf-8")
            return True
        return False
