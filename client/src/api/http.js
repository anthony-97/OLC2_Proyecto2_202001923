import axios from 'axios';

export const PostMethod = async (url, data) => {
    try {
        const response = await axios.post(`${url}`, data);
        return response.data
    } catch (error) {
        console.error('Error en la solicitud:', error);
    }
}

export const GetMethod = async (url) => {
    try {
        const response = await axios.get(url);
        return response.data;
    } catch (error) {
        console.error('Error en la solicitud:', error);
        throw error; // Si quieres propagar el error para manejarlo en el componente que realiza la llamada
    }
}