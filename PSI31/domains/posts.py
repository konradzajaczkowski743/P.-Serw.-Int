from dataclasses import dataclass


@dataclass(frozen=True)
class Post:
    user_id: int
    id: int
    title: str
    body: str
