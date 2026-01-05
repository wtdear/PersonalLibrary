import PageIcon from './PageIcon';
import '../styles/profile.css'
import { useNavigate } from 'react-router-dom';

function Profile() {

    document.title = "Your profile"

    const user = JSON.parse(localStorage.getItem("user"))

    const navigate = useNavigate();

    return (
        <>
            <PageIcon iconName="profile" />
            <div className="container_profile">
            <div className="profile_info">
                <button className='close' onClick={() => navigate('/library')}>X</button>
                <h1 style={{color: 'white'}}>Hi, {user.name}!</h1>
                <div className="logo">
                    <img src="/public/user.png" alt="" />
                </div>
                <div className='container'>
                    <label htmlFor="name">Name:</label>
                    <input type="text" name='name' disabled value={user.name}/>
                    <label htmlFor="name">Email:</label>
                    <input type="text" name='name' disabled value={user.email}/>
                    <label htmlFor="name">Password:</label>
                    <input type="password" name='name' disabled value={user.password}/>
                </div>
                <div className="libraries">
                    <button onClick={() => navigate('/books')}>Books</button>
                    <button onClick={() => navigate('/films')}>Films</button>
                    <button onClick={() => navigate('/games')}>Games</button>
                </div>
            </div>
            </div>
        </>
    )
}

export default Profile;