// Funciones para operaciones de conjuntos
function performSetOperation(operation) {
    const setA = new Set(document.getElementById('setA').value.split(',').map(Number));
    const setB = new Set(document.getElementById('setB').value.split(',').map(Number));
    let result;

    switch (operation) {
        case 'union':
            result = [...new Set([...setA, ...setB])];
            break;
        case 'intersection':
            result = [...new Set([...setA].filter(x => setB.has(x)))];
            break;
        case 'difference':
            result = [...new Set([...setA].filter(x => !setB.has(x)))];
            break;
        default:
            result = [];
    }

    document.getElementById('set-result').innerText = `Resultado: { ${result.join(', ')} }`;
    buildBinaryTree(operation, setA, setB); // Llamamos a la función para construir el árbol binario
}

// Función para evaluar expresiones algebraicas
function evaluateExpression() {
    const expression = document.getElementById('expression').value;
    // Aquí podrías implementar una lógica más avanzada para evaluar la expresión algebraica
    document.getElementById('expression-result').innerText = `Expresión evaluada: ${expression}`;
}

// Función simple para construir un árbol binario basado en la operación
function buildBinaryTree(operation, setA, setB) {
    const treeExpression = `(${[...setA].join(', ')}) ${operation} (${[...setB].join(', ')})`;
    document.getElementById('tree-result').innerText = `Árbol Binario: ${treeExpression}`;
}
