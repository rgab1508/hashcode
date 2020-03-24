var fs = require("fs");

var scores = {};
var days;
var libs = [];
var lib_app = [];
var file = 'b_read_on.txt';

fs.readFile(file,'utf8', function(err, data) {
    var lines = data.split("\n");
    var bi = parseInt(lines[0].split(" ")[0]);
    var li = parseInt(lines[0].split(" ")[1]);
    days = parseInt(lines[0].split(" ")[2]);
    for (i=0; i<bi; i++) {scores[i]=parseInt(lines[1].split(" ")[i])}
    for (k=0; k<li; k++) {libs[k]={"time":parseInt(lines[2*k+2].split(" ")[1]),"n": parseInt(lines[2*k+2].split(" ")[2]),"books": lines[2*k+3].split(" ")}}
    for (k=0; k<li; k++) {var sum = 0; libs[k].books.forEach(x=>{sum+=scores[x]}); lib_app[k]=(sum/libs[k].books.length)*libs[k].n}
    var ldays = days;
    var ord = [];
    var ns = 0;
    libs.forEach(x => {ns+=x.time});
    var n = Math.floor(days*li/ns);
    var clib_app = lib_app;
    clib_app.sort(function(a,b) {return a-b;});
    ord = clib_app.map(x => lib_app.indexOf(x));
    fs.appendFile("soln_"+file,n+"\n",function() {});
    for (x in ord) {
    	fs.appendFile("soln_"+file,+ord[x]+" "+libs[ord[x]].books.length+"\n"+libs[ord[x]].books.sort(function(a,b) {return scores[a]-scores[b];}).join(" ")+"\n",function() {});
    }
});
