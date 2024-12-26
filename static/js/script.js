function adicionarCarrinho(produtoId) {
    fetch('/adicionar_carrinho', {
        method: 'POST',
        body: new URLSearchParams({
            'produto_id': produtoId
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status) {
            alert(data.status);  // Mostra a mensagem de sucesso
            atualizarCarrinho();  // Atualiza o carrinho na interface
        }
    })
    .catch(error => console.log('Erro ao adicionar ao carrinho:', error));
}

function atualizarCarrinho() {
    // Fazendo uma nova requisição para buscar o carrinho atualizado
    fetch('/carrinho')
        .then(response => response.json())
        .then(data => {
            let carrinhoHtml = '';
            data.forEach(item => {
                carrinhoHtml += `
                    <div class="d-flex justify-content-between mb-3">
                        <span>${item.nome} - R$ ${item.preco}</span>
                        <button class="btn btn-danger" onclick="excluirItem(${item.id})">Excluir</button>
                    </div>
                `;
            });
            document.getElementById('itensCarrinho').innerHTML = carrinhoHtml;
        })
        .catch(error => console.log('Erro ao atualizar carrinho:', error));
}
