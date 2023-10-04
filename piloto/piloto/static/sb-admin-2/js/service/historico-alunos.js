(function( historicoAlunos ) {

    var nextPage = undefined;
    var previousPage = undefined;
    var currentPage = 1;

    historicoAlunos.alunos = [];
    historicoAlunos.count = undefined;

    historicoAlunos.load = async (url) => {
        let response = await fetch(`${url}?page=${currentPage}`);
        const data = await response.json();

        nextPage = data.next;
        previousPage = data.previous;
        historicoAlunos.count = data.count;
        historicoAlunos.alunos = data.results;

        return data;
    }

    historicoAlunos.loadNextPage = async () => {
        let response = await fetch(nextPage);
        const data = await response.json();

        nextPage = data.next;
        previousPage = data.previous;
        historicoAlunos.alunos = historicoAlunos.alunos.concat(data.results);

        return historicoAlunos.alunos;
    }

    historicoAlunos.hasNext = () => {
        return nextPage != undefined;
    }
}(window.historicoAlunos = window.historicoAlunos || {}));