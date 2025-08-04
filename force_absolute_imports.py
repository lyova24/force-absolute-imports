import ast
import sys
import argparse
import re
from pathlib import Path

if not hasattr(ast, "unparse"):
    print("python 3.9+ required.")
    sys.exit(1)


def get_module_path(file_path: Path, root_dir: Path) -> str | None:
    try:
        relative_path = file_path.resolve().relative_to(root_dir.resolve()).with_suffix("")
    except ValueError:
        print(f"skip: {file_path} not in root_dir {root_dir}")
        return None
    return ".".join(relative_path.parts)


def convert_relative_to_absolute_imports(file_path: Path, root_dir: Path) -> bool:
    source = file_path.read_text(encoding="utf-8")
    tree = ast.parse(source)
    modified = False

    class ImportTransformer(ast.NodeTransformer):
        def visit_ImportFrom(self, node):
            nonlocal modified
            if node.level > 0:
                current_module = get_module_path(file_path, root_dir)
                if current_module is None:
                    return node
                current_parts = current_module.split(".")
                if node.level > len(current_parts):
                    print(f"warn: level {node.level} too deep in {file_path}")
                    return node

                base_parts = current_parts[:-node.level]
                if node.module:
                    new_module = ".".join(base_parts + [node.module])
                else:
                    new_module = ".".join(base_parts)

                new_node = ast.ImportFrom(
                    module=new_module if new_module else None,
                    names=node.names,
                    level=0,
                )
                modified = True
                return ast.copy_location(new_node, node)
            return node

    transformer = ImportTransformer()
    new_tree = transformer.visit(tree)
    if modified:
        new_source = ast.unparse(new_tree)
        file_path.write_text(new_source, encoding="utf-8")
    return modified


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root-dir", required=False, default=".", help="path to root directory (for example, ./src)")
    parser.add_argument("--ignore", action="append", default=[], help="regex pattern to ignore file paths")
    parser.add_argument("files", nargs="+", help="files to be processed (pre-commit passing it)")
    args = parser.parse_args()

    root_dir = Path(args.root_dir).resolve()
    if not root_dir.is_dir():
        print(f"err: {root_dir} is not a directory")
        sys.exit(1)


    changed = 0
    scanned = 0
    ignore_patterns = [re.compile(pattern) for pattern in args.ignore]
    for file in args.files:
        path = Path(file)

        str_path = str(path)
        if any(pat.search(str_path) for pat in ignore_patterns):
            continue

        if not path.suffix == ".py":
            continue
        scanned += 1
        if convert_relative_to_absolute_imports(path, root_dir):
            changed += 1

    print(f"done! scanned: {scanned}, changed: {changed}")


if __name__ == "__main__":
    main()
