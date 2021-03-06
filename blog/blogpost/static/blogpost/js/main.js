$(document).ready(function () {
    $('#typeahead-input').typeahead({
        source: function (query, process) {
            return $.get('/blogpost/api/blogpost/?format=json&title=' + query, function (data) {
                return process(data);
            });
        },
        updater: function (item) {
            return item;
        },
        displayText: function (item) {
            return item.title;
        },
        afterSelect: function (item) {
            location.href = 'http://localhost:8088/blogpost/blog/' + item.slug + ".html";
        },
        delay: 500
    });
});
