import React from 'react';
import Head from 'next/head';
import Link from 'next/link';

const Home: React.FC = () => {
  return (
    <div>
      <Head>
        <title>Home Page</title>
        <meta name="description" content="Welcome to the home page" />
      </Head>

      <h1>Welcome to the Home Page</h1>

      <p>This is a simple Next.js application.</p>

      <Link href="/netflix">
        <p>Go to Netflix page</p>
      </Link>
      <hr />
      <Link href="/netflix_movies">
        <p>Go to Netflix Movies page</p>
      </Link>
    </div>
  );
};

export default Home;