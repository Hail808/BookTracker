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

@app.get("/books")
def get_books():
    return tracker.load_library()

@app.post("/books")
def add_book(book: Book):
    return tracker.add_book(book.model_dump())