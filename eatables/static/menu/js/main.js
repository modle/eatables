$(document).ready( function() {
  $('.notSelectable').disableSelection();

  $('#add-ingredient-button').on('click', showAddIngredientModal);
  $('#cancel-ingredient-add').on('click', hideAddIngredientModal);

  $('#add-note-button').on('click', showAddCommentModal);
  $('#cancel-comment-add').on('click', hideAddCommentModal);
});

/*
handle modals
*/
function showAddIngredientModal() {
  showModal(addIngredientModal);
  $('#id_name').focus();
  hideButtons();
}
function showAddCommentModal() {
  showModal(addCommentModal);
  $('#comment_field').focus();
  hideButtons();
}
function hideButtons() {
  hideComponent('add-ingredient-button');
  hideComponent('edit-button');
  hideComponent('add-note-button');
}
function hideComponent(componentId) {
  $('#' + componentId).hide()
}
function hideAddIngredientModal() {
  hideModal(addIngredientModal);
  showButtons();
}
function hideAddCommentModal() {
  hideModal(addCommentModal);
  showButtons();
}
function showButtons() {
  showComponent('add-ingredient-button');
  showComponent('edit-button');
  showComponent('add-note-button');
}
function showComponent(componentId) {
  $('#' + componentId).show()
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


/*
add ingredient to shopping list asynchronously
*/
function add_to_shopping_list(ingredient_id, source_page) {
  console.log("adding ingredient_id " + ingredient_id + " to shopping list")
  $.ajax({
    url : "/add_to_shopping_list/",
    type : "POST",
    data : { ingredient_id : ingredient_id },
    success : function(json) {
      console.log(json['status'])
      $("#results_"+json.id).html("<strong>ADDED!</strong>");
      if (source_page == 'shopping_list') {
        location.reload();
      }
    },
    error : function(xhr, errmsg, err) {
      console.log("encountered an error: " + errmsg);
    }
  });
};


function pushIngredientBlock(ingredient) {
  console.log(ingredient);
  console.log(buildIngredientBlock(ingredient));
  $("#ingredients_section").append(buildIngredientBlock(ingredient));
}

function buildIngredientBlock(ingredient) {
  ingredient_block = '<div class="ingredient_block">' +
  '<div class="ingredient_details">' +
  '<a class="right_tab_button" id="' + ingredient.id + '" onClick="add_to_shopping_list(this.id)">+</a>' +
  ingredient.amount + ' ' + ingredient.unit + ' ' + ingredient.name + ', ' + ingredient.comment +
  '</div></div>';
  return ingredient_block;
}

/*
add ingredient to recipe asynchronously
*/
function add_ingredient_to_recipe(recipe_id) {
  console.log("adding ingredient to " + recipe_id);
  ingredient = {};
  ingredient.name = $('#ingredient_name').val();
  ingredient.amount = $('#ingredient_amount').val();
  ingredient.unit = $('#ingredient_unit').val();
  ingredient.comment = $('#ingredient_comment').val();
  ingredient.recipe_id = recipe_id;
  console.log(ingredient);
  $.ajax({
    url : "/add_ingredient_to_recipe/",
    type : "POST",
    data : ingredient,
    success : function(json) {
      console.log(json['status'])
      ingredient = json['ingredient']
      ingredient.id = json['id']
      pushIngredientBlock(json['ingredient'])
    },
    error : function(xhr, errmsg, err) {
      console.log("encountered an error: " + errmsg);
    }
  });
};


function pushCommentBlock(comment) {
  console.log(comment);
  console.log(buildCommentBlock(comment));
  $("#comments_section").prepend(buildCommentBlock(comment));
}

function buildCommentBlock(comment) {
  comment_block = '<div class="comment_block notSelectable" id="' + comment.recipe_id + '12" style="user-select: none;">' +
  comment.publishDate +
  '<a href="/' + comment.id + '/comment_delete/" onclick="return confirm(\'Are you sure you want to delete this note?\')">' +
  '<img style="margin-top: 5px;" src="/staticfiles/menu/img/delete_icon.png" height="16em"></a>' +
  '<br>' +
  comment.comment + '</div><hr>';
  return comment_block;
}

/*
add comment to recipe asynchronously
*/
function add_comment_to_recipe(recipe_id) {
  console.log("adding comment to " + recipe_id);
  comment = {};
  comment.comment = $('#comment_field').val();
  comment.recipe_id = recipe_id;
  console.log(comment);
  $.ajax({
    url : "/add_comment_to_recipe/",
    type : "POST",
    data : comment,
    success : function(json) {
      console.log(json['status'])
      comment = json['comment']
      comment.id = json['id']
      comment.publishDate = json['publishDate']
      pushCommentBlock(json['comment'])
    },
    error : function(xhr, errmsg, err) {
      console.log("encountered an error: " + errmsg);
    }
  });
};


/*
handles tap and swipe
*/
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


/*
makes text non-selectable on mobile, and prevents the highlight on long-press function
*/
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


/*
This function gets cookie with a given name
*/
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
