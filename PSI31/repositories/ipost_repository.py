from abc import ABC
from typing import Iterable

from domains.posts import Post


class IPostRepository(ABC):
    async def save_all(self, posts: Iterable[Post]) -> None:
        pass

    async def get_all(self) -> Iterable[Post] | None:
        pass

