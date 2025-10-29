from abc import ABC
from typing import Iterable

from domains.comments import Comment


class ICommentRepository(ABC):

    async def save_all(self, comments: Iterable[Comment]) -> None:
        pass

    async def get_all(self) -> Iterable[Comment] | None:
        pass

    async def fetch_all(self) -> Iterable[Comment] | None:
        pass
