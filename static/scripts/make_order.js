let order_cost = 0;

function takenDateChange(){
    let date1 = document.getElementById('date1');
    let date_value = date1.value;
    let date2 = document.getElementById('date2');
    date2.setAttribute('min', date_value);
}

function checkedProduct(id){
    let checkbox = document.getElementById('select'+id);
    let costInput = document.getElementById('cost'+id);
    let numberInput = document.getElementById('number'+id);
    let cost = (costInput.textContent * 1) * numberInput.value;
    if(checkbox.checked){
        order_cost += cost;
    }
    else {
        order_cost -= cost;
    }
    let orderCost = document.getElementById('orderCost');
    orderCost.textContent = (order_cost+0.001).toFixed(2);
}

function numberButtonClick(id, button, stock){
    let numberInput = document.getElementById('number'+id);
    if((stock <= numberInput.value && button ==2) || (numberInput.value <= 1 && button==1)){
        return ;
    }
    let checkbox = document.getElementById('select'+id);
    let costInput = document.getElementById('cost'+id);
    let cost = costInput.textContent * 1;
    if (button==1 && checkbox.checked){
        order_cost -= cost;
    }
    else{
        if(button==2 && checkbox.checked){
            order_cost += cost;
        }
    }
    let orderCost = document.getElementById('orderCost');
    orderCost.textContent = (order_cost+0.001).toFixed(2);
}

function setCost(){
    let checkedProducts = document.getElementsByName("checked_product");
    for(let i=0; i<checkedProducts.length; ++i){
         if(checkedProducts[i].checked){
             let costInput = document.getElementById('cost'+checkedProducts[i].value);
             let numberInput = document.getElementById('number'+checkedProducts[i].value);
             let cost = (costInput.textContent * 1) * numberInput.value;
             order_cost += cost;

         }
    }
    let orderCost = document.getElementById('orderCost');
    orderCost.textContent = order_cost.toFixed(2);
}

document.addEventListener("DOMContentLoaded", setCost);

function insertCost(){
    let orderForm = document.getElementById('orderForm');
    let inputCost = document.createElement("input");
    inputCost.type = "hidden";
    inputCost.name = "inputCost";
    inputCost.value = order_cost;
    orderForm.appendChild(inputCost);
}