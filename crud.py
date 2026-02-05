from fastapi import FastAPI, status
from typing import List, Optional
from pydantic import BaseModel
from fastapi.exceptions import HTTPException

books = [
    {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "published_date": "1988-01-01"
    },
    
    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "published_date": "1934-10-01"
    },
    
    {
        "id": 3,
        "title": "1984",
        "author": "George Orwell",
        "published_date": "1999-03-02"
    },
    
    {
        "id": 4,
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "published_date": "1990-03-06"
    }
]

app = FastAPI()


class CreateBook(BaseModel):
    id: int
    title: str
    author: str
    published_date: str
    


class UpdateBook(BaseModel):
    title: str
    author: str
    published_date: str


@app.get('/all_books')
async def get_all_books():
    return books




@app.get('/single_book/{book_id}', status_code=status.HTTP_200_OK)
async def single_book(book_id: int):
        for book in books:
            if book['id'] == book_id:
                return book
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    
    


@app.put('/update/{book_id}')
async def update_book(book_id: int, book_data: UpdateBook):
    for book in books:
        if book['id'] == book_id:
            book['title'] = book_data.title
            book['author'] = book_data.author
            book['published_date'] = book_data.published_date
            return {
                "message": "Book updated successfully",
                "book": book
            }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    



@app.post('/create_book')
async def create_book(book: CreateBook):
    new_book = book.model_dump()
    books.append(new_book)
    return {
        "message": "Book created successfully",
        "book": book
    }




@app.delete('/delete_book{book_id}')
async def delete_book(book_id: int):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return {
                "message": "Book deleted successfully"
            }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")