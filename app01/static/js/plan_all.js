function Make_plan() {
    let div_plan = document.getElementById('plan');
    let add_form = document.getElementById('plan1');
    let str = add_form.innerHTML;
    let node = document.createElement('div')
    node.innerHTML = str
    let node1 = document.createElement('input')
    node1.setAttribute("type", "button")
    node1.setAttribute("value", "Del")
    node1.setAttribute("id","delete")
    node1.setAttribute("onclick", "Delete_plan()")
    node1.setAttribute("class", "delete_button")
    let br1 = document.createElement('br')
    let br2 = document.createElement('br')
    let br3 = document.createElement('br')
    let br4 = document.createElement('br')
    let HR = document.createElement('HR')
    HR.setAttribute("width", "300")
    HR.setAttribute("color","#b9b4ae")
    node.appendChild(br1)
    node.appendChild(br2)
    node.appendChild(node1)
    node.appendChild(br3)
    node.appendChild(br4)
    node.appendChild(HR)
    div_plan.appendChild(node)
}
function Delete_plan() {
    let del_form = document.getElementById('delete');
    del_form.parentElement.remove()
}

function time_maker() {
    let n = document.getElementById('get_time').value;
    let dync = document.getElementById('dync')
    dync.innerHTML=''
    //let plan1 = document.getElementById('plan1')
    //let str = plan1.innerHTML;
    let tpl = "";
    for (let i = 0; i < n; i++) {
        tpl += `<div class="inpIte"><span>times${i+1}: </span><input type="time" name="num_time"/></div>`
    }
    dync.innerHTML = tpl
}

