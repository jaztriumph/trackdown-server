$(document).ready(function () {
    $('.sidenav').sidenav();
    $('.collapsible').collapsible();
});

function signOut() {
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function () {
        console.log('User signed out.');
    });
    GoogleAuth.disconnect();
}

function onLoad() {
    gapi.load('auth2', function () {
        gapi.auth2.init();
    });
}
