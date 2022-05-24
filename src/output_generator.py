"""
'''
Description: a Weibo Emoji image generator
Version: 2.0.0.20220524
Author: Arvin Zhao
Date: 2022-03-31 16:57:38
Last Editors: Arvin Zhao
LastEditTime: 2022-05-24 13:28:26
'''
"""

from typing import Optional
import json
import os
import shutil

from dotenv import load_dotenv
from PIL import Image

from downloader import load_emoji_list

ERROR_MESSAGE_TEMPLATE = "Error: {}"


def convert_to_gif(output_dir: str, source_dir: str) -> None:
    """Convert the original output images to GIF images.

    Parameters
    ----------
    output_dir : str
        The output directory.
    """
    print("Converting to GIF...")

    with os.scandir(source_dir) as entries:
        n_emoji = 0

        for entry in entries:
            if entry.is_dir():
                with os.scandir(entry.path) as subentries:
                    for subentry in subentries:
                        if subentry.is_dir():
                            print(
                                'The directory "{}" is skipped for conversion.'.format(
                                    os.path.join(entry.name, subentry.name)
                                )
                            )
                            continue

                        n_emoji += save_gif(
                            destination_dir=os.path.join(output_dir, entry.name),
                            source=subentry,
                        )

                continue

            n_emoji += save_gif(destination_dir=output_dir, source=entry)

        print("{} image{} converted.".format(n_emoji, "" if n_emoji <= 1 else "s"))


def process_emotion_pack(
    emotion_dirname: str,
    emotion_pack_dir: str,
    output_dir: str,
    source_1_map: dict,
) -> None:
    """Process the emotion pack.

    Parameters
    ----------
    emotion_dirname : str
        The emotion directory name.
    emotion_pack_dir : str
        The emotion pack directory.
    output_dir : str
        The output directory.
    source_1_map : dict
        The dictionary using the Source 1 emoji list's value property as the key.
    """
    emotion_raw_info: list[dict] = []
    info_filename = "info.json"
    info_file_path = os.path.join(emotion_pack_dir, info_filename)

    if os.path.isfile(info_file_path):
        info_file = open(info_file_path)
        info: dict = json.load(info_file)
        info_file.close()
        emotion_raw_info = info.get("emoticons", [])
    else:
        print(
            'No "{}" found in the emotion pack of "{}".'.format(
                info_filename, emotion_dirname
            )
        )

    emotion_info = {}

    for emotion_raw in emotion_raw_info:
        filename: Optional[str] = emotion_raw.get("png")
        value: Optional[str] = emotion_raw.get("chs")

        if filename is None or value is None:
            print(
                'No filename or value found in the emotion info\'s dict {} of "{}".'.format(
                    emotion_raw, emotion_dirname
                )
            )
            continue

        emotion_info[filename] = value

    with os.scandir(emotion_pack_dir) as emotion_entries:
        for emotion_entry in emotion_entries:
            # A PNG image in the directory entry's emotion pack is expected.
            if not emotion_entry.is_file() or not emotion_entry.name.endswith(".png"):
                if emotion_entry.name != info_filename:
                    print(
                        '"{}" in "{}" is not a PNG image and is skipped.'.format(
                            emotion_entry.name, emotion_dirname
                        )
                    )

                continue

            process_emotion(
                filename=emotion_entry.name,
                output_dir=output_dir,
                source_1_map=source_1_map,
                source_file_path=os.path.join(emotion_pack_dir, emotion_entry.name),
                value=emotion_info.get(emotion_entry.name)
                if emotion_entry.name in emotion_info.keys()
                else " {} ".format(
                    emotion_entry.name[: emotion_entry.name.rindex(".")]
                ),
            )


def generate_output() -> None:
    """Generate Weibo Emoji images for a new release."""
    load_dotenv()
    output_dir = os.path.join("..", "output")
    release_dir_name = "WeiboEmoji_V{}".format(os.getenv("VERSION", "0"))
    original_output_dir = os.path.join(output_dir, release_dir_name, "original")
    print("Initialising output...")

    if os.path.isdir(output_dir):
        try:
            shutil.rmtree(output_dir)
        except OSError as e:
            print(ERROR_MESSAGE_TEMPLATE.format(e))
            return

    process_source_1(output_dir=original_output_dir)
    process_source_2(output_dir=original_output_dir)
    convert_to_gif(
        output_dir=os.path.join(output_dir, release_dir_name, "gif"),
        source_dir=original_output_dir,
    )


def generate_source_1_map() -> dict:
    """Generate a dictionary using the Source 1 emoji list's value property as the key.

    Returns
    -------
    dict
        The dictionary using the Source 1 emoji list's value property as the key.
    """
    images = load_emoji_list()
    source_1_map = {}

    for image in images:
        category: str = image.get("category", "未定义")
        value: Optional[str] = image.get("value")

        if value is None:
            print("No value found in {}.".format(image))
            continue

        source_1_map[value[1:-1]] = {
            "category": category if category != "" else "默认",
            "url": image.get("url"),
        }

    return source_1_map


def process_emotion(
    filename: str,
    output_dir: str,
    source_1_map: dict,
    source_file_path: str,
    value: str,
) -> None:
    """Process an emotion dictionary in the emotion info from Source 2.

    Parameters
    ----------
    filename : str
        The emotion image's filename.
    output_dir : str
        The output directory.
    source_1_map : dict
        The dictionary using the Source 1 emoji list's value property as the key.
    source_file_path : str
        The path of the emotion image in Source 2.
    value : str
        The emotion's value property.
    """
    duplication: Optional[dict] = source_1_map.get(value[1:-1])
    category: Optional[str] = (
        "补充" if duplication is None else duplication.get("category")
    )
    category_dir = os.path.join(output_dir, category)
    url: Optional[str] = "" if duplication is None else duplication.get("url")

    if category is None or url is None:
        print(
            'No category or URL found in the Source 1 map\'s dict "{}".'.format(
                {value[1:-1]: duplication}
            )
        )
        return

    if not os.path.isdir(category_dir):
        os.makedirs(category_dir)

    try:
        shutil.copy2(
            source_file_path,
            os.path.join(
                category_dir,
                "{}{}".format(
                    "{}{}".format(
                        value[1:-1],
                        "_mobile" if url.endswith(".gif") else "",
                    ),  # The suffix is needed if Source 2 contains the emotion with the same value as that in Source 1 but the emotion contained in Source 2 is in PNG format for mobile rather than GIF format.
                    filename[filename.rindex(".") :],
                ),
            ),
        )  # Replace the emotions in Source 1 with the same value as that in Source 2, or copy the emotions from Source 2 to Source 1. The specific operation for each emotion depends.
    except OSError as e:
        print(ERROR_MESSAGE_TEMPLATE.format(e))
        return


def process_source_1(output_dir: str) -> None:
    """Process the images from Source 1.

    Parameters
    ----------
    output_dir : str
        The output directory.
    """
    print("Processing Source 1...")
    source_1_dir = os.path.join("..", "img", "source_1")

    # Copy all contents from Source 1 to the output directory.
    with os.scandir(source_1_dir) as entries:
        for entry in entries:
            output_category_dir = os.path.join(output_dir, entry.name)

            if entry.is_dir():
                try:
                    shutil.copytree(entry.path, output_category_dir)
                except OSError as e:
                    print(ERROR_MESSAGE_TEMPLATE.format(e))
            else:
                try:
                    shutil.copy2(entry.path, output_category_dir)
                except OSError as e:
                    print(ERROR_MESSAGE_TEMPLATE.format(e))


def process_source_2(output_dir: str) -> None:
    """Process the images from Source 2.

    Parameters
    ----------
    output_dir : str
        The output directory.
    """
    print("Processing Source 2...")
    source_1_map = generate_source_1_map()
    source_2_dir = os.path.join("..", "img", "source_2")

    with os.scandir(source_2_dir) as entries:
        for entry in entries:
            # A directory entry (e.g. com.sina.default) is expected.
            if not entry.is_dir():
                print('"{}" is not a directory and is skipped.'.format(entry.name))
                continue

            emotion_pack_dir = os.path.join(entry.path, "emotionPack")

            if not os.path.isdir(emotion_pack_dir):
                print('No emotion pack found in "{}".'.format(entry.name))
                continue

            process_emotion_pack(
                emotion_dirname=entry.name,
                emotion_pack_dir=emotion_pack_dir,
                output_dir=output_dir,
                source_1_map=source_1_map,
            )


def save_gif(destination_dir: str, source: os.DirEntry) -> bool:
    """Save an image in GIF format.

    Parameters
    ----------
    destination_dir : str
        The destination directory.
    source : os.DirEntry
        The source image entry.

    Returns
    -------
    bool
        A flag indicating if the image is saved successfully.
    """
    if not os.path.isdir(destination_dir):
        os.makedirs(destination_dir)

    destination_path = os.path.join(
        destination_dir,
        "{}{}".format(source.name[: source.name.rindex(".")], ".gif"),
    )

    if source.name.endswith(".gif"):
        shutil.copy2(source.path, destination_path)
        return True

    try:
        emoji = Image.open(source.path).convert("RGBA")
        background = Image.new(color=(0, 0, 0, 0), mode="RGBA", size=emoji.size)
        emoji_copy = emoji.copy()
        background.paste(im=emoji_copy, mask=emoji_copy)
        background.save(fp=destination_path, optimize=True)
    except OSError as e:
        print(ERROR_MESSAGE_TEMPLATE.format(e))
        return False

    return True


# For simple tests only.
if __name__ == "__main__":
    generate_output()
