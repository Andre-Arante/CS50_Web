var last_form = null;
document.addEventListener('DOMContentLoaded', function () {

    //Add the likeDislike () function call to the heart's onclick method
    document.querySelectorAll('.fa-heart').forEach(div => {
        div.onclick = function () {
            likeDislike(this);
        };
    });

    //It receives an element and makes the asynchronous call of the like method.
    async function likeDislike(element) {
        await fetch(`/like/${element.dataset.id}`)
            .then(response => response.json())
            .then(data => {
                element.className = data.css_class;
                element.querySelector('small').innerHTML = data.total_likes;
            });
    }
});