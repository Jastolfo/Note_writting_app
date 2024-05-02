import { useState } from "react";
import api from "../api";
import { useNavigate } from "react-router-dom";
import { REFRESH_TOKEN, ACCESS_TOKEN } from "../constants";
import "../styles/Form.css"

function Form({ route, method }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const name = method === "login" ? "Login" : "Register";

  const handleSubmit = async (e) => {
    setLoading(true);
    e.preventDefault();

    try {
      console.log(route);
      const res = await api.post(route, { username, password });

      console.log(`method: ${method}`);

      if (method === "login") {
        localStorage.setItem(ACCESS_TOKEN, res.data.access);
        localStorage.setItem(REFRESH_TOKEN, res.data.refresh);
        console.log('navigate to home');
        navigate("/");
      } else {
        console.log('navigate to login');
        navigate("/login")
      }
    } catch (error) {
      alert(error);
    } finally {
      setLoading(false);
    }
  }

  return <form onSubmit={handleSubmit} className="form-container">
    <h1>{name}</h1>
    <input
      className="form-input"
      type="text"
      value={username}
      onChange={(e) => setUsername(e.target.value)}
      placeholder="Username"
    />

    <input
      className="form-input"
      type="text"
      value={password}
      onChange={(e) => setPassword(e.target.value)}
      placeholder="password"
    />

    <button className="form-button" type="submit">
      {name}
    </button>
  </form>
}

export default Form