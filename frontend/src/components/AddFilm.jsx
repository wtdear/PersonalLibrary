import { useState } from "react";

function AddFilm() {
    const [query, setQuery] = useState("");
    const [results, setResults] = useState([]);
    const token = localStorage.getItem("token");

    const searchFilm = async () => {
        const res = await fetch("/api/films/search", {
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

    const addFilm = async (filmId) => {
        await fetch(`/api/user/films/add`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${token}`,
            },
            body: JSON.stringify({ filmId }),
        });
    };

    return (
        <div className="add-film">
            <input
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="Enter film title"
            />
            <button onClick={searchFilm}>Search</button>

            {results.length > 0 && (
                <div className="results">
                    {results.map(film => (
                        <div key={film.id}>
                            <p>{film.title}</p>
                            <button onClick={() => addFilm(film.id)}>
                                Add
                            </button>
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
}

export default AddFilm;
