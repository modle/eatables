$(document).ready( function() {
  $('.notSelectable').disableSelection();

  $('#edit_recipe').on('click', showAddIngredientModal);

  addIngredientModal = document.getElementById('addIngredientModal');
  if (addIngredientModal) {
    hideModal(addIngredientModal);
  }
});

function showAddIngredientModal() {
  showModal(addIngredientModal);
  $('#id_name').focus();
  // hideModalAfterAWhile(addIngredientModal);
}

function showModal(modal) {
  console.log("showing modal: " + modal.id)
  modal.style.display = "block";
}

function hideModal(modal) {
  modal.style.display = "none";
}

function hideModalAfterAWhile(modal) {
  setTimeout(function(){ hideModal(modal); }, 3000);
}

/* eslint-disable camelcase*/
$('.recipe_block').mousemove(function() {
    recipe_id = this.id;
});
$('.recipe_block').swipe({
  tap: function(event, target) {
    window.location.href = '/'+recipe_id+'/recipe_details/';
  },
  swipeLeft: function(event, direction, distance, duration, fingerCount) {
    window.location.href = '/'+recipe_id+'/edit_recipe/';
  },
  threshold: 50,
  allowPageScroll: 'auto',
});
/* eslint-enable camelcase*/


// makes text non-selectable on mobile, and prevents the highlight on long-press function
$.fn.extend({
    disableSelection: function() {
        this.each(function() {
            this.onselectstart = function() {
                return false;
            };
            this.unselectable = 'on';
            $(this).css('-moz-user-select', 'none');
            $(this).css('-webkit-user-select', 'none');
        });
        return this;
    },
});


// This function gets cookie with a given name
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie != '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
let csrftoken = getCookie('csrftoken');


/*
The functions below will create a header with csrftoken
*/

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    let host = document.location.host; // host + port
    let protocol = document.location.protocol;
    let srOrigin = '//' + host;
    let origin = protocol + srOrigin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == srOrigin || url.slice(0, srOrigin.length + 1) == srOrigin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            xhr.setRequestHeader('X-CSRFToken', csrftoken);
        }
    },
});