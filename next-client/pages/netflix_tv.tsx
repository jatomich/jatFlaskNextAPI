// Description: This page will fetch data from the API endpoint '/netflix/tv'
// Author: Andrew Tomich

import React, { useEffect, useState } from "react";
import axiosInstance from "../utils/axios";

import Container from "react-bootstrap/Container";
import Card from "react-bootstrap/Card";

import "../types/NetflixContent";

/**
 * Renders the api page component.
 * Fetches data from the API and displays a loading message until the data is fetched.
 */
function NetflixTv() {

  const [data, setData] = useState<NetflixContent[]>([]);

  useEffect(() => {
    const fetchData = async () => {
      try{
        const res = await axiosInstance.get("/netflix/tv");
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
      <h1>Netflix TV Shows</h1>
      {data && data.map((item, index) => (
        <Container key={index}>
          <Card>
            <Card.Body>
              <Card.Title>{item.title}</Card.Title>
              <Card.Text>{item.description}</Card.Text>
            </Card.Body>
          </Card>
        </Container>
      )
      )}
    </div>
  )
};

export default NetflixTv;