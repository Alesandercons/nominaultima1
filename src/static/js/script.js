const eliminaModal = document.getElementById('eliminaModal');
eliminaModal.addEventListener('show.bs.modal', event => {
    const button = event.relatedTarget;
    const id = button.getAttribute('data-bs-id');
    const form = document.querySelector('#form-elimina');
    form.action = form.action.split('?')[0] + '?id=' + id;
    document.querySelector('#form-elimina input[name="id"]').value = id;
});




