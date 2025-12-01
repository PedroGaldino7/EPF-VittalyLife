% rebase('layout.tpl', title=('Editar Hábito' if habit else 'Novo Hábito'))
<link rel="stylesheet" href="../static/css/stylePages.css">

<div class="container-page">

    <h1>{{ 'Editar Hábito' if habit else 'Criar Novo Hábito' }}</h1>

    <form action="{{action}}" method="post">

        <label>Nome:</label>
        <input type="text" name="name" value="{{habit.name if habit else ''}}" required>

        <label>Descrição:</label>
        <textarea name="description" required>{{habit.description if habit else ''}}</textarea>

        <label>Frequência:</label>
        <select name="frequency" required>
            % for f in ['Diario', 'Semanal', 'Quinzenal', 'Mensal', 'Bimestral', 'Trimestral', 'Semestral', 'Anual']:
                <option value="{{f}}" {{'selected' if habit and habit.frequency == f else ''}}>
                    {{'Diário' if f=='Diario' else 'Semanal' if f=='Semanal' else 'Quinzenal' if f=='Quinzenal' else 'Mensal' if f=='Mensal' else 'Bimestral' if f=='Bimestral' else 'Trimestral' if f=='Trimestral' else 'Semestral' if f=='Semestral' else 'Anual' if f=='Anual' else ''}}
                </option>
            % end
        </select>

        <button class="btn btn-success" type="submit">Salvar</button>
    </form>

    <br>
    <a class="btn" href="/dashboard">Voltar</a>

</div>
