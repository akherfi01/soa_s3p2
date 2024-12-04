import axios from 'axios';

// Backend base URL
const BASE_URL = 'http://localhost:5000/api';

export const api = axios.create({
  baseURL: BASE_URL,
});

