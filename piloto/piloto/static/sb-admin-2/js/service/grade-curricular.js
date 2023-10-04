(function( gradeCurricular ) {
    
    gradeCurricular.periodos = new Map();
    gradeCurricular.disciplinas = new Array();

    gradeCurricular.load = async (url) => {
        var response = await fetch(url);
        response = await response.json();
        
        let disciplinas = new Map();
        let periodos = new Array();
        response.forEach((value) => {
            if (disciplinas.has(value.periodoIdeal)) {
                disciplinas.get(value.periodoIdeal).push(value);
            } else {
                periodos.push(value.periodoIdeal);
                disciplinas.set(value.periodoIdeal, [value]);
            }
        });

        periodos.forEach((periodo) => {
            disciplinas.get(periodo).sort((a,b) => a.codigo > b.codigo ? 1 : -1);
        })

        gradeCurricular.periodos = periodos;
        gradeCurricular.disciplinas = disciplinas;
        
        return {periodos, disciplinas};
    }
}(window.gradeCurricular = window.gradeCurricular || {}));