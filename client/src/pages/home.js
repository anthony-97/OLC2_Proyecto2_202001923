import React from 'react';
import { useState } from 'react';
import { InputTextarea } from 'primereact/inputtextarea';
import { Button } from 'primereact/button';
import { PostMethod } from '../api/http';
import { GetMethod } from '../api/http';


const interpreterAPI = process.env.REACT_APP_API_URL_INTERPRETER;

const Home = () => {

    const [codeText, setCodeText] = useState('')
    const [consoleText, setConsoleText] = useState('')
    var errores = ""
    
    const CompileInterpreter = async() => {
        const resp = await PostMethod(interpreterAPI+'interpreter', { code: codeText })
        await setConsoleText(resp?.console)
        errores = resp?.errores
    }

    //Leyendo archivos y poniendolos en la entrada
    const handleFileChange = (event) => {
        const file = event.target.files[0];
        const reader = new FileReader();
    
        reader.onload = (e) => {
          const content = e.target.result;
          setCodeText(content);
        };
        reader.readAsText(file);
      };

    const generarReportes = async () => {
        try {
            // Llama al endpoint de reportes
            const resp = await GetMethod(interpreterAPI+'reportes');
            // Actualiza el estado de consoleText con el mensaje deseado
            setConsoleText("Reportes generados exitosamente");
        } catch (error) {
            console.error("Error al generar reportes:", error);
        }
    };

    return (
        <div>
            <div style={{display: 'flex', marginTop: '5%'}}>
                <InputTextarea value={codeText} rows={18} cols={60} style={{marginBottom: '5%', marginRight: '2%'}} onChange={e => {setCodeText(e.target.value)}}/>
                <InputTextarea value={consoleText} rows={18} cols={60} style={{marginBottom: '5%', marginLeft: '2%'}} onChange={e => {setConsoleText(e.target.value)}}/>
            </div>
            <div style={{display: 'flex', marginBottom: '3%', justifyContent: 'center'}}>
                <input type="file" onChange={handleFileChange}/>
            </div>
            <div style={{display: 'flex', marginBottom: '3%', justifyContent: 'center'}}>
                <Button label="Interpretar" onClick={CompileInterpreter} style={{marginRight: '2%'}}/>
                <Button label="Generar reportes" onClick={generarReportes} style={{marginRight: '2%'}}/>
            </div>
        </div>
    );
};

export default Home;
