import axios from "axios";

const getAPI = axios.create({
  //baseURL: "https://alexlopez.pythonanywhere.com",
  //baseUrl: "https://bynarySystem.pythonanywhere.com"
  baseUrl: "https://binarysystem.pythonanywhere.com",
});

export {getAPI};
