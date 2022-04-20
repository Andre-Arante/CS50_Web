document.addEventListener('DOMContentLoaded', function() {

    function likeOrUnlike(id, like) {
        fetch(`/like/${id}`, {
          method: "PUT",
          body: JSON.stringify({ like: !!like }),
        })
          .then((resp) => resp.json())
          .then((post) => {
            document.querySelector(`#like_count${id}`).innerHTML = post.likes;
          });
      }
      
      function like(id) {
        likeOrUnlike(id, true);
      }
      
      function unlike(id) {
        likeOrUnlike(id, false);
      }
});