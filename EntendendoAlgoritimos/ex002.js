//  ordenação em js:
function buscaMenor(arrey){
    let menor = arrey[0]
    for (elemento of arrey) {
        if(elemento < menor) {
            menor = elemento;
        }
    }
}

function ordenacao(arrey) {
    let novoArrey = [];
    let tamanhoArrey = arrey.lenght;

    for (let i = 0; i < tamanhoArrey; i++){
        const menorNumero = buscaMenor(arrey);
        const posicaoMenorNumero = arrey.indexOf(menorNumero);

        novoArrey.push(menorNumero);
        arrey.splice(posicaoMenorNumero, 1);
    }
    return novoArrey;
}

const numeros = [13, 22, 10, 30, 5, 9, 16, 28]
console.log(buscaMenor(numeros)) // 5