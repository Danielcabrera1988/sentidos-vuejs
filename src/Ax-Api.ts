import axios from "axios";

const getAPI = axios.create({
  baseURL: "https://binarysystem.pythonanywhere.com",
});

export {getAPI};
