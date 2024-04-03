document.addEventListener('DOMContentLoaded', function() {
    executeSearch('');
});

document.getElementById('searchInput').addEventListener('input', function() {
    var searchQuery = this.value;
    executeSearch(searchQuery);
});

function executeSearch(query) {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            var searchResults = JSON.parse(xhr.responseText);
            displaySearchResults(searchResults);
        }
    };
    xhr.open('GET', '/search?query=' + query, true);
    xhr.send();
}

function displaySearchResults(results) {
    var searchResultsElement = document.getElementById('searchResults');
    searchResultsElement.innerHTML = '';

    results.forEach(function(result) {
        var li = document.createElement('li');
        var a = document.createElement('a');
        a.setAttribute('href', '#');
        a.setAttribute('class', 'user-link');
        a.setAttribute('data-user-name', result.name);
        a.textContent = result.name;
        searchResultsElement.appendChild(li);
        li.appendChild(a);
    });
}
