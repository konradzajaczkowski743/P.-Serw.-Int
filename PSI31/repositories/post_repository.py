import aiohttp

from typing import Iterable

from utils import consts
from domains.posts import Post
from repositories.ipost_repository import IPostRepository


class PostRepository(IPostRepository):

    def __init__(self) -> None:
        self._posts: list[Post] = []

    async def save_all(self, posts: Iterable[Post]) -> None:
        self._posts = list(posts)

    async def get_all(self) -> Iterable[Post] | None:
        return list(self._posts)

    async def fetch_all(self) -> list[Post] | None:
        async with aiohttp.ClientSession() as session:
            async with session.get(consts.POSTS_URL) as response:
                if response.status != 200:
                    return None

                data = await response.json()
                return [
                    Post(
                        user_id=item["userId"],
                        id=item["id"],
                        title=item["title"],
                        body=item["body"]
                    )
                    for item in data
                ]
