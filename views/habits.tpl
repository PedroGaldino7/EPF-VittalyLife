% rebase('layout.tpl', title='Hábitos')

<link rel="stylesheet" href="../static/css/stylePages.css">

<h1>Hábitos</h1>

<table border="1">
    <tr>
        <th>Nome</th>
        <th>Descrição</th>
        <th>Frequência</th>
        <th>Status</th>
        <th>Ações</th>
    </tr>

    % for h in habits:
    <tr>
        <td>{{h["name"]}}</td>
        <td>{{h["description"]}}</td>
        <td>{{h["frequency"]}}</td>

        <!-- STATUS -->
        % if h["done"]:
            <td style="color: green; font-weight: bold;">Concluído ✓</td>
        % else:
            <td style="color: red; font-weight: bold;">Pendente ✗</td>
        % end

        <td>
            <a href="/habits/edit/{{h['id']}}">Editar</a>

            <form action="/habits/delete/{{h['id']}}" method="post" style="display:inline;">
                <button type="submit">Excluir</button>
            </form>

            % if not h["done"]:
                <form action="/habits/checkin/{{h['id']}}" method="post" style="display:inline;">
                    <button type="submit">Check-in</button>
                </form>
            % else:
                <span style="color: #888; font-size: 14px;">✔ Já concluído hoje</span>
            % end
        </td>
    </tr>
    % end
</table>

<p><a href="/dashboard">Voltar para o dashboard</a></p>
