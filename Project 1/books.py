from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One',   'author': 'Author One',   'category': 'science'},
    {'title': 'Title Two',   'author': 'Author Two',   'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four',  'author': 'Author Four',  'category': 'math'},
    {'title': 'Title Five',  'author': 'Author Five',  'category': 'math'},
    {'title': 'Title Six',   'author': 'Author Two',   'category': 'math'},
]

# =============================================================================
# [GET] Read Data
# =============================================================================

@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/{title}")
async def read_books_by_title_path(title: str):
    for book in BOOKS:
        if book.get("title").casefold() == title.casefold():
            return book


@app.get("/books/")
async def read_books_by_category_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/{author}/")
async def read_books_by_author_path_category_query(author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("author").casefold() == author.casefold():
            if book.get("category").casefold() == category.casefold():
                books_to_return.append(book)
    return books_to_return

# =============================================================================
# [POST] Create Data
# =============================================================================

@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)

# =============================================================================
# [PUT] Update Data
# =============================================================================

@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == updated_book.get("title").casefold():
            BOOKS[i] = updated_book

# =============================================================================
# [DELETE] Delete Data
# =============================================================================
@app.delete("/books/delete_book/{title}")
async def delete_book(title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == title.casefold():
            BOOKS.pop(i)
            break
