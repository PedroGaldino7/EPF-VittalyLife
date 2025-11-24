% rebase('layout.tpl', title='Hábitos')

<h1>Hábitos</h1>

<table border="1">
    <tr>
        <th>ID</th>
        <th>Nome</th>
        <th>Descrição</th>
        <th>Frequência</th>
        <th>Ativo?</th>
        <th>Ações</th>
    </tr>

    % for h in habits:
    <tr>
        <td>{{h.id}}</td>
        <td>{{h.name}}</td>
        <td>{{h.description}}</td>
        <td>{{h.frequency}}</td>
        <td>{{'Sim' if h.active else 'Não'}}</td>
        <td>
            <a href="/habits/edit/{{h.id}}">Editar</a>
            <form action="/habits/delete/{{h.id}}" method="post" style="display:inline;">
                <button type="submit">Excluir</button>
            </form>
        </td>
    </tr>
    % end
</table>

<p><a href="/dashboard">Voltar para o dashboard</a></p>
