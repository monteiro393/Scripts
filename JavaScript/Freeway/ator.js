// variáveis do Ator
let xAtor = 100
let yAtor = 366
let colisao = false
let meusPontos = 0

// tamanho do ator
function ator(){
  image(imagemAtor, xAtor, yAtor, 30, 30)
}

// movimento do ator
function movimentoAtor(){
  if (keyIsDown(UP_ARROW)){
    yAtor -= 3
  }
  if (keyIsDown(DOWN_ARROW) && yAtor < 366){
    yAtor += 3
  }
// if (keyIsDown(LEFT_ARROW)){ xAtor -= 3 }
// if (keyIsDown(RIGHT_ARROW)){ xAtor += 3 }
}

function posicaoInicialAtor(){
  if (yAtor < 3){
    yAtor = 366
  }
}

function verificarColisao(){
  // collideRectCircle(x1, y1, width1, height1, cx, cy, diameter)
  for (let i = 0; i < imagemCarros.length; i++){
    colisao = collideRectCircle(xCarros[i], yCarros[i], wCarros, hCarros, xAtor, yAtor, 10)
    if (colisao){
      colidiu()
    }
  }
}

function colidiu(){
  yAtor = 366
  if (pontosMaiorQueZero()){
    meusPontos -= 1
  }
}

function incluiPontos(){
  textAlign(CENTER)
  textSize(25)
  fill(color(255, 140, 0))
  stroke(0)
  text(meusPontos, width / 3, 27)
}

function marcaPonto(){
  if (yAtor < 4){
    meusPontos += 1
  }
}

function pontosMaiorQueZero(){
  return meusPontos > 0
}