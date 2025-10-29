from typing import Iterable

from domains.posts import Post
from repositories.ipost_repository import IPostRepository
from services.ipost_services import IPostService


class PostService(IPostService):
    repository: IPostRepository

    def __init__(self, repository: IPostRepository) -> None:
        self.repository = repository

    async def save_posts(self) -> Iterable[Post]:
        posts = await self.repository.fetch_all()
        await self.repository.save_all(posts)
        return posts

    async def filter_posts(self, query: str) -> Iterable[Post]:
        posts = await self.repository.get_all()

        query_lower = query.lower()
        return [
            p for p in posts
            if query_lower in p.title.lower() or query_lower in p.body.lower()
        ]
