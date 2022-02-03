var serarch_filter = document.querySelector('.dropdown')
// console.log(serarch_filter.innerHTML);

serarch_filter.innerHTML += '<option class="dropdown_links" value="Member ID">Member ID</option>'
serarch_filter.innerHTML += '<option class="dropdown_links" value="First Name">First Name</option>'
serarch_filter.innerHTML += '<option class="dropdown_links" value="Last Name">Last Name</option>'
serarch_filter.innerHTML += '<option class="dropdown_links" value="Phone Number">Phone Number</option>'


function filter_by_member_id(value){
    // console.log('in filter');
    var table_rows = document.querySelectorAll('.table_value_')
    if (value){
        for (let index = 0; index < table_rows.length; index++) {
            console.log(table_rows[index].children[0].innerText)
            if(table_rows[index].children[0].innerText != value){
                table_rows[index].classList.add('hidden')
            } else {
                table_rows[index].classList.remove('hidden')
            }
            
        }
    } else {
        for (let index = 0; index < table_rows.length; index++) {
            
                table_rows[index].classList.remove('hidden')
        }
    }
    
    console.log(table_rows);
}

function filter_by_first_name(value){
    // console.log('in filter');
    var table_rows = document.querySelectorAll('.table_value_')
    if (value){
        for (let index = 0; index < table_rows.length; index++) {
            // console.log(table_rows[index].children[1].innerText)
            if(table_rows[index].children[1].innerText != value){
                table_rows[index].classList.add('hidden')
            } else {
                table_rows[index].classList.remove('hidden')
            }
            
        }
    } else {
        for (let index = 0; index < table_rows.length; index++) {
                table_rows[index].classList.remove('hidden')
        }
    }
    
    console.log(table_rows);
}

function filter_by_last_name(value){
    // console.log('in filter');
    var table_rows = document.querySelectorAll('.table_value_')
    if (value){
        for (let index = 0; index < table_rows.length; index++) {
            if(table_rows[index].children[2].innerText != value){
                table_rows[index].classList.add('hidden')
            } else {
                table_rows[index].classList.remove('hidden')
            }
            
        }
    } else {
        for (let index = 0; index < table_rows.length; index++) {
            
                table_rows[index].classList.remove('hidden')
        }
    }
    
    console.log(table_rows);
}

function filter_by_phone_number(value){
    // console.log('in filter');
    var table_rows = document.querySelectorAll('.table_value_')
    if (value){
        for (let index = 0; index < table_rows.length; index++) {
            if(table_rows[index].children[3].innerText != value){
                table_rows[index].classList.add('hidden')
            } else {
                table_rows[index].classList.remove('hidden')
            }
            
        }
    } else {
        for (let index = 0; index < table_rows.length; index++) {
            
                table_rows[index].classList.remove('hidden')
        }
    }
    
    console.log(table_rows);
}




function filter_by(selected_filter, value){
    if(selected_filter == "Member ID"){
        filter_by_member_id(value)
    } else if(selected_filter == "First Name"){
        filter_by_first_name(value)

    } else if(selected_filter == "Last Name") {
        filter_by_last_name(value)

    } else if(selected_filter == "Phone Number") {
        filter_by_phone_number(value)

    }

}

function filter() {
    let serarch_filter_val = document.getElementById('search_filter').value
    if(!serarch_filter_val){
        console.log('TRUE');
        let table_rows = document.querySelectorAll('.table_value_')
        for (let index = 0; index < table_rows.length; index++){
            table_rows[index].classList.remove('hidden')
        }
    } else {
        console.log(serarch_filter_val);
        let search_text = document.getElementById('search_input').value
        console.log('>>>> ',serarch_filter_val);
        filter_by(serarch_filter_val, search_text)
    }
    
}
console.log('hi there');

// serarch_filter.onchange = filter();
// filter()
