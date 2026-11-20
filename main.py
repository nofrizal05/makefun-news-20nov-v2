"""Entry program for make.fun news-image-20261120 (v2).

Copies the shipped entry.png to the output directory using only the
Python 3.13 standard library, so it runs in the grading sandbox,
which has nothing installed and no network.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(os.path.join(HERE, "entry.png"),
                os.path.join(OUT_DIR, "entry.png"))
