import { useState, useEffect } from 'react';
import axiosInstance from '../utils/axios';

import '../types/SampleData';

import Container from 'react-bootstrap/Container';
import Card from 'react-bootstrap/Card';
import style from './netflix.module.css';

function Sample() {

    const [results, setResults] = useState<SampleData[]>([])

    useEffect(() => {
        const fetchData = async () => {
            try {
                const res = await axiosInstance.get('/sample');
                setResults(res.data);
                console.log(res.data)
            } catch (err) {
                console.error(err);
            }
        };

        fetchData();
    }, []);

    return (
        <div>
            {results && results.map((result, index) => (
           <Container key={index}>
           <Card className={style.container}>
             <Card.Body className={style.netflixContent}>
               <Card.Title>{result.LastName}, {result.FirstName}</Card.Title>
               <Card.Text>{result.EmailAddress}</Card.Text>
               <Card.Text>{result.City}, {result.StateProvince}</Card.Text>
             </Card.Body>
           </Card>
         </Container>
            ))}
        </div>
    );
}

export default Sample;
