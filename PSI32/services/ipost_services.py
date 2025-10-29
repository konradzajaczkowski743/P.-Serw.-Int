from typing import Iterable

from abc import ABC
from typing import Iterable
from domains.posts import Post


class IPostService(ABC):
    async def save_posts(self) -> Iterable[Post]:
        pass

    async def filter_posts(self, query: str) -> Iterable[Post]:
        pass


