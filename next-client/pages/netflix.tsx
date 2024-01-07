/* Description: This page will fetch data from the API endpoint '/netflix'
and display it on the page.*/
// Author: Andrew Tomich

import React, { useEffect, useState } from "react";
import axiosInstance from "../utils/axios";

import Container from "react-bootstrap/Container";
import Card from "react-bootstrap/Card";

import style from "./netflix.module.css";

/**
 * Renders the api page component.
 * Fetches data from the API and displays a loading message until the data is fetched.
 */
function Netflix() {

  type NetflixContent = { title: string, description: string };

  const [data, setData] = useState<NetflixContent[]>([]);

  useEffect(() => {
    const fetchData = async () => {
      try{
        const res = await axiosInstance.get("/netflix");
        setData(res.data.data);
       } catch (err) {
        console.error(err);
      }
    };

    fetchData();
  }, []);

  return (
    // map the data to a list of JSX elements with the title and description
    <div>
      <h1>Netflix</h1>
      {data && data.map((item, index) => (
        <Container key={index}>
          <Card className={style.container}>
            <Card.Body className={style.netflixContent}>
              <Card.Title>{item.title}</Card.Title>
              <Card.Text>{item.description}</Card.Text>
            </Card.Body>
          </Card>
        </Container>
      )
      )}
    </div>
  );
}

export default Netflix;
