#! c:\Python\Python37\python.exe

import os
import piexif
import shutil
import sys


# import importlib.util
# spec = importlib.util.spec_from_file_location("module.name", "c:\Python\Python37\Lib\site-packages\piexif\__init__.py")
# foo = importlib.util.module_from_spec(spec)
# spec.loader.exec_module(foo)
# foo.MyClass()

dir_path = 'm:\\test_photo\\'


def main():
    expos = dict()
    n = 1

    for path, subdirs, files in os.walk(dir_path):
        for name in files:
            exif_dict = piexif.load(dir_path + name)
            expos[name[4:-4]] = exif_dict["Exif"][37380][0]
    print(expos)
    for item in expos:
        sub_dir_name = 'hdr_' + "%02d" % n
        if int(expos[item]) < 0:
            file_number = int(item)
            prev_file = file_number-1
            next_file = file_number+1
            if str(prev_file) in expos and str(next_file) in expos:
                if expos[str(prev_file)] == 0 and expos[str(next_file)] > 0:
                    print(sub_dir_name)
                    n += 1
                    if not os.path.exists(dir_path + sub_dir_name):
                        os.makedirs(dir_path + sub_dir_name)
                    print(prev_file, expos[str(prev_file)], dir_path + 'DSC_%s.NEF' % prev_file)
                    print(file_number, expos[str(file_number)], dir_path + 'DSC_%s.NEF' % file_number)
                    print(next_file, expos[str(next_file)], dir_path + 'DSC_%s.NEF' % next_file)

                    move_file_by_number(prev_file, sub_dir_name)
                    move_file_by_number(file_number, sub_dir_name)
                    move_file_by_number(next_file, sub_dir_name)


def move_file_by_number(file_number, sub_dir_name):
    shutil.move(dir_path + 'DSC_%s.NEF' % file_number, dir_path + sub_dir_name + '\DSC_%s.NEF' % file_number)


def get_parameters(file_path):
    exif_dict = piexif.load(file_path)
    for ifd in ("0th", "Exif", "GPS", "1st"):
        for tag in exif_dict[ifd]:
            print(piexif.TAGS[ifd][tag]["name"], exif_dict[ifd][tag])


if __name__ == '__main__':
    if len(sys.argv) == 1:
        main()
    else:
        dir_path = sys.argv[1]
        main()
