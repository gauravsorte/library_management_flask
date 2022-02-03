var serarch_filter = document.querySelector('.dropdown')
// console.log(serarch_filter.innerHTML);

serarch_filter.innerHTML += '<option class="dropdown_links" value="Book ID">Book ID</option>'
serarch_filter.innerHTML += '<option class="dropdown_links" value="Title">Title</option>'
serarch_filter.innerHTML += '<option class="dropdown_links" value="Author">Author</option>'
serarch_filter.innerHTML += '<option class="dropdown_links" value="ISBN">ISBN</option>'

// console.log('hii hello');

function filter_by_id(value){
    var table_rows = document.querySelectorAll('.table_value_')
    if(value) {
        console.log(table_rows);
        for (let index = 0; index < table_rows.length; index++){
            if(table_rows[index].children[0].innerText != value){
                table_rows[index].classList.add('hidden')
            } else {
                table_rows[index].classList.remove('hidden')
            }
        }
    } else {
        for (let index = 0; index < table_rows.length; index++){
                table_rows[index].classList.remove('hidden')
        }
    }
    
}

function filter_by_title(value){
    var table_rows = document.querySelectorAll('.table_value_')
    if(value) {
        console.log(table_rows);
        for (let index = 0; index < table_rows.length; index++){
            if(table_rows[index].children[1].innerText != value){
                table_rows[index].classList.add('hidden')
            } else {
                table_rows[index].classList.remove('hidden')
            }
        }
    } else {
        for (let index = 0; index < table_rows.length; index++){
                table_rows[index].classList.remove('hidden')
        }
    }
    
}


function filter_by_author(value){
    var table_rows = document.querySelectorAll('.table_value_')
    if(value) {
        console.log(table_rows);
        for (let index = 0; index < table_rows.length; index++){
            if(table_rows[index].children[2].innerText != value){
                table_rows[index].classList.add('hidden')
            } else {
                table_rows[index].classList.remove('hidden')
            }
        }
    } else {
        for (let index = 0; index < table_rows.length; index++){
                table_rows[index].classList.remove('hidden')
        }
    }
    
}


function filter_by_ISBN(value){
    var table_rows = document.querySelectorAll('.table_value_')
    if(value) {
        console.log(table_rows);
        for (let index = 0; index < table_rows.length; index++){
            if(table_rows[index].children[3].innerText != value){
                table_rows[index].classList.add('hidden')
            } else {
                table_rows[index].classList.remove('hidden')
            }
        }
    } else {
        for (let index = 0; index < table_rows.length; index++){
                table_rows[index].classList.remove('hidden')
        }
    }
    
}




function filter_by(selected_filter, value){
    if(selected_filter == "Book ID"){
        filter_by_id(value)
    } else if(selected_filter == "Title"){
        filter_by_title(value)
    } else if(selected_filter == "Author") {
        filter_by_author(value)
    } else if(selected_filter == "ISBN") {
        filter_by_ISBN(value)
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
// console.log('hi there');

// serarch_filter.onchange = filter();
// filter()
