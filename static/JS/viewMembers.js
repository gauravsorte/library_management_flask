var serarch_filter = document.querySelector('.dropdown')
// console.log(serarch_filter.innerHTML);

serarch_filter.innerHTML += '<option class="dropdown_links" value="Member ID">Member ID</option>'
serarch_filter.innerHTML += '<option class="dropdown_links" value="First Name">First Name</option>'
serarch_filter.innerHTML += '<option class="dropdown_links" value="Last Name">Last Name</option>'
serarch_filter.innerHTML += '<option class="dropdown_links" value="Phone Number">Phone Number</option>'


function filter_by_member_id(value){
    console.log('in filter');
    var table_rows = document.querySelectorAll('.table_value_')
    for (let index = 0; index < table_rows.length; index++) {
        console.log(table_rows[index].childNodes[0])
        
    }
    console.log(table_rows);
}




function filter_by(selected_filter, value){
    if(selected_filter == "Member ID"){
        filter_by_member_id(value)
    } else if(selected_filter == "First Name"){

    } else if(selected_filter == "Last Name") {

    } else if(selected_filter == "Phone Number") {

    }

}

function filter() {
    let serarch_filter_val = document.getElementById('search_filter').value
    console.log('in func');
    let search_text = document.getElementById('search_input').value
    console.log('>>>> ',serarch_filter_val);
    console.log('>>>>>>>>>', search_text);
    filter_by(serarch_filter_val, search_text)
}
console.log('hi there');

// serarch_filter.onchange = filter();
// filter()
