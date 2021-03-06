#!/usr/bin/env python
import os
import subprocess
import sys
from pathlib import Path

if __name__ == "__main__":
    os.chdir(Path(__file__).parent)
    os.environ["CUSTOM_COMPILE_COMMAND"] = "requirements/compile.py"

    try:
        os.environ.pop("PIP_REQUIRE_VIRTUALENV")
    except KeyError:
        pass

    common_args = ["-m", "piptools", "compile", "--generate-hashes"] + sys.argv[1:]
    subprocess.run(
        ["python3.7", *common_args, "-o", "py37.txt"],
        check=True,
    )
    subprocess.run(
        ["python3.8", *common_args, "-o", "py38.txt"],
        check=True,
    )
