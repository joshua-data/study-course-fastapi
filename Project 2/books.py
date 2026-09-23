from fastapi import FastAPI, Path, Query, HTTPException
from starlette import status
from modules import Book, BookRequest, set_valid_book_id


app = FastAPI()
BOOKS = [
    Book(1, "Computer Science Pro", "codingwithjoshua", "A very nice book!", 5, 2030),
    Book(2, "Be Fast with FastAPI", "codingwithjoshua", "A great book!",     5, 2030),
    Book(3, "Master Endpoints",     "codingwithjoshua", "A awesome book!",   5, 2029),
    Book(4, "HP1",                  "Author 1",         "Book Description",  2, 2028),
    Book(5, "HP2",                  "Author 2",         "Book Description",  3, 2027),
    Book(6, "HP3",                  "Author 3",         "Book Description",  1, 2026)
]


# =============================================================================
# [GET] Read Data
# =============================================================================

@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS

@app.get("/books/{id}", status_code=status.HTTP_200_OK)
async def read_book_by_id_path(id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == id:
            return book
    raise HTTPException(status_code=404, detail="Item not found.")

@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_books_by_rating_query(rating: int = Query(gt=0, lt=6)):
    books_to_return = []
    for book in BOOKS:
        if book.rating == rating:
            books_to_return.append(book)
    return books_to_return

@app.get("/books/published_year/", status_code=status.HTTP_200_OK)
async def read_books_by_published_year_query(published_year: int = Query(gt=1999, lt=2031)):
    books_to_return = []
    for book in BOOKS:
        if book.published_year == published_year:
            books_to_return.append(book)
    return books_to_return

# =============================================================================
# [POST] Create Data
# =============================================================================

@app.post("/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    new_book = set_valid_book_id(BOOKS, new_book)
    BOOKS.append(new_book)

# =============================================================================
# [PUT] Update Data
# =============================================================================

@app.put("/books/update-book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book_request: BookRequest):
    is_id_found = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_request.id:
            BOOKS[i] == book_request
            is_id_found = True
    if not is_id_found:
        raise HTTPException(status_code=404, detail="Item not found.")

# =============================================================================
# [DELETE] Delete Data
# =============================================================================

@app.delete("/books/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book_by_id_path(id: int = Path(gt=0)):
    is_id_found = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == id:
            BOOKS.pop(i)
            is_id_found = True
            break
    if not is_id_found:
        raise HTTPException(status_code=404, detail="Item not found.")
