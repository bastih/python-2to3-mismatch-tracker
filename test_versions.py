#!/usr/bin/env python3.6
"""
A module to check for parsing ability mismatches
"""
import csv
import itertools
import os.path
import subprocess

from collections import defaultdict

IMAGES = [
    "python:2.7", "python:3.3", "python:3.4", "python:3.5.2", "python:3.5.3",
    "python:3.6.1", "python:3.7.0a"
]
PATH = os.path.abspath(os.path.dirname(__file__))
FILENAMES = ["v30.py", "v33.py", "v35.py", "v36.py", "v37.py"]
invoke_2to3 = "docker run -w /code --rm -t -v {path}:/code {image} 2to3 --no-diff {filename}"
invoke_compile = "docker run -w /code --rm -t -v {path}:/code {image} python -m py_compile {filename}"

def yesno(b):
    return "yes" if b else "no"


def main():
    result = []

    for image, filename in itertools.combinations(IMAGES, FILENAMES):
        out = subprocess.run(
            invoke_2to3.format(path=PATH, filename=filename,
                               image=image).split(),
            check=False,
            stdout=subprocess.PIPE)
        rc_compile = subprocess.call(
            invoke_compile.format(path=PATH, filename=filename,
                                  image=image).split(),
            stdout=subprocess.PIPE)
        result.append((filename, image, rc_compile == 0,
                       not b"ParseError" in out.stdout))

    with open("version_compat.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["file", "python", "compile", "2to3"])
        writer.writerows(result)
    
    data = defaultdict(defaultdict)
    for line in result:
        fname, img, comp, to3 = line
        data[img]["image"] = img
        data[img][fname] = yesno(comp) + "/" + yesno(to3)

    with open("version_pivot.csv", "w") as f:
        writer = csv.DictWriter(f, ["image"] + FILENAMES)
        writer.writerow({k: k for k in ["image"] + FILENAMES})
        for image in IMAGES:
            writer.writerow(data[image])


if __name__ == '__main__':
    main()
