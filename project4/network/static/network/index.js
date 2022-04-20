window.onpopstate = function(event) {
    alert("location: " + document.location + ", state: " + JSON.stringify(event.state));
}

function like(id) {
    fetch(`posts/${id}`)
    .then(response => response.likes)
    .then(likes => {
        console.log(likes)
        document.querySelector('#num-likes').innerHTML = likes;
    });
}

document.addEventListener('DOMContentLoaded', function() {
    const button = document.querySelector('#like-button')
    button.addEventListener('click', () => {
        const likes = this.dataset.likes
        history.pushState({likes: likes}, "", `Likes updated to${likes}`);
        like()
    })
})