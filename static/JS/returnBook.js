let return_book_btn = document.getElementById("return_book_btn")
var total_amount = document.querySelector('.total_amount');
var book_id = document.querySelector(".issued_book_id");
var table = document.querySelector(".table");

var debt_msg = document.querySelector('.debt_msg');

console.log('in return book js');

function check_disabled() {
    var amt_paid = document.querySelector('.amount_paid_');

    // console.log('in function', amt_paid.value, total_amount.innerText);

    console.log((parseInt(total_amount.innerText) - parseInt(amt_paid.value)));
    if((parseInt(total_amount.innerText) - parseInt(amt_paid.value))>500){
        // console.log('true');
        debt_msg.classList.remove("hidden");
        return_book_btn.setAttribute('disabled', 'True')
    } else {
        // console.log('false');
        debt_msg.classList.add("hidden");
        return_book_btn.removeAttribute('disabled', '' );
    }
}


// amt_paid.addEventListener('change', (event)=> {
//     console.log(event);
// })