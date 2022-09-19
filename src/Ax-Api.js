import axios from "axios";

const getAPI = axios.create({
  baseURL: "https://alexlopez.pythonanywhere.com",
});

export { getAPI };
