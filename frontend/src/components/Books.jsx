import { useState } from 'react';
import '../styles/books.css'
import PageIcon from './PageIcon';
import { useNavigate } from "react-router-dom";

function Books() {
    document.title = 'Books Library';

    const navigate = useNavigate();

    const databooks = [
        {
            id: 1,
            name: 'The Devils',
            author: 'Fyodor Dostoevsky',
            genres: ["psychological", "political", "philosophical", "classic"],
            link: 'https://www.chitai-gorod.ru/product/besy-roman-2863229'
        },
        {
            id: 2,
            name: 'The Man in the Queue',
            author: 'Josephine Tey',
            genres: ["detective", "mystery", "crime"],
            link: 'https://www.chitai-gorod.ru/product/chelovek-iz-ocheredi-2978877'
        },
        {
            id: 3,
            name: '1984',
            author: 'George Orwell',
            genres: ["dystopia", "political", "scifi", "social", "classic"],
            link: 'https://www.chitai-gorod.ru/product/1984-novyy-perevod-2918634'
        },
    ]

    const [genre, setGenre] = useState("all");

    const filteredBooks = genre === "all" 
    ? databooks 
    : databooks.filter(book => book.genres.includes(genre));

    const handleGenre = (e) => {
        setGenre(e.target.value)
    }

    const handleBook = (link) => {
        window.open(link,'_blank', 'noopener,noreferrer')
    }

    return (
        <>
        <PageIcon iconName="books"></PageIcon>
        <div className="books">
            <h1>📚 Books Page</h1>
            <h5>You may click books!</h5>
            <div className="character">
                <select name="" id="" value={genre} onChange={handleGenre}>
                    <option value="all">all</option>
                    <option value="psychological">Psychological</option>
                    <option value="detective">Detective</option>
                    <option value="mystery">Mystery</option>
                    <option value="crime">Crime</option>
                    <option value="dystopia">Dystopia</option>
                    <option value="scifi">Sci-Fi</option>
                    <option value="fantasy">Fantasy</option>
                    <option value="horror">Horror</option>
                    <option value="romance">Romance</option>
                    <option value="adventure">Adventure</option>
                    <option value="historical">Historical</option>
                    <option value="biography">Biography</option>
                    <option value="classic">Classic</option>
                    <option value="philosophical">Philosophical</option>
                    <option value="political">Political</option>
                    <option value="social">Social</option>
                    <option value="realism">Realism</option>
                    <option value="satire">Satire</option>
                </select>
                <button
                className='btn'
                onClick={() => navigate("/books/add")}
                >
                Add new..
                </button>
            </div>
            <div className="cards">
                {filteredBooks.map(book => {
                    return (
                        <div
                        key={book.id}
                        className='book'
                        onClick={() => handleBook(book.link)}
                        >
                            <div className="name">
                                <p>{book.name}</p>
                            </div>
                            <div className="author">
                                <p>{book.author}</p>
                            </div>
                        </div> 
                        )
                })}
                {databooks.length === 0 && (
                    <p style={{color: 'white'}}>No books yet!</p>
                )}
                {filteredBooks.length === 0 && (
                    <p style={{color: 'white'}}>No books found!</p>
                )}
            </div>
        </div>
        </>
    )
}

export default Books;