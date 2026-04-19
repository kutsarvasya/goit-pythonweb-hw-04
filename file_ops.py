import asyncio
import shutil
from pathlib import Path
from logger import logger


async def copy_file(file_path: Path, output_folder: Path):
    try:
        extension = file_path.suffix.lower().lstrip(".")
        if not extension:
            extension = "no_extension"

        target_folder = output_folder / extension

        await asyncio.to_thread(target_folder.mkdir, parents=True, exist_ok=True)

        target_file = target_folder / file_path.name

        await asyncio.to_thread(shutil.copy2, file_path, target_file)

        logger.info("Copied %s -> %s", file_path, target_file)

    except Exception as error:
        logger.error("Error copying %s: %s", file_path, error)


async def read_folder(source_folder: Path, output_folder: Path):
    tasks = []

    try:
        for item in source_folder.iterdir():
            if item.is_dir():
                tasks.append(read_folder(item, output_folder))
            elif item.is_file():
                tasks.append(copy_file(item, output_folder))
    except Exception as error:
        logger.error("Error reading folder %s: %s", source_folder, error)
        return

    if tasks:
        await asyncio.gather(*tasks)
