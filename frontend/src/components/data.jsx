import React, { useState } from "react";
import { useEffect } from "react";

const Data = () => {
  const [data, setData] = useState([]);
  const [error, setError] = useState("");
  try {
    useEffect(() => {
      const fetchData = async () => {
        const rawData = await fetch("http://127.0.0.1:5000/posts")
          .then((data) => data.json())
          .then((response) => {
            setData(response);
            console.log(response);
          })
          .catch((error) => {
            console.error("There was an error!", error.message);
            setError(error.message);
          });
      };
      fetchData();
    }, []);
  } catch (ex) {
    console.log(ex);
  }
  const table = (
    <>
      <p>Data Successfully retrieved!</p>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Post Body</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item) => (
            <tr key={item.id}>
              <td>{item.id}</td>
              <td>{item.name.slice(0, 10)}</td>
              <td>{item.email}</td>
              <td>{item.body.slice(0, 20)}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </>
  );
  const response = error ? <p>{error}</p> : table;
  return <>{response}</>;
};

export default Data;
