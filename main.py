from src.config import config
from src.service import ImportFormatter


def main():
    formatter = ImportFormatter(config=config)
    exit(formatter.convert_relative_imports())


if __name__ == "__main__":
    main()
