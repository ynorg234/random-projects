function array(text) {
    var e = text;
    if (isFinite(e) !== false) {
        e = e.toString()
    }
    var a = [0];
    var t = 0;
    var i = 0;
    for (var d = 0; d < e.length; d++) {
        a[d] = 0;
    }
    while (i < a.length) {
        if (i === e.length) {
            i = 0;
            t++;
            if (t === e.length) {
                break;
            }
        }
        a[i] = e[i];
        i++;
    }
    return a;
}
