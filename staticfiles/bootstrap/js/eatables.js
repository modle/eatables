function Rate(x, recipeId) {
    $.ajax({
         type:"POST",
//         url:"/update_rating/",
         data: {
                'rating': x,
                'recipeId': recipeId,
                csrfmiddlewaretoken: '{{ csrf_token }}',
                },
         success: alert("you clicked " + x + " for recipe " + recipeId)
    });
    return false;
};
