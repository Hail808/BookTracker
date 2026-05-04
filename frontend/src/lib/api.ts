import { Book } from "../types";

export async function getBooks(): Promise<Book[]> {
    const response = await fetch("http://127.0.0.1:8000/books");
    return response.json();
}