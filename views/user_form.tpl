% rebase('layout.tpl', title=('Editar Usuário' if user else 'Novo Usuário'))

<h1>{{ 'Editar Usuário' if user else 'Novo Usuário' }}</h1>

<form action="{{action}}" method="post">

    <label>Nome:<br>
        <input type="text" name="name" value="{{user.name if user else ''}}" required>
    </label><br><br>

    <label>Email:<br>
        <input type="email" name="email" value="{{user.email if user else ''}}" required>
    </label><br><br>

    <label>Senha:<br>
        <input type="password" name="password" placeholder="Nova senha...">
    </label><br><br>

    <button type="submit">Salvar</button>

</form>

<a href="/users">Voltar</a>
