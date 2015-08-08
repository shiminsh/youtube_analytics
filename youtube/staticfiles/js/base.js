msg = "Your Suggestion and Support very much required to success the initiatives -- Bong Collection....     ";
pos = 0;
function ScrollMessage() {
    var newtext = msg.substring(pos, msg.length) + msg.substring(0, pos);
    var div = document.getElementById("scroll");
    div.firstChild.nodeValue = newtext;
    pos++;
    if (pos >= msg.length) pos = 0;
    window.setTimeout(ScrollMessage,300);
}
ScrollMessage(); 