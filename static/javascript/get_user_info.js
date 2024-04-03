document.addEventListener('DOMContentLoaded', function () {
    const user_info_div = document.getElementById('user_info');

    document.getElementById('contener').addEventListener('click', function(event) {
        if (event.target.classList.contains('user-link')) {
            event.preventDefault();
            const user_name = event.target.getAttribute('data-user-name');
            fetch(`/get_user_info/${user_name}/`)
                .then(response => response.json())
                .then(data => {
                    user_info_div.innerHTML = `
                    <p> ${data.name} </p>
                    <p> ${data.position} </p>
                    <p> ${data.description} </p>
                   `
                })
                .catch(error => console.log('Error: ', error))
        }
    });
});
