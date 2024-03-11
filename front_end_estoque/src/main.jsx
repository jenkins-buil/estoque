import Home from './routes/Home'
import NewPost from './routes/NewPost'
import Categoria from './routes/Categoria'
import Entradas from './routes/Entradas'
import NovaCategoria from './routes/NovaCategoria'
import Post from './routes/Post'
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import { createBrowserRouter, RouterProvider, Route } from 'react-router-dom'
import './index.css'

const router = createBrowserRouter([
  {
    element: <App />,
    children: [
      {
        path: "/",
        element: <Home />
      },
      {
        path: "/new/:id",
        element: <NewPost />
      },
      {
        path: "/produtos/:id",
        element: <Post />
      },
      {
        path: "/categorias",
        element: <Categoria />
      },
      {
        path: "/entradas/:id",
        element: <Entradas />
      }, 
      {
        path: "nova_categoria",
        element: <NovaCategoria />
      }
    ]
  }
])



ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
)
