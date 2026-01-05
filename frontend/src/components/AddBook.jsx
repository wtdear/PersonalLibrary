import { useState } from "react";

function AddBook() {
    const [query, setQuery] = useState("");
    const [results, setResults] = useState([]);
    const token = localStorage.getItem("token");

    const searchBook = async () => {
        const res = await fetch("/api/books/search", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${token}`,
            },
            body: JSON.stringify({ query }),
        });

        const data = await res.json();
        setResults(data);
    };

    const addBook = async (bookId) => {
        await fetch(`/api/user/books/add`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${token}`,
            },
            body: JSON.stringify({ bookId }),
        });
    };

    return (
        <div className="add-book">
            <input
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="Enter book title"
            />
            <button onClick={searchBook}>Search</button>

            {results.length > 0 && (
                <div className="results">
                    {results.map(book => (
                        <div key={book.id}>
                            <p>{book.title}</p>
                            <button onClick={() => addBook(book.id)}>
                                Add
                            </button>
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
}

export default AddBook;
