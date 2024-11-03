### README (Portuguese)

## Descrição

EisenhowerMatrixApp é uma aplicação em Python com interface gráfica (GUI) criada com PySide6, que permite ao usuário organizar tarefas em uma matriz de Eisenhower. A matriz é dividida em quatro quadrantes: Importante e Urgente, Importante, mas Não Urgente, Não Importante, mas Urgente, e Não Importante e Não Urgente. O aplicativo permite adicionar, remover e salvar tarefas em cada quadrante.

## Funcionalidades
- **Adicionar Tarefa**: Adiciona uma nova tarefa a um dos quatro quadrantes.
- **Remover Tarefa**: Remove uma tarefa ao clicar duas vezes sobre ela.
- **Salvar Tarefas**: Salva as tarefas em um arquivo JSON.
- **Carregar Tarefas**: Carrega as tarefas salvas de um arquivo JSON.

## Tecnologias Utilizadas
- **Python 3.13**
- **PySide6**: Interface gráfica.

## Instalação
1. Clone o repositório:
    ```bash
    git clone https://github.com/fernandoncidade/eisenhower_organizing
    cd File_Manager
    ```
2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Uso
1. **Execute o aplicativo**:
    ```bash
    python eisenhower_organizing_v001.py
    ```
2. **Adicione uma tarefa**:
    - Digite a tarefa no campo de entrada.
    - Selecione o quadrante apropriado no menu suspenso.
    - Clique no botão "Adicionar Tarefa".
3. **Remova uma tarefa**:
    - Clique duas vezes na tarefa que deseja remover.
    - Confirme a remoção na caixa de diálogo que aparece.

## Estrutura do Código
A classe EisenhowerMatrixApp possui as seguintes funcionalidades principais:

### Funções Core
- **__init__()**: Inicializa a janela principal e carrega as tarefas salvas.
- **initUI()**: Configura a interface do usuário, incluindo os campos de entrada e os quadrantes.
- **`add_placeholder(list_widget, text)`**: Adiciona um item de espaço reservado a um quadrante.
- **add_task()**: Adiciona uma nova tarefa ao quadrante selecionado.
- **`remove_task(item, list_widget)`**: Remove uma tarefa ao clicar duas vezes sobre ela.
- **save_tasks()**: Salva as tarefas em um arquivo JSON.
- **load_tasks()**: Carrega as tarefas salvas de um arquivo JSON.

## Exemplo de Código
```python
# Inicia a aplicação
app = QApplication(sys.argv)
window = EisenhowerMatrixApp()
window.show()
sys.exit(app.exec())
```

## Dependências
- PySide6
- json
- sys


____________________________________________________________________



### README (English)

## Description

EisenhowerMatrixApp is a Python application with a graphical user interface (GUI) created with PySide6, which allows the user to organize tasks in an Eisenhower matrix. The matrix is divided into four quadrants: Important and Urgent, Important but Not Urgent, Not Important but Urgent, and Not Important and Not Urgent. The application allows adding, removing, and saving tasks in each quadrant.

## Features
- **Add Task**: Adds a new task to one of the four quadrants.
- **Remove Task**: Removes a task by double-clicking on it.
- **Save Tasks**: Saves tasks to a JSON file.
- **Load Tasks**: Loads tasks from a saved JSON file.

## Technologies Used
- **Python 3.13**
- **PySide6**: Graphical interface.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/fernandoncidade/eisenhower_organizing
    cd File_Manager
    ```
2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. **Run the application**:
    ```bash
    python eisenhower_organizing_v001.py
    ```
2. **Add a task**:
    - Enter the task in the input field.
    - Select the appropriate quadrant from the dropdown menu.
    - Click the "Add Task" button.
3. **Remove a task**:
    - Double-click on the task you want to remove.
    - Confirm the removal in the dialog box that appears.

## Code Structure
The EisenhowerMatrixApp class has the following main functionalities:

### Core Functions
- **__init__()**: Initializes the main window and loads saved tasks.
- **initUI()**: Sets up the user interface, including input fields and quadrants.
- **`add_placeholder(list_widget, text)`**: Adds a placeholder item to a quadrant.
- **add_task()**: Adds a new task to the selected quadrant.
- **`remove_task(item, list_widget)`**: Removes a task by double-clicking on it.
- **save_tasks()**: Saves tasks to a JSON file.
- **load_tasks()**: Loads tasks from a saved JSON file.

## Code Example
```python
# Start the application
app = QApplication(sys.argv)
window = EisenhowerMatrixApp()
window.show()
sys.exit(app.exec())
```

## Dependencies
- PySide6
- json
- sys
