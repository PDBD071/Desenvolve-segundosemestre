// Array de objetos Tarefa
const tasks = [];

// Função para renderizar a lista de tarefas
function renderTasks() {
    const taskList = document.getElementById('taskList');
    taskList.innerHTML = ''; // Limpa a lista atual
    tasks.forEach((task, index) => {
        const taskDiv = document.createElement('div');
        taskDiv.classList.add('task');
        if (task.status) {
            taskDiv.classList.add('completed');
        }

        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.checked = task.status;
        checkbox.addEventListener('change', () => {
            task.status = checkbox.checked; // Atualiza o status da tarefa
            renderTasks(); // Re-renderiza a lista
        });

        taskDiv.appendChild(checkbox);
        taskDiv.appendChild(document.createTextNode(task.description));
        taskList.appendChild(taskDiv);
    });
}

// Evento para adicionar uma nova tarefa
document.getElementById('addTaskButton').addEventListener('click', () => {
    const taskDescription = document.getElementById('taskDescription').value;
    if (taskDescription.trim()) {
        const newTask = {
            description: taskDescription,
            status: false // Inicializa o status como não concluído
        };
        tasks.push(newTask); // Adiciona a nova tarefa ao array
        document.getElementById('taskDescription').value = ''; // Limpa o campo de texto
        renderTasks(); // Re-renderiza a lista
    } else {
        alert('Por favor, insira uma descrição para a tarefa.');
    }
});

// Renderiza a lista inicialmente
renderTasks();
