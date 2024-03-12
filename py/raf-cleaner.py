"""RAF Cleaner

This script cleans up, in a folder, all .RAF images with no .JPG version.

I use Adobe Bridge to mark then delete all .JPG files that I'm not satisfied with.
But this will leave the .RAF files, so I need to clean them up.

"""

import os
import argparse


def raf_clean(dir_path):
    clean_count = 0
    for root, _, files in os.walk(dir_path):
        for file in files:
            if file.lower().endswith('.raf'):
                basename = os.path.splitext(file)[0]
                jpg_file = basename + '.JPG'
                if not os.path.exists(os.path.join(root, jpg_file)):
                    raf_file = os.path.join(root, file)
                    print(f'To be cleaned: {raf_file}')
                    clean_count += 1
                    os.remove(raf_file)
    print(f'Cleaned {clean_count} RAF files')


def main():
    print("=== RAF Cleaner ===")
    parser = argparse.ArgumentParser(description='RAF Cleaner')
    parser.add_argument('-d', '--dir', required=True, help='Sub-folders will also be searched')

    args = parser.parse_args()
    raf_clean(args.dir)


if __name__ == '__main__':
    main()


