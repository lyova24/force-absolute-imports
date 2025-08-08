from src.config import config
from src.service import ImportFormatter


def main():
    formatter = ImportFormatter(config=config)
    scanned, changed = formatter.convert_relative_imports()
    print(f"done! scanned {scanned}; changed {changed};")


if __name__ == '__main__':
    main()
