import aiohttp

from typing import Iterable

from utils import consts
from domains.comments import Comment
from repositories.icomment_repository import ICommentRepository


class CommentRepository(ICommentRepository):

    def __init__(self) -> None:
        self._comments: list[Comment] = []

    async def save_all(self, comments: Iterable[Comment]) -> None:
        self._comments = list(comments)

    async def get_all(self) -> Iterable[Comment] | None:
        return list(self._comments)

    async def fetch_all(self) -> Iterable[Comment] | None:
        async with aiohttp.ClientSession() as session:
            async with session.get(consts.POSTS_URL) as response:
                if response.status != 200:
                    return None

                data = await response.json()
                return [
                    Comment(
                        user_id=item["userId"],
                        id=item["id"],
                        name=item["name"],
                    )
                    for item in data
                ]

