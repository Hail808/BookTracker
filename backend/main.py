from fastapi import FastAPI
from pydantic import BaseModel
import sys
sys.path.append(".")
import tracker

app = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    status: str
    currentVol: int
    currentCh: int

class BookUpdate(BaseModel):
    key: str
    value: str

@app.get("/books")
def get_books():
    return tracker.load_library()

@app.post("/books")
def add_book(book: Book):
    return tracker.add_book(book.model_dump())

@app.put("/books/{book_id}")
def update_book(book_id: int, update: BookUpdate):
    return tracker.update_book(book_id, update.key, update.value)

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    return tracker.delete_book(book_id)