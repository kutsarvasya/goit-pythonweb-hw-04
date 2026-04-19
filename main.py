import asyncio
from pathlib import Path

from parser import parse_args
from file_ops import read_folder
from logger import logger


async def main():
    args = parse_args()

    source_folder = Path(args.source)
    output_folder = Path(args.output)

    if not source_folder.exists():
        logger.error("Source folder does not exist: %s", source_folder)
        return

    if not source_folder.is_dir():
        logger.error("Source is not a folder: %s", source_folder)
        return

    await asyncio.to_thread(output_folder.mkdir, parents=True, exist_ok=True)

    await read_folder(source_folder, output_folder)


if __name__ == "__main__":
    asyncio.run(main())
