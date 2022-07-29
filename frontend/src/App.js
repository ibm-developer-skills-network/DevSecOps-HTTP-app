import logo from "./logo.svg";
import "./App.css";
import React from "react";
import Data from "./components/data";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <Data />
      </header>
    </div>
  );
}

export default App;
