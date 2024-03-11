import blogFetch from "../axios/config"
import { useState, useEffect } from "react"
import { useParams } from "react-router-dom"
import "./Entradas.css"



const Entradas = () => {
    const { id } = useParams()

    const [entrada, setEntrada] = useState([])

    const getEntrada = async() => {
      try {
        const response = await blogFetch.get(`/entradas/${id}`)                                       
        const data = await response.data
        setEntrada(data)
        console.log(await data[0])
        
      } catch (error) {
        console.log(error)
      }
    }
  
    useEffect(() => {
      getEntrada()
    }, [])


  return (
    <div className="container">
        <table>
        <thead>
            <h2>Histórico de entrada</h2><br />
            <tr>
                <th>Data Entrada</th>
                <th>Hora de Entrada</th>
                <th>Tamanho</th>
                <th>Cor</th>
                <th>Quantidade</th>
                <th>id Produto</th>
            </tr>
        </thead>
        <tbody>
          {entrada.map(item => (
            <tr key={item.id} className="item">
              <td>{item.data_entrada}</td>
              <td>{item.hora_entrada}</td>
              <td>{item.tamanho}</td>
              <td>{item.cor}</td>
              <td>{item.quantidade}</td>
              <td>{item.produto_id}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>  
  )
}

export default Entradas