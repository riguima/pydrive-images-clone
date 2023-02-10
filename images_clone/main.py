from argparse import ArgumentParser
from pathlib import Path

from adapters import Drive, FakeDrive
from domain import save_image


if __name__ == '__main__':
    parser = ArgumentParser(description='Google Drive images clone')
    parser.add_argument('-d', '--dir', type=str, help='Clone directory')
    parser.add_argument('-t', '--testing', action='store_true')
    args = parser.parse_args()
    if args.testing:
        drive = FakeDrive()
    else:
        drive = Drive()
    for image in drive.get_images():
        save_image(Path(args.dir), image.id, image.content)
