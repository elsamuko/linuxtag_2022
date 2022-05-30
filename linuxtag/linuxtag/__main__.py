
import importlib.metadata as metadata


def get_version() -> str:
    try:
        return str(metadata.version("linuxtag"))
    except metadata.PackageNotFoundError:
        return "0.0"


def main() -> None:
    print("Hello!")
    print(get_version())


if __name__ == "__main__":
    main()
