import axios from "axios";
import React, { useState } from "react";
import { useEffect } from "react";

const Data = () => {
  const [data, setData] = useState();
  const [error, setError] = useState();
  try {
    useEffect(() => {
      const { data: raw } = fetch("http://127.0.0.1:5000/serve")
        .then((response) => response.json())
        .then((data) => setData(data))
        .catch((error) => {
          console.error("There was an error!", error.message);
          setError(error.message);
        });
      // setData(raw);
    }, []);
  } catch (ex) {
    console.log(ex);
  }
  const response = error ? <p>{error}</p> : <p>Data Successfully retrieved!</p>;
  return <>{response}</>;
};

export default Data;
