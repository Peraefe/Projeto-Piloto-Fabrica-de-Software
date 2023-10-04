// Call the dataTables jQuery plugin
(function( tabelaHistorico ) {
    var configurated = false;

    var listaAlunos = new Array();
    var gradeCurricular = new Map();
    var totalAlunos = undefined;
    
    var tableDiv = undefined;
    var table = undefined;
    var colunas = new Array();

    var alunosFiltrados = new Array() // rows
    
    var filtro = {
        periodoIdeal: "",
        situacaoDisciplina: "",
        anoIngresso: "",
        versaoPPC: "",
    };

    var sortTable = {
        state: 'disable',
        id: undefined,
        sortBy: undefined,
    };

    tabelaHistorico.disciplinaStatus = [
        {id: 0, label: 'Aprovado', isIn: (value) => value && value.situacao.aprovado, className: 'aprovado'},
        {id: 1, label: 'Matrícula', isIn: (value) => value && value.situacao.nome == 'Matrícula', className: 'matricula'},
        {id: 2, label: 'Reprovado', isIn: (value) => value && value.situacao.reprovado, className: 'reprovado'},
        {id: 3, label: 'Reprovado por Frequência', isIn: (value) => value && value.situacao.nome == 'Reprovado por Frequência', className: 'reprovado'},
        {id: 4, label: 'Reprovado com Dependência', isIn: (value) => value && value.situacao.nome != 'Reprovado por Frequência' && value.situacao.reprovado && value.mediaFinal >= 4.0, className: 'dependencia'},
        {id: 5, label: 'Não cursado', isIn: (value) => value == undefined, className: 'nao-cursado'},
    ];

    tabelaHistorico.alterarFiltro = (key, value) => {
        filtro[key] = value;
    };

    tabelaHistorico.getFiltro = (key) => {
        return filtro[key];
    }

    tabelaHistorico.initFiltro = ({periodoIdeal, situacaoDisciplina, anoIngresso, versaoPPC}) => {
        filtro.periodoIdeal = periodoIdeal;
        filtro.situacaoDisciplina = situacaoDisciplina;
        filtro.anoIngresso = anoIngresso;
        filtro.versaoPPC = versaoPPC;
    };

    tabelaHistorico.config = (element, alunos, disciplinas, total = undefined) => {
        tableDiv = element;
        gradeCurricular = disciplinas;
        listaAlunos = alunos;
        totalAlunos = total;
        configurated = true;
        
    }

    tabelaHistorico.criarTabela = () => {
        if (!configurated) {
            console.error('Tabela não configurada!!');
            return ;
        }

        alunosFiltrados = filtrarRegistros();

        if (sortTable.state != 'disable') {
            alunosFiltrados.sort((a, b) => {
                const a_value = getValuePath(sortTable.sortBy, a);
                const b_value = getValuePath(sortTable.sortBy, b);
                return sortTable.state == "desc" ? b_value.localeCompare(a_value) : a_value.localeCompare(b_value);
            });
        }

        table = document.createElement('table');
        table.className = "table table-hover table-sm table-bordered m-auto";
        table.append(createTableHead());
        table.append(createTableBody());
        table.append(createCaption());
    
        tableDiv.empty();
        tableDiv.append(table);
    }

    tabelaHistorico.updateAlunos = (alunos) => {
        listaAlunos = alunos;
        tabelaHistorico.criarTabela();
    }

    function createCaption() {
        const caption = document.createElement('caption');
        caption.className = 'text-right';
        caption.textContent = `${alunosFiltrados.length} alunos de ${listaAlunos.length}.`

        if (totalAlunos) {
            caption.textContent += ` Total de alunos no curso: ${totalAlunos}`;
        }

        return caption;
    }

    function createTableHead() {
        const thead = document.createElement('thead');
        const tr = document.createElement('tr');
    
        colunas = [
            {title: '#', tipo: 'count'},
            {title: 'Matricula', tipo: 'info', value: 'matricula', id: 'matricula'},
            {title: 'Nome Aluno', tipo: 'info', value: 'pessoa.nomeCompleto', id: 'nomeAluno'},
        ];

        if (filtro.periodoIdeal == 'all') {
            let disciplinas = []
            gradeCurricular.forEach((value) => {
                disciplinas = disciplinas.concat(value);
            })

            disciplinas.forEach((disciplina) => {
                colunas.push({title: disciplina.codigo, tipo: 'disciplina', tooltip: disciplina.nomeDisciplina})
            });
        } else {
            const periodo = parseInt(filtro.periodoIdeal);
            if (gradeCurricular.has(periodo)) {
                gradeCurricular.get(periodo).forEach((disciplina) => {
                    colunas.push({title: disciplina.codigo, tipo: 'disciplina', tooltip: disciplina.nomeDisciplina})
                });
            }
        }
        
        colunas.forEach((col) => {
            const th = document.createElement('th');
            th.scope = 'col';
            th.className = 'text-center';
            th.textContent = col.title;

            if (col.tipo == 'disciplina') {
                th.setAttribute('data-toggle', 'tooltip');
                th.setAttribute('title', col.tooltip);
            } else if (col.tipo == 'info') {
                th.className += ' sort-field';
                th.setAttribute('id', col.id);
                th.onclick = () => sortTableByColumn(col);
                th.append(createSortIcon(sortTable.id == col.id ? sortTable.state : 'disable'));
            }

            tr.append(th);
        })
        thead.append(tr);

        return thead;
    }

    function createTableBody() {
        const tbody = document.createElement('tbody');
        
        var index = 1;

        alunosFiltrados.forEach((aluno) => {
            const tr = document.createElement('tr');
    
            colunas.forEach((col) => {
                var tag;
    
                if (col.tipo == 'count') {
                    tag = document.createElement('th');
                    tag.scope = 'row';
                    tag.className = 'text-center';
                    tag.textContent = index;
                } else if (col.tipo == 'info') {
                    tag = document.createElement('td');
                    tag.textContent = getValuePath(col.value, aluno);
                } else if (col.tipo == 'disciplina') {
                    tag = document.createElement('td');
        
                    const histDisciplina = aluno.historico_escolar.find(obj => obj.disciplina.codigo === col.title);
                    const status = getDisciplinaStatus(histDisciplina);
            
                    tag.className = status.className;
                    if (histDisciplina && status.label != 'Reprovado por Frequência') {
                        tag.className += ` text-center`;
                        tag.textContent =  status.label == 'Matrícula' ? '-' : histDisciplina.mediaFinal;
                    }                    
            
                    tag.setAttribute('data-toggle', 'tooltip');
                    tag.setAttribute('title', `Status: ${status.label}`);
                }
    
                tr.append(tag);
            })
    
            tbody.append(tr);
            index++;
        });

        return tbody;
    }

    function sortTableByColumn(col) {
        const newColumn = sortTable.id != col.id;

        sortTable.id = col.id;
        sortTable.sortBy = col.value;

        colunas.filter(col => col.tipo == "info").forEach((col) => {
            var th = $(`#${col.id}`);
            th.empty();

            if (sortTable.id == col.id) {
                if (sortTable.state == 'disable' || newColumn) {
                    sortTable.state = 'asc';
                } else if (sortTable.state == 'asc') {
                    sortTable.state = 'desc';
                } else {
                    sortTable.state = 'disable';
                }
                th.append(createSortIcon(sortTable.state));
            } else {
                th.append(createSortIcon('disable'));
            }
        });

        tabelaHistorico.criarTabela();
    }

    function createSortIcon(state) {
        const icon = document.createElement('i');
        if (state == 'asc') {
            icon.className = 'ml-2 fas fa-sort-amount-down-alt';
        } else if (state == 'desc') {
            icon.className = 'ml-2 fas fa-sort-amount-down';
        } else {
            icon.className = 'ml-2 fas fa-sort';
        }
        return icon;
    }

    function filtrarRegistros() {
        var alunosFiltrados = JSON.parse(JSON.stringify(listaAlunos));
        var { anoIngresso, periodoIdeal, situacaoDisciplina, versaoPPC } = filtro;

        if (versaoPPC != "") {
            alunosFiltrados = alunosFiltrados.filter((aluno) => aluno.ppc.id == versaoPPC)
        }
        if (anoIngresso != "") {
            alunosFiltrados = alunosFiltrados.filter((aluno) => aluno.anoIngresso == anoIngresso);
        }
        if (periodoIdeal != "") {
            var disciplinas_periodo = new Array();

            if (periodoIdeal == 'all') {
                gradeCurricular.forEach((value) => {
                    disciplinas_periodo = disciplinas_periodo.concat(value);
                })
            } else {
                const periodo = parseInt(periodoIdeal);
                disciplinas_periodo = gradeCurricular.get(periodo);
            }

            if (disciplinas_periodo) {
                alunosFiltrados.forEach((aluno) => {
                    const historico = new Array();
    
                    disciplinas_periodo.forEach((value) => {
                        const found = aluno.historico_escolar.find(({disciplina}) => disciplina.codigo && disciplina.codigo == value.codigo);
                        if (found != undefined) {
                            historico.push(found);
                        }
                    })
                    aluno.historico_escolar = historico;
                });
            }
        }
        if (situacaoDisciplina != "") {
            if (situacaoDisciplina == 5) { // Não Cursado
                alunosFiltrados = alunosFiltrados.filter((aluno) => aluno.historico_escolar.length == 0);
            } else {
                const status = tabelaHistorico.disciplinaStatus[parseInt(situacaoDisciplina)];
                alunosFiltrados = alunosFiltrados.filter((aluno) => {
                    var historico = aluno.historico_escolar.filter((value) => status.isIn(value));
                    return historico.length > 0;
                });
            }
        }

        return alunosFiltrados;
    }

    var getValuePath = (path, obj) => path.split('.').reduce((p,c)=>p&&p[c]||null, obj);

    function getDisciplinaStatus(histDisciplina) {
        var result;
        tabelaHistorico.disciplinaStatus.forEach((status) => {
            if (status.isIn(histDisciplina)) {
                result = status;
            }
        });
        return result;
    }
}(window.tabelaHistorico = window.tabelaHistorico || {}));
