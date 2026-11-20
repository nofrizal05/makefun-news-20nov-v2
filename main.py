"""Entry program for make.fun news-image-20261120 (v2).

Copies the shipped entry.png to the output directory using only the
Python 3.13 standard library, so it runs in the grading sandbox,
which has nothing installed and no network. After the copy it verifies
the output is byte-identical to the source (size and sha256), so a
truncated or corrupted copy can never pass silently.
"""
import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(OUT_DIR, "entry.png")
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(src, dst)
    src_size = os.path.getsize(src)
    dst_size = os.path.getsize(dst)
    if src_size != dst_size:
        raise SystemExit(
            "entry.png copy failed: size mismatch "
            f"(source {src_size} bytes, output {dst_size} bytes)"
        )
    src_hash = sha256_of(src)
    dst_hash = sha256_of(dst)
    if src_hash != dst_hash:
        raise SystemExit(
            "entry.png copy failed: sha256 mismatch "
            f"(source {src_hash}, output {dst_hash})"
        )


if __name__ == "__main__":
    main()
