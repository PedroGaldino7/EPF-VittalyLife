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
            % for f in ['daily', 'weekly', 'custom']:
                <option value="{{f}}" {{'selected' if habit and habit.frequency == f else ''}}>
                    {{ 'Diário' if f=='daily' else 'Semanal' if f=='weekly' else 'Personalizado' }}
                </option>
            % end
        </select>
    </label><br><br>

    <label>
        <input type="checkbox" name="active" {{'checked' if habit and habit.active else ''}}>
        Hábito Ativo?
    </label><br><br>

    <button type="submit">Salvar</button>

</form>

<a href="/dashboard">Voltar</a>