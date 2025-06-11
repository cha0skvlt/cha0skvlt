"""Test module imports."""

import importlib
import pkgutil
import sys
from pathlib import Path

PACKAGE = 'cha0skvlt'

# Ensure package root is on path
sys.path.append(str(Path(__file__).resolve().parents[1]))


def test_all_modules_importable():
    package = importlib.import_module(PACKAGE)
    for _, modname, _ in pkgutil.walk_packages(package.__path__, package.__name__ + '.'):
        importlib.import_module(modname)
