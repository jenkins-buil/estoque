import blogFetch from '../axios/config'
import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { useParams } from 'react-router-dom'

import "./NewPost.css"
const NewPost = () => {

  const { id } = useParams()

  const navigate = useNavigate()

  const [descricao, setDescricao] = useState()
  const [marca, setMarca] = useState()
  const categoria_id = id

  const createPost = async(e) => {
    e.preventDefault()
    
    await blogFetch.post("/produtos", {
      descricao,
      marca,
      categoria_id
    })
    navigate("/")
  }

  return (
    <div className='new-post'>
      <h2>Cadastro de Produtos </h2>
      <form onSubmit={(e) => createPost(e)}>
      <div className="form-control">
        <label htmlFor="marca-produto">Produto:</label>
        <input 
          type="text" 
          name='marca-produto' 
          id='marca-produto' 
          placeholder='Inserir nome do produto'
          onChange={(e) => setDescricao(e.target.value)}
        />
      </div>
      <div className="form-control">
        <label htmlFor="tamanho-produto">Marca:</label>
        <input 
          type="text" 
          name='tamanho-produto' 
          id='tamanho-produto' 
          placeholder='Inserir marca do produto'
          onChange={(e) => setMarca(e.target.value)}
        />
      </div>
      <input type="submit" value="Cadastrar" className='btn'/>
      </form>
    </div>
  )
}

export default NewPost