function delete_plan() {
    let id = document.getElementById('del').value;
    console.log(id)
    $.ajax({
        type: 'POST',
        url: '/main/',
        data: {
            'id': id
        },
        datatype: 'json'
    })
    window.location.reload()
}
