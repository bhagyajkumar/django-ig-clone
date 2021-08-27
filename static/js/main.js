

function perform_like(post_id){
    $.ajax(
        {
            url: '/ajax/like-post',
            type: "POST",
            data: {
                post_id: post_id
            },
            success: (data)=>{
                var like_button = document.querySelector(`#like-${post_id}`)
                var like_count = document.querySelector(`#like-count-${post_id}`)
                if (data.status == 1){
                    like_button.classList.add('liked')
                }
                else{
                    like_button.classList.remove('liked')
                }
                like_count.textContent = data.total
            }

        }
    )
}