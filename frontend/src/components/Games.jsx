import { useState } from 'react';
import '../styles/games.css'
import PageIcon from './PageIcon';
import { useNavigate } from "react-router-dom";

function Games() {
    document.title = 'Games Library';

    const navigate = useNavigate();

    const datagames = [
    {
        id: 1,
        name: 'Knock-Knock',
        developer: 'Ice-Pick Lodge',
        year: 2013,
        genres: ["horror", "adventure", "psychological", "puzzle"],
        platform: ["PC "],
        link: 'https://store.steampowered.com/app/250380/KnockKnock/'
    },
    {
        id: 2,
        name: 'Milk outside a bag of milk outside a bag of milk',
        developer: 'Nikita Krukov',
        year: 2021,
        genres: ["psychological", "visual-novel", "horror", "drama"],
        platform: ["PC ", "Mobile "],
        link: 'https://store.steampowered.com/app/1600360/Milk_outside_a_bag_of_milk_outside_a_bag_of_milk/'
    },
    {
        id: 3,
        name: 'Beholder',
        developer: 'Warm Lamp Games',
        year: 2016,
        genres: ["simulator", "strategy", "dystopia", "political"],
        platform: ["PC ", "Mobile ", "Switch "],
        link: 'https://store.steampowered.com/app/475550/Beholder/'
    }
];

    const [genre, setGenre] = useState("all");

    const filteredGames = genre === "all" 
    ? datagames 
    : datagames.filter(game => game.genres.includes(genre));

    const handleGenre = (e) => {
        setGenre(e.target.value)
    }

    const handleGame = (link) => {
        window.open(link,'_blank', 'noopener,noreferrer')
    }

    return (
        <>
        <PageIcon iconName="games" />
        <div className="games">
            <h1>👾 Games Page</h1>
            <h5>You may click games!</h5>
            <div className="character">
                <select name="" id="" value={genre} onChange={handleGenre}>
                    <option value="all">all</option>
                    <option value="action">Action</option>
                    <option value="adventure">Adventure</option>
                    <option value="rpg">RPG</option>
                    <option value="strategy">Strategy</option>
                    <option value="simulator">Simulator</option>
                    <option value="puzzle">Puzzle</option>
                    <option value="horror">Horror</option>
                    <option value="survival">Survival</option>
                    
                    <option value="psychological">Psychological</option>
                    <option value="visual-novel">Visual Novel</option>
                    <option value="dystopia">Dystopia</option>
                    <option value="political">Political</option>
                    <option value="detective">Detective</option>
                    <option value="noir">Noir</option>
                    <option value="fantasy">Fantasy</option>
                    <option value="drama">Drama</option>
                    
                    <option value="fps">FPS</option>
                    <option value="sandbox">Sandbox</option>
                    <option value="platformer">Platformer</option>
                    <option value="fighting">Fighting</option>
                    <option value="racing">Racing</option>
                    <option value="sports">Sports</option>
                    <option value="roguelike">Roguelike</option>
                    <option value="metroidvania">Metroidvania</option>
                    <option value="point-and-click">Point & Click</option>
                    <option value="arcade">Arcade</option>
                    <option value="mmo">MMO</option>
                    <option value="mobile">Mobile</option>
                    <option value="indie">Indie</option>
                </select>
                <button
                className='btn'
                onClick={() => navigate("/games/add")}
                >
                Add new..
                </button>
            </div>
            <div className="cards">
                {filteredGames.map(game => {
                    return (
                        <div
                        key={game.id}
                        className='game'
                        onClick={() => handleGame(game.link)}
                        >
                            <div className="name">
                                <p>{game.name}</p>
                            </div>
                            <div className="developer">
                                <p>{game.developer}</p>
                            </div>
                            <div className="year">
                                <p>{game.year}</p>
                            </div>
                            <div className="platform">
                                <p>{game.platform}</p>
                            </div>
                        </div> 
                        )
                })}
                {datagames.length === 0 && (
                    <p style={{color: 'white'}}>No games yet!</p>
                )}
                {filteredGames.length === 0 && (
                    <p style={{color: 'white'}}>No games found!</p>
                )}
            </div>
        </div>
        </>
    )
}

export default Games;