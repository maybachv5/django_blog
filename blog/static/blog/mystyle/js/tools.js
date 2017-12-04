function wordsearch_func(URL){
    var word = $("#tb-search").val();
    if (word.length>1){
    $.get(URL,
        {"word":word},
        function(ret){
            var tbhtml = "";
            var tmhtml = "";
            var jdhtml = "";
            var tbret = ret.tb_results;
            var tmret = ret.tm_results;
            var jdret = ret.jd_results;
            for (var i=0;i<tbret.length;i++){
                tbhtml += '<tr><th scope="row">' + (i+1) + '</th>' + '<td>' + tbret[i][0] +
                '</td>' + '<td>' + tbret[i][1] + '</td></tr>'
            };
            $("#tb-results").html(tbhtml);
            for (var j=0;j<tmret.length;j++){
                tmhtml += '<tr><th scope="row">' + (j+1) + '</th>' + '<td>' + tmret[j][0] + '</td>' +
                '<td>' + tmret[j][1] + '</td>' + '<td>' + tmret[j][2] + '</td>' +
                '<td>' + tmret[j][3] + '</td></tr>'
            }
            $("#tm-results").html(tmhtml);
            for (var k=0;k<jdret.length;k++){
                jdhtml += '<tr><th scope="row">' + (k+1) + '</th>' + '<td>' + jdret[k].key +
                '</td>' + '<td>' + jdret[k].qre + '</td></tr>'
            }
            $("#jd-results").html(jdhtml);

    });
    };
    if (word.length<1){
    alert('搜索词不能为空！')
    }

}