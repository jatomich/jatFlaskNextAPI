// Description: This page displays the contents of the API.
// Author: Andrew Tomich

// The API is fetched on the client side.

import React, { useEffect, useState } from 'react'
import axiosInstance from '../utils/axios'

/**
 * Renders the test_api page component.
 * Fetches data from the API and displays a loading message until the data is fetched.
 */
function test_api() {

  const [data, setData] = useState<string>("Loading...");

  useEffect(() => {
    axiosInstance.get("health").then(
      res => res.data
    ).then((data) => {
        setData(data.data);
  });
  }, []);

  return (
    <div>{ data }</div>
  )
}

export default test_api