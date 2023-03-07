// variáveis dos carros
let xCarros = [500, 500, 500, -60, -60, -60]
let yCarros = [45, 97, 151, 210, 270, 318]
let wCarros = 55
let hCarros = 35
let velocidadeCarros = [2, 3, 2.5, -5, -2.3, -2.8]

// tamanho dos carros
function mostraCarro(){
  for (let i = 0; i < imagemCarros.length; i++){
  image(imagemCarros[i], xCarros[i], yCarros[i], wCarros, hCarros)
  }
}

// movimento dos carros
function movimentoCarro(){
  for (let i = 0; i < xCarros.length; i++){
  xCarros[i] -= velocidadeCarros[i]
  }
}

function posicaoInicialCarro(){
  for (let i = 0; i < xCarros.length; i++){
    if (xCarros[i] < -50){
      xCarros[i] = 500
    }
  else {
    if (xCarros[i] > 500){
      xCarros[i] = -50
      }
    }
  }
}