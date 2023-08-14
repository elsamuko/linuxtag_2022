import importlib.metadata as metadata
import logging
import signal
import sys
from typing import Any


def parse_version(version: str) -> str:
    # 0.1.post18 -> 0.1.18
    return version.replace("post", "")


def get_version() -> str:
    version = "0.1.0"
    try:
        version = str(metadata.version("linuxtag"))
    except metadata.PackageNotFoundError:
        pass
    return parse_version(version)


def handler(signum: int, frame: Any) -> None:
    print("Exiting...")
    sys.exit(0)


def configure_logger() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="[%(levelname)8s] %(asctime)s %(funcName)10s : %(message)s",
        handlers=[
            logging.StreamHandler(),
        ],
    )


def main() -> None:
    # handle keyboard interrupts
    signal.signal(signal.SIGINT, handler)

    configure_logger()

    print("Hello!")
    logging.info("Hello!")
    print(get_version())


if __name__ == "__main__":
    main()
