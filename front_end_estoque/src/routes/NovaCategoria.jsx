import blogFetch from '../axios/config'
import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import "./NovaCategoria.css"

const NovaCategoria = () => {

    const navigate = useNavigate()

  const [categoria, setCategoria] = useState()
  
  const createPostCategoria = async(e) => {
    e.preventDefault()
    
    await blogFetch.post("/categorias", {
      categoria
    })
    navigate("/categorias")
  }

  return (
    <div className='new-post'>
      <h2>Cadastro de Categorias</h2>
      <form onSubmit={(e) => createPostCategoria(e)}>
      <div className="form-control" id='container_categoria'>
        <label htmlFor="marca-produto" >Categoria:</label>
        <input 
          type="text" 
          name='marca-produto' 
          id='marca-produto' 
          placeholder='Inserir nome categoria'
          onChange={(e) => setCategoria(e.target.value)}
        />
      </div>
      <input type="submit" value="Cadastrar" className='btn'/>
      </form>
    </div>
  )
}

export default NovaCategoria