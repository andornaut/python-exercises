import os
from collections.abc import Generator

import pytest


@pytest.fixture
def lines_generator(request):
    basename = request.node.get_closest_marker("lines_generator").args[0]
    abs_path = os.path.join(os.path.dirname(__file__), basename)

    def generator() -> Generator[str, None, None]:
        with open(abs_path, "r") as f:
            for line in f:
                yield line.strip()

    return generator
