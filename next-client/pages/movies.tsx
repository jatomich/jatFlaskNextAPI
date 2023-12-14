// Description: This page displays the contents of the API that are of type MOVIE.

import React, { useEffect, useState } from 'react';
import Movie from '../components/Movie'; // Import your Movie component

function Movies() {
  const [movies, setMovies] = useState([]);

  useEffect(() => {
    // Fetch movies from your API
    getMovies().then((data) => {
      setMovies(data);
    });
  }, []);

  return (
    <div>
      {movies.map((movie, index) => (
        <Movie key={ index } movie={movie} /> // Render your Movie component for each movie
      ))}
    </div>
  );
}

async function getMovies() {
  // Replace with your actual API call
  const response = await fetch('https://api.example.com/movies');
  const data = await response.json();
  return data;
}

export default Movies;