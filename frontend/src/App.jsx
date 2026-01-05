import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';

import Library from "./components/Library.jsx";

import Books from "./components/Books.jsx";
import Films from "./components/Films.jsx";
import Games from "./components/Games.jsx";

import Auth from './components/Auth.jsx';
import Profile from './components/Profile.jsx';

import PrivateRoute from './components/PrivateRoute.jsx';

import AddBook from './components/AddBook.jsx';
import AddFilm from './components/AddFilm.jsx';
import AddGame from './components/AddGame.jsx';

export default function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={
                    <Navigate to="/auth" />
                } />

                <Route path="/auth" element={<Auth />} />

                <Route path="/library" element={
                    <PrivateRoute>
                        <Library />
                    </PrivateRoute>
                } />

                <Route path="/books" element={
                    <PrivateRoute>
                        <Books />
                    </PrivateRoute>
                }></Route>

                <Route path="/films" element={
                    <PrivateRoute>
                        <Films />
                    </PrivateRoute>
                }></Route>

                <Route path="/games" element={
                    <PrivateRoute>
                        <Games />
                    </PrivateRoute>
                }></Route>
                
                <Route path="/profile" element={
                    <PrivateRoute>
                        <Profile />
                    </PrivateRoute>
                } />

                <Route path="/books/add" element={
                    <PrivateRoute>
                        <AddBook />
                    </PrivateRoute>
                } />

                <Route path="/films/add" element={
                    <PrivateRoute>
                        <AddFilm />
                    </PrivateRoute>
                } />

                <Route path="/games/add" element={
                    <PrivateRoute>
                        <AddGame />
                    </PrivateRoute>
                } />

            </Routes>
        </BrowserRouter>
    )
}