import { useState } from 'react';
import '../styles/films.css'
import PageIcon from './PageIcon';
import { useNavigate } from "react-router-dom";

function Films() {
    document.title = 'Films Library';

    const navigate = useNavigate();

    const datafilms = [
        {
            id: 1,
            name: 'The Batman',
            director: 'Matt Reeves',
            year: 2022,
            genres: ["action", "crime", "drama", "noir", "superhero"],
            link: 'https://www.kinopoisk.ru/film/590286/'
        },
        {
            id: 2,
            name: 'American Psycho',
            director: 'Mary Harron',
            year: 2000,
            genres: ["horror", "thriller", "drama", "satire", "psychological"],
            link: 'https://www.kinopoisk.ru/film/588/'
        },
        {
            id: 3,
            name: 'Drive',
            director: 'Nicolas Winding Refn',
            year: 2011,
            genres: ["crime", "drama", "thriller", "neo-noir"],
            link: 'https://www.kinopoisk.ru/film/276598/'
        },
    ]

    const [genre, setGenre] = useState("all");

    const filteredFilms = genre === "all" 
    ? datafilms 
    : datafilms.filter(film => film.genres.includes(genre));

    const handleGenre = (e) => {
        setGenre(e.target.value)
    }

    const handleFilm = (link) => {
        window.open(link,'_blank', 'noopener,noreferrer')
    }

    return (
        <>
        <PageIcon iconName="films" />
        <div className="films">
            <h1>🎬 Films Page</h1>
            <h5>You may click films!</h5>
            <div className="character">
                <select name="" id="" value={genre} onChange={handleGenre}>
                    <option value="all">all</option>
                    <option value="action">Action</option>
                    <option value="comedy">Comedy</option>
                    <option value="drama">Drama</option>
                    <option value="thriller">Thriller</option>
                    <option value="noir">Noir</option>
                    <option value="neo-noir">Neo-Noir</option>
                    <option value="superhero">Superhero</option>
                    <option value="animation">Animation</option>
                    <option value="documentary">Documentary</option>
                    <option value="musical">Musical</option>
                    <option value="western">Western</option>
                </select>
                <button
                className='btn'
                onClick={() => navigate("/films/add")}
                >
                Add new..
                </button>
            </div>
            <div className="cards">
                {filteredFilms.map(film => {
                    return (
                        <div
                        key={film.id}
                        className='film'
                        onClick={() => handleFilm(film.link)}
                        >
                            <div className="name">
                                <p>{film.name}</p>
                            </div>
                            <div className="director">
                                <p>{film.director}</p>
                            </div>
                            <div className="year">
                                <p>{film.year}</p>
                            </div>
                        </div> 
                        )
                })}
                {datafilms.length === 0 && (
                    <p style={{color: 'white'}}>No films yet!</p>
                )}
                {filteredFilms.length === 0 && (
                    <p style={{color: 'white'}}>No films found!</p>
                )}
            </div>
        </div>
        </>
    )
}

export default Films;