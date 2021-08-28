

function perform_like(post_id){
    const csrftoken = getCookie('csrftoken')
    $.ajax(
        {
            url: '/ajax/like-post',
            type: "POST",
            headers: {"X-CSRFToken": csrftoken},
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

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}