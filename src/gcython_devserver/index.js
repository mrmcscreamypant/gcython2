import "https://www.desmos.com/api/v1.11/calculator.js?apiKey=8b3dceaf9fc446a38bf40c6e805cafd9";

const sleep = ms => new Promise(r => setTimeout(r, ms));
const elem = document.getElementById("calculator");

async function fetchLaTeX() {
    const response = await fetch("/latex");
    return response.json();
}

function pushLaTeX(latex, calculator) {
    calculator.setExpressions(
        latex.map(
            ltx => (
                { type: "expression", latex: ltx }
            )
        )
    );
}

async function go() {

    const latex = await fetchLaTeX();

    //await sleep(10);
    elem.innerHTML = "";
    const calculator = Desmos.GraphingCalculator(elem);
    pushLaTeX(latex, calculator);
}

go();