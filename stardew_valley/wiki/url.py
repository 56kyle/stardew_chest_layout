
import os

from dataclasses import dataclass, field


@dataclass
class Url:
    value: str = field(repr=False)
    base: str = field(init=False)

    def __post_init__(self):
        self.base = os.path.dirname(self.value)


if __name__ == '__main__':
    test_url = Url('https://www.google.com/foo/bar/baz.html')



