% rebase('layout.tpl', title='Usuários')

<h1>Usuários</h1>
<a href="/users/add">Adicionar Usuário</a>

<table border="1">
    <tr>
        <th>ID</th>
        <th>Nome</th>
        <th>Email</th>
        <th>Criado em</th>
        <th>Ações</th>
    </tr>

    % for u in users:
    <tr>
        <td>{{u.id}}</td>
        <td>{{u.username}}</td>
        <td>{{u.email}}</td>
        <td>{{u.created_at}}</td>
        <td>
            <a href="/users/edit/{{u.id}}">Editar</a>
            <form action="/users/delete/{{u.id}}" method="post" style="display:inline;">
                <button type="submit">Excluir</button>
            </form>
        </td>
    </tr>
    % end
</table>
