

$(document).ready( function() {
  $("span").click(function(){
    $(this).attr("href", "#ex1");
    $(this).attr("rel", "modal:open");

  //$("span").mouseleave(function(){
   //     $(this).css("background-color", "white");
    //});
});
  $("#modal1").click( function(event) {
msgstr = $("#msg").html()
        msgstr = msgstr + "o"
        $("#msg").html(msgstr)
 });

  $("#modal2").click( function(event) {
msgstr = $("#msg").html()
        msgstr = msgstr + "a"
        $("#msg").html(msgstr)
 });

  $("#modal3").click( function(event) {
msgstr = $("#msg").html()
        msgstr = msgstr + "i"
        $("#msg").html(msgstr)
 });

  $("#modal4").click( function(event) {
msgstr = $("#msg").html()
        msgstr = msgstr + "u"
        $("#msg").html(msgstr)
 });
	
    
});

