

const openEdit = document.querySelectorAll(".btn-edit")
openEdit.forEach(button=>{

    button.addEventListener('click',()=>{

        const modalDm= button.getAttribute("data-modal")
        const modal= document.getElementById(modalDm)
        //1. Extrai dados do botão
        const id = button.getAttribute("data-id")
        const produto = button.getAttribute("data-produto")
        const categoria = button.getAttribute("data-categoria")
        const quantidade = button.getAttribute("data-quantidade")
        const custo =button.getAttribute("data-custo")
        const venda = button.getAttribute("data-venda")

        

        //2.Preenche o formulário
        document.getElementById('input-edit-id').value = id;
        document.getElementById('input-edit-produto').value = produto
        document.getElementById('input-edit-categoria').value = categoria
        document.getElementById('input-edit-quantidade').value = quantidade
        document.getElementById('input-edit-custo').value = custo
        document.getElementById('input-edit-venda').value = venda

        
        modal.showModal()
      
    })
})
const openDelete = document.querySelectorAll(".btn-delete")
const deleteForm = document.getElementById("form-excluir")
openDelete.forEach(button=>{
    button.addEventListener('click',()=>{
        const modalDm= button.getAttribute("data-modal")
        const modal= document.getElementById(modalDm)
        const id = button.getAttribute("data-id")

        deleteForm.action = '/delete/'+id
        
        modal.showModal()
        console.log(id)
    })
})

const closeModals = document.querySelectorAll(".close-modal")
closeModals.forEach(button=> {
    button.addEventListener('click', ()=>{
        const modalDm= button.getAttribute("data-modal")
        const modal= document.getElementById(modalDm)
        modal.close()

    })
})