from dataclasses import dataclass


@dataclass
class Comment:
    user_id: int
    id: int
    name: str
