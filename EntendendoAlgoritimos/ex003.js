// recursividade
function contagemRegresiva(num) {
    console.log(num)
    if(num < 1){
        return
    }else{
        contagemRegresiva(num - 1)
    }
}

contagemRegresiva(1000)