import { useEffect } from 'react';
import '../styles/library-main.css'
import PageIcon from './PageIcon';
import { useNavigate } from "react-router-dom";

function Library() {
    document.title = 'Choose Your Library';

    const navigate = useNavigate();
    const user = JSON.parse(localStorage.getItem("user"));

    useEffect(() => {
        if (!user) navigate("/auth");
    }, []);

    const dataCards = [
        {
            id: 1,
            name: 'Books',
            img: '📚',
            link: '/books'
        },
        {
            id: 2,
            name: 'Films',
            img: '🎬',
            link: '/films'
        },
        {
            id: 3,
            name: 'Games',
            img: '👾',
            link: '/games'
        }
    ]

    const handleCategory = (url) => {
        window.open(url,'_blank', 'noopener,noreferrer')
    }

    return (
        <>
            <PageIcon iconName="library"></PageIcon>
            <div className="profile" >
                <div className="acc" onClick={() => navigate("/profile")}>
                    <div className="logo">
                        <img src="/public/user.png" alt="" />
                    </div>
                    <p style={{ fontSize: '16px', fontWeight: 'bold'}}>{user.name}</p>
                </div>
            </div>
            <div className="library">
                <div className="block">
                    <h1 style={{color: 'white'}}>Hi, {user.name}!</h1>
                    <h2>Choose library!</h2>
                    <div className='cards'>
                    {dataCards.map(card => {
                        return (
                        <div
                        key={card.id}
                        className='card'
                        onClick={() => handleCategory(card.link)}
                        >
                            <div className="title">
                                <p>{card.name}</p>
                            </div>
                            <div className="text">
                                <p>{card.img}</p>
                            </div>
                        </div> 
                        )
                    })}
                    </div>
                </div>
            </div>
        </>
    )
}

export default Library