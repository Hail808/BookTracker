import { getBooks } from "../src/lib/api";
import { Book } from "../src/types";

export default async function Home() {
    const books = await getBooks();
    
    return (
        <main>
            <h1>Book Tracker</h1>
            {books.map((book: Book) => (
                <div key={book.id}>
                    <p>{book.title} by {book.author}</p>
                    <p>Status: {book.status}</p>
                    <p>Volume: {book.currentVol} | Chapter: {book.currentCh}</p>
                </div>
            ))}
        </main>
    );
}
