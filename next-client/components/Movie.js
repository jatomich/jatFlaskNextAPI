import React, { useEffect, useState } from 'react';
import axiosInstance from '../utils/axios';

function Movie() {
  const [movies, setMovies] = useState([]);

  useEffect(() => {
    fetchMovies();
  }, []);

  const fetchMovies = async () => {
    const response = await axiosInstance.get('/api/netflix');
    const data = await response.json();
    const movies = data.filter(item => item.type === 'Movie');
    setMovies(movies);
  };

  return (
    <div>
      {movies.map((movie) => (
        <div key={movie.id}>
          <h2>{movie.title}</h2>
          <p>{movie.description}</p>
        </div>
      ))}
    </div>
  );
}

export default Movie;