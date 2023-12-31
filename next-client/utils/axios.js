// This file creates and exports an Axios instance with some default values

import axios from 'axios';

/**
 * Axios instance for making HTTP requests.
 * @type {import("axios").AxiosInstance}
 */
const axiosInstance = axios.create({
    baseURL: 'http://127.0.0.1:8080',   // Base URL of the API server
    timeout: 20000,                      // Timeout of 20 seconds
    headers: {                          // Headers
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
});

export default axiosInstance;