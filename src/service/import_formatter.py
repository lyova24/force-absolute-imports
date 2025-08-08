from pathlib import Path
from re import compile

import libcst as cst

from src.config import Config
from src.utils import (
    get_path_from_str,
    get_paths_from_list,
    exit_if_path_is_not_a_dir,
)
from .import_transformer import ImportTransformer
from src.logger import log


class ImportFormatter:
    def __init__(self, config: Config):
        self.root_dir = get_path_from_str(config.root_dir).resolve()
        self.file_paths = get_paths_from_list(config.file_paths)
        self.ignore_patterns = list(set([compile(pattern) for pattern in config.ignored_paths]))
        exit_if_path_is_not_a_dir(self.root_dir)

    def convert_relative_imports(self):
        scanned, changed = 0, 0
        for file_path in self.file_paths:
            if not file_path.is_file() or \
                    not file_path.name.endswith(".py") or \
                    any(pat.search(str(file_path)) for pat in self.ignore_patterns):
                log.debug(f"ignored: {file_path};")
                continue

            scanned += 1
            if self._convert_imports(file_path):
                changed += 1
        log.info(f"total_scanned {scanned}; total_changed {changed};")

    def _convert_imports(self, file_path: Path) -> bool:
        source = file_path.read_text(encoding="utf-8")
        tree = cst.parse_module(source)

        transformer = ImportTransformer(file_path, self.root_dir)
        modified_tree = tree.visit(transformer)

        if transformer.modified:
            log.debug(f"changed {file_path};")
            file_path.write_text(modified_tree.code, encoding="utf-8")
            return True
        log.debug(f"approved {file_path};")
        return False
