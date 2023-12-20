import React, { useEffect, useState } from "react";
import axiosInstance from "../utils/axios";

/**
 * Renders the api page component.
 * Fetches data from the API and displays a loading message until the data is fetched.
 */
function Netflix() {

  type NetflixContent = { title: string, description: string };

  const [data, setData] = useState<NetflixContent[]>([]);

  useEffect(() => {
    axiosInstance.get("/netflix").then(
      res => res.data
    ).then((data) => {
        setData(data.data);
  });
  }, []);

  return (
    // map the data to a list of JSX elements with the title and description
    <div>
      <h1>Netflix</h1>
      {data && data.map((item, index) => (
        <div key={index}>
          <h2>{item.title}</h2>
          <p>{item.description}</p>
        </div>
      )
      )}
    </div>
  );
}

export default Netflix;