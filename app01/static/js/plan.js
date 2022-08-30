function Make_plan() {
    let add_form = document.getElementById('plan');
    let add_form1 = document.getElementById('plan1');
    let str = add_form1.innerHTML;
    let node = document.createElement('div')
    node.innerHTML = str
    add_form.appendChild(node)


}

function times() {
    let n = document.getElementById('get_time').value;
    let dync = document.getElementById('dync')
    dync.innerHTML=''

    //let plan1 = document.getElementById('plan1')
    //let str = plan1.innerHTML;
    var tpl = ""
    for (let i = 0; i < n; i++) {

        tpl += `<div class="inpIte"><span>times${i+1}: </span><input type="time"/></div>`


    }

    dync.innerHTML = tpl

}

