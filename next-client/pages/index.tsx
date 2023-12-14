// Description: This page displays the contents of the API.
// Author: Andrew Tomich

// The API is fetched on the client side.

import React, { useEffect, useState } from 'react'

/**
 * Renders the test_api page component.
 * Fetches data from the API and displays a loading message until the data is fetched.
 */
function test_api() {

  const [message, setMessage] = useState<string>("Loading...");

  useEffect(() => {
    fetch("http://127.0.0.1:8080/api/test").then(
      res => res.json()
    ).then((data) => {
        setMessage(data.message);
  });
  }, []);

  return (
    <div>{ message }</div>
  )
}

export default test_api