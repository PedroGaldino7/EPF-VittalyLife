% rebase('layout.tpl', title='Usuários')
<link rel="stylesheet" href="../static/css/stylePages.css">

<div class="container-page">

    <h1>Gerenciar Usuários</h1>

    <a class="btn btn-success" href="/users/add">+ Adicionar Usuário</a>
    <br><br>

    <table class="table">
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
                % if u.is_admin == True:
                    <span style="color:#ffd700; font-weight:600;">👑 Administrador</span>
                % else:
                    <a class="btn" href="/users/edit/{{u.id}}">Editar</a>

                    <form action="/users/delete/{{u.id}}" method="post" style="display:inline;">
                        <button class="btn btn-danger" type="submit">Excluir</button>
                    </form>
                % end
            </td>

        </tr>
        % end
    </table>

    <br>
    <a class="btn" href="/dashboard">Voltar</a>

</div>
