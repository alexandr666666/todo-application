function changeTheme() {
    var theme = document.getElementById("theme-selector").value;
    var body = document.body;

    if (theme === "light") {
        body.className = "light-theme";
    } else if (theme === "dark") {
        body.className = "dark-theme";
    }
}