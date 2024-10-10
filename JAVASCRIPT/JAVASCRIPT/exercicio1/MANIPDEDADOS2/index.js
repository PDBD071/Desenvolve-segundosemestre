// Recupera as tarefas do localStorage ou inicializa um array vazio
let tarefas = JSON.parse(localStorage.getItem('tarefas')) || [];

// Função para renderizar a lista de tarefas
function renderizarTarefas() {
    const taskList = document.getElementById('taskList');
    taskList.innerHTML = ''; // Limpa a lista

    tarefas.forEach((tarefa, index) => {
        const div = document.createElement('div');
        div.className = 'task' + (tarefa.status ? ' completed' : '');

        // Checkbox para alterar o status da tarefa
        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.checked = tarefa.status;
        checkbox.addEventListener('change', () => {
            tarefa.status = checkbox.checked;
            localStorage.setItem('tarefas', JSON.stringify(tarefas));
            renderizarTarefas();
        });

        // Descrição da tarefa
        const descricao = document.createElement('span');
        descricao.textContent = tarefa.descricao;

        // Botão para excluir a tarefa
        const excluirBtn = document.createElement('button');
        excluirBtn.textContent = 'Excluir';
        excluirBtn.className = 'delete-button'; // Adiciona classe para estilo
        excluirBtn.addEventListener('click', () => {
            tarefas.splice(index, 1); // Remove a tarefa do array
            localStorage.setItem('tarefas', JSON.stringify(tarefas));
            renderizarTarefas();
        });

        div.appendChild(checkbox);
        div.appendChild(descricao);
        div.appendChild(excluirBtn);
        taskList.appendChild(div);
    });
}

// Adiciona uma nova tarefa
document.getElementById('addTaskButton').addEventListener('click', () => {
    const taskDescription = document.getElementById('taskDescription');
    const novaTarefa = {
        descricao: taskDescription.value,
        status: false // Status inicial como não concluído
    };

    if (taskDescription.value.trim() !== '') {
        tarefas.push(novaTarefa); // Adiciona a nova tarefa ao array
        localStorage.setItem('tarefas', JSON.stringify(tarefas)); // Atualiza o localStorage
        taskDescription.value = ''; // Limpa o campo de entrada
        renderizarTarefas(); // Renderiza a lista atualizada
    }
});

// Renderiza as tarefas ao carregar a página
renderizarTarefas();
