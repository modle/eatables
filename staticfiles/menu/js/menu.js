$(document).ready(function() {
    $(".datepicker").datepicker({
        "dateFormat":"yy-mm-dd",
        "changeMonth":true,
        "changeYear":true
    });
});


$('#post-form').on('submit', function(event){
    event.preventDefault();
    alert("form submitted!")  // sanity check
    create_post();
});
