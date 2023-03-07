// variáveis da bolinha 
let xBolinha = 350
let yBolinha = 250
let diametro = 20
let raio = diametro / 2

// OU = ||
// E = &&

// velocidade da bolinha
let velocidadexBolinha = 7
let velocidadeyBolinha = 7

// variáveis da minha raquete
let xRaquete = 5
let yRaquete = 210

// variáveis do oponente
let xRaqueteOponente = 685
let yRaqueteOponente = 210
let velocidadeyOponente

let wRaquete = 8
let hRaquete = 70

// placar do jogo
let meusPontos = 0
let oponentePontos = 0

// sons do jogo
let raquetada
let ponto

function preload(){
  raquetada = loadSound('Sons/raquetada.mp3')
  ponto = loadSound('Sons/ponto.mp3')
}

function setup() {
  createCanvas(700, 500)
}

function draw() {
  background(0)
  
  placar()
  marcaPonto()
  
  linhas()
  
  bolinha()
  
  movimentoBolinha()
  colisaoBolinhaBorda()
  
  colisaoRaquete()
  colisaoRaqueteOponente()
  
  Raquete(xRaquete, yRaquete)
  Raquete(xRaqueteOponente, yRaqueteOponente)
  movimentoMinhaRaquete()
  movimentoRaqueteOponente()
}

// propriedades das funções em draw

// linhas
function linhas(){
  fill(255)
  rect(349, 0, 1, 500)
} 

// bolinha
function bolinha(){
  circle(xBolinha, yBolinha, diametro)
}

function movimentoBolinha(){
  xBolinha += velocidadexBolinha
  yBolinha += velocidadeyBolinha
}

function colisaoBolinhaBorda(){
    if (xBolinha + raio > width || xBolinha - raio < 0){
    velocidadexBolinha *= -1
  }
  
  if (yBolinha + raio > height || yBolinha - raio < 0){
    velocidadeyBolinha *= -1
  }
}

//raquetes
function Raquete(x, y){
  rect( x, y, wRaquete, hRaquete, 20)
}

function movimentoMinhaRaquete(){
  if (keyIsDown(UP_ARROW) && yRaquete > 10){
    yRaquete -= 9
  }
  
  if (keyIsDown(DOWN_ARROW) && yRaquete < 420){
    yRaquete += 9
  }
}

function movimentoRaqueteOponente(){
  velocidadeyOponente = yBolinha - yRaqueteOponente - wRaquete / 2 - 69
  yRaqueteOponente += velocidadeyOponente
}

// colisões
function colisaoRaquete(){
  if (xBolinha - raio < xRaquete + wRaquete
  &&  yBolinha - raio < yRaquete + hRaquete
  &&  yBolinha + raio > yRaquete){
    velocidadexBolinha *= -1
    raquetada.play()
  }
}

function colisaoRaqueteOponente(){
  if (xBolinha + raio > xRaqueteOponente 
  &&  yBolinha - raio < yRaqueteOponente + hRaquete 
  &&  yBolinha + raio > yRaqueteOponente){
    velocidadexBolinha *= -1
    raquetada.play()
  }
}

// placar
function placar(){
  textAlign(CENTER)
  textSize(16)
  stroke(200)
  fill(color("#E19600"))
  rect(260, 10, 40, 20, 20)
  rect(400, 10, 40, 20, 20)
  fill(255)
  text(meusPontos, 280, 25)
  text(oponentePontos, 420, 25)
}

function marcaPonto(){
  if (xBolinha > 690){
    meusPontos += 1
    ponto.play()
  }
  if (xBolinha < 10){
    oponentePontos += 1
    ponto.play()
  }
}