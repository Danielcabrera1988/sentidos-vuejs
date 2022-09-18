import axios from 'axios'

const getAPI = axios.create({
    baseURL: 'http://alexlopez.pythonanywhere.com'
})

export { getAPI }