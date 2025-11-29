% rebase('layout.tpl', title=('Editar Hábito' if habit else 'Novo Hábito'))

<h1>{{ 'Editar Hábito' if habit else 'Novo Hábito' }}</h1>

<form action="{{action}}" method="post">

    <label>Nome:<br>
        <input type="text" name="name" value="{{habit.name if habit else ''}}" required>
    </label><br><br>

    <label>Descrição:<br>
        <textarea name="description" required>{{habit.description if habit else ''}}</textarea>
    </label><br><br>

    <label>Frequência:<br> 
        <select name="frequency" required>
            % for f in ['Diario', 'Semanal', 'Quinzenal', 'Mensal', 'Bimestral', 'Trimestral', 'Semestral', 'Anual']:
                <option value="{{f}}" {{'selected' if habit and habit.frequency == f else ''}}>
                    {{ 'Diário' if f=='Diario' else 'Semanal' if f=='Semanal' else 'Quinzenal' if f=='Quinzenal' else 'Mensal' if f=='Mensal' else 'Bimestral' if f=='Bimestral' else 'Trimestral' if f=='Trimestral' else 'Semestral' if f=='Semestral' else 'Anual' if f=='Anual' else ''}}
                </option>
            % end
        </select>
    </label><br><br>

    <button type="submit">Salvar</button>

</form>

<a href="/dashboard">Voltar</a>