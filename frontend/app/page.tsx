import { getBooks } from "../src/lib/api";

export default async function Home() {
    const books = await getBooks();
    console.log(books);
    return (
        <main>
            <h1>Book Tracker</h1>
        </main>
    );
}
