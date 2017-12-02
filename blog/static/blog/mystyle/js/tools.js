function wordsearch_func(URL){
    var word = $("#tb-search").val();
    if (word.length>1){
    $.get(URL,
        {"word":word},
        function(ret){
            var tbhtml = "";
            var tmhtml = "";
            var tmret = ret.tm_results;
            for (var i=0;i<ret.tb_results.length;i++){
                tbhtml += '<tr><th scope="row">' + i + '</th>' + '<td>' + ret.tb_results[i][0] +
                '</td>' + '<td>' + ret.tb_results[i][1] + '</td></tr>'
            };
            $("#tb-results").html(tbhtml);
            for (var j=0;j<tmret.length;j++){
                tmhtml += '<tr><th scope="row">' + j + '</th>' + '<td>' + tmret[j][0] + '</td>' +
                '<td>' + tmret[j][1] + '</td>' + '<td>' + tmret[j][2] + '</td>' +
                '<td>' + tmret[j][3] + '</td></tr>'
            }
            $("#tm-results").html(tmhtml);
    });
    };
    if (word.length<1){
    alert('搜索词不能为空！')
    }

}