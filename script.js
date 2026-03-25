const openEdit = document.querySelectorAll(".btn-edit")
openEdit.forEach(button=>{
    button.addEventListener('click',()=>{
        const modalDm= button.getAttribute("data-modal")
        const modal= document.getElementById(modalDm)
        modal.showModal()
    })
})
const openDelete = document.querySelectorAll(".btn-delete")
openDelete.forEach(button=>{
    button.addEventListener('click',()=>{
        const modalDm= button.getAttribute("data-modal")
        const modal= document.getElementById(modalDm)
        modal.showModal()
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