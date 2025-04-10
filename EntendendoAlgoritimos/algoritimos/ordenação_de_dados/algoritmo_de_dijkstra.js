//  o algoritio de Dijkstra é basicamete deva em conta "pesos" para atingir determinado camonho.
//  ps1 ele não finciona com pesos negativos: O algoritno de bellman-Ford é o mais comum para caminhos com pesosas negativos.

let grafo = {};

grafo['inicio'] = {};
grafo['inicio']['a'] = 6;
grafo['inicio']['b'] = 1;

grafo['a'] = {};
grafo['a']['fim'] = 1;

grafo['b'] = {};
grafo['a']['b'] = 3;
grafo['b']['fim'] = 5;

grafo['fim'] = {};

const infinito = Number.POSITIVE_INFINITY; // define infinito em JS

let custo = {};
custo['a'] = 6;
custo['b'] = 2;
custo['fim'] = infinito;

console.log(grafo['inicio']['a']);

let pais = {};
pais['a'] = 'inicio';
pais['b'] = 'inicio';
pais['fim'] = null;

const processados = {}

let custos = [];
custos['a'] = 6;
custos['b'] = 2;
custos['fim'] = infinito;

print(grafo['inicio']['a']);

let pais = [];
pais['a'] = 'inicio';
pais['b'] = 'inicio';
pais['fim'] = null

const no = ache_no_custo_mais_baixo(custo);

while (nó){
    let custo = custos[nó]
    let vizinhos = grafo[nó]

    for (n in vizinhos.keys()){

        novo_custo = custo + vizinhos[n]
        if (custos[n] > novo_custo){
            custos[n] = novo_custo
            pais[n] = nó
        }
    }
}

function ache_no_custo_mais_baixo (custos) {
    let custo_mais_baixo = Infinity
    let no_mais_baixo = null
    
    for (let node of object.keys(custos)) {
        if (custos[node] < custo_mais_baixo && !processados.includes(node)) {
            custo_mais_baixo = custos[node]
            no_mais_baixo = node
        }
    }
    return no_mais_baixo 
}