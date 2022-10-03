function delete_plan() {
    let id = document.getElementById('del').value;
    console.log(id)
    $.ajax({
        type: 'GET',
        url: '/delete/',
        data: {
            'id': id
        },
        datatype: 'json'
    })
    window.location.reload()
}
