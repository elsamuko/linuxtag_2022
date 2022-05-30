
import importlib.metadata as metadata
import signal
import sys


def get_version() -> str:
    try:
        return str(metadata.version("linuxtag"))
    except metadata.PackageNotFoundError:
        return "0.0"


def handler(signum, frame):
    print("Exiting...")
    sys.exit(0)


def main() -> None:
    # handle keyboard interrupts
    signal.signal(signal.SIGINT, handler)

    print("Hello!")
    print(get_version())


if __name__ == "__main__":
    main()
