from abc import ABC
from typing import Iterable

from domains.posts import Post


class IPostRepository(ABC):
    async def save_all(self, posts: Iterable[Post]) -> None:
        pass

    async def get_all(self) -> Iterable[Post] | None:
        pass

    async def fetch_all(self) -> list[Post] | None:
        pass

    async def delete_post(self, post_id: int) -> list[Post] | None:
        pass