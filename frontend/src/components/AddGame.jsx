import { useState } from "react";

function AddGame() {
    const [query, setQuery] = useState("");
    const [results, setResults] = useState([]);
    const token = localStorage.getItem("token");

    const searchGame = async () => {
        const res = await fetch("/api/games/search", {
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

    const addGame = async (gameId) => {
        await fetch(`/api/user/games/add`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${token}`,
            },
            body: JSON.stringify({ gameId }),
        });
    };

    return (
        <div className="add-game">
            <input
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="Enter game title"
            />
            <button onClick={searchGame}>Search</button>

            {results.length > 0 && (
                <div className="results">
                    {results.map(game => (
                        <div key={game.id}>
                            <p>{game.title}</p>
                            <button onClick={() => addGame(game.id)}>
                                Add
                            </button>
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
}

export default AddGame;
