var info = {
    'auther': 'author',
    'size': 20,
    'cur_page': 1,
    'cur_size': 20,
    'isLoading': false
}
$(function () {
    window.onscroll = function () {
        var scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
//	    var scrollHeight = $('body')[0].scrollHeight;
        var bottomY = $('#footer').position().top;
        if (scrollTop >= bottomY - 600) {
            if (!info.isLoading && info.cur_size == info.size) {
                info.cur_page = info.cur_page + 1;
                info.isLoading = true;
                getArticles();
            }
        }
    }

    getArticles()
})


function getArticles() {

    $("#loader").show();

    $.ajax({
        type: "get",
        url: "post",
        data: {page: info.cur_page, size: info.size},
        dataType: 'json',
        success: function (data) {
            info.cur_page = data.page;
            info.cur_size = data.size;
            var html = template('article-list-temp', data);
            $("#blog-post").append(html)
        },
        complete: function () {
            info.isLoading = false;
            $("#loader").hide();
        }
    });

}
