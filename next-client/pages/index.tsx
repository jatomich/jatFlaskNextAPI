import React, { useEffect, useState } from 'react'

function index() {

  useEffect(() => {
    fetch("http://127.0.0.1:8080/api/contents").then(
      res => res.json()
    ).then((data) => {
        console.log(data);
  });
  }, []);

  return (
    <div>index</div>
  )
}

export default index