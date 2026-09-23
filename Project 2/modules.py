from pydantic import BaseModel, Field
from typing import Optional


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_year: int

    def __init__(self, id, title, author, description, rating, published_year):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_year = published_year


class BookRequest(BaseModel):
    id: Optional[int] = Field(description="ID is not needed on create.", default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)
    published_year: int = Field(gt=1999, lt=2031)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new book",
                "author": "Joshua",
                "description": "A new description of a book",
                "rating": 5,
                "published_year": 2026
            }
        }
    }


def set_valid_book_id(BOOKS: list, book: Book):
    if len(BOOKS) == 0:
        book.id = 1
    else:
        book.id = BOOKS[-1].id + 1
    return book
