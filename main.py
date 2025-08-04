import re

from service import ImportFormatter
from utils import get_args, get_path_from_str, exit_if_path_is_not_a_dir, get_paths_from_list

def main():
    args = get_args()
    root_dir = get_path_from_str(args.root_dir)
    file_paths = get_paths_from_list(args.files)
    exit_if_path_is_not_a_dir(root_dir)
    ignore_patterns = [re.compile(pattern) for pattern in args.ignore]
    formatter = ImportFormatter(
        root_dir=root_dir,
        file_paths=file_paths,
        ignore_patterns=ignore_patterns,
    )
    scanned, changed = formatter.convert_relative_imports()
    print(f"done! scanned {scanned}; changed {changed};")


if __name__ == '__main__':
    main()