// Description: This page will fetch a single item from the API endpoint '/netflix/:id'
// and display it on the page.
// Author: Andrew Tomich

import React, { useEffect, useState } from "react";
import { useRouter } from "next/router";
import axiosInstance from "../utils/axios";

import Container from "react-bootstrap/Container";
import Card from "react-bootstrap/Card";

import style from "./netflix.module.css";

/**
 * Renders the api page component.
 * Fetches data from the API and displays a loading message until the data is fetched.
 */
function NetflixId() {
    type NetflixContent = { title: string; description: string };

    const [data, setData] = useState<NetflixContent[]>([]);
    const router = useRouter();

    useEffect(() => {
        const fetchData = async () => {
            try {
                const res = await axiosInstance.get(`/netflix_id/${router.query.id}`);
                setData(res.data.data);
            } catch (err) {
                console.error(err);
            }
        };
    
        if (router.query.id) {
            fetchData();
        }
    }, [router.query.id]);

    return (
        <Container className={style.container}>
            {data.map((content, index) => (
                <Card key={index} className={style.netflixContent}>
                    <Card.Body>
                        <Card.Title>{content.title}</Card.Title>
                        <Card.Text>{content.description}</Card.Text>
                    </Card.Body>
                </Card>
            ))}
        </Container>
    );
}

export default NetflixId;