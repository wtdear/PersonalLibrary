import { useEffect, useState } from 'react';
import { useNavigate } from "react-router-dom";
import '../styles/auth.css'
import PageIcon from './PageIcon';

function Auth() {
    document.title = 'Аuthorization';

    const [isLogin, setIsLogin] = useState(false);

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [name, setName] = useState("");
    const [modal, setModal] = useState("");
    const [visible, setVisible] = useState(false);
    const [isClosing, setIsClosing] = useState(false);

    const navigate = useNavigate();

    const emailRegExp = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

    useEffect(() => {
        const token = localStorage.getItem("token");
        if (token) navigate("/library")
    }, [])

    useEffect(() => {
        if (modal) {
            setVisible(false);
            setTimeout(() => {
                setVisible(true);
            }, 1);
        }
    }, [modal])

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (!emailRegExp.test(email)) {
            setModal("Enter correct email!");
            return;
        }

        if (password.length < 8) {
            setModal("Your password must be at least 8 characters!");
            return;
        }

        if (!isLogin && name.trim().length < 2) {
            setModal("Enter correct username!");
            return;
        }

        const body = isLogin
            ? { email, password }
            : { email, password, name };

        const url = isLogin ? "/api/auth/login" : "/api/auth/register";

        try {
            const response = await fetch(url, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(body)
            });

            if (!response.ok) {
                const err = await response.json();
                setModal(err.message || "Server error!");
                return;
            }

            const data = await response.json();

            localStorage.setItem("token", data.token);
            localStorage.setItem("user", JSON.stringify(data.user));

            navigate("/library");

        } catch (err) {
            setModal("Connection error!");
        }
    };

    const closeWindow = () => {
        setIsClosing(true);
        setVisible(false);
        setTimeout(() => {
            setModal("");
            setIsClosing(false);
        }, 300);
    }

    return (
        <>
            <PageIcon iconName="auth" />
            <div className="container_auth">

                <div className='auth_login' style={{ width: "300px", margin: "0 auto" }}>
                    <h2>{isLogin ? "Login" : "Register"}</h2>

                    <form onSubmit={handleSubmit} noValidate>
                        <input
                            placeholder="Email"
                            type="email"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                        />
                        <br /><br />

                        <input
                            type="password"
                            placeholder="Password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                        />
                        <br /><br />

                        {!isLogin && (
                            <>
                                <input
                                    type="text"
                                    placeholder="Your name"
                                    value={name}
                                    onChange={(e) => setName(e.target.value)}
                                />
                                <br /><br />
                            </>
                        )}

                        <div className="cont-submit">
                            <button className='submit' type="submit">
                                {isLogin ? "Login" : "Sign up"}
                            </button>
                        </div>
                    </form>

                    <br />

                    <p className='already' onClick={() => setIsLogin(!isLogin)}>
                        {isLogin
                            ? "No account? Click sign up"
                            : "Already have an account? Click login"}
                    </p>
                </div>

                {modal && (
                    <>
                        <div
                            className={`modalBackdrop ${isClosing ? "closing" : ""}`}
                            onClick={closeWindow}
                        />

                        <div className={`modalWindow ${visible ? "active" : ""} ${isClosing ? "closing" : ""}`}>
                            <h2>{modal}</h2>
                            <button onClick={closeWindow}>Close this window</button>
                        </div>
                    </>
                )}
            </div>
        </>
    );
}

export default Auth;