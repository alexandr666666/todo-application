function changeColor() { // изменит цвет при наведении мыши
    document.getElementById("redirect-to-add-page").style.backgroundColor = "green";
    document.getElementById("redirect-to-add-page").style.borderColor = "green";
}

function resetColor() { // вернуть прежний цвет при отведении мыши
    document.getElementById("redirect-to-add-page").style.backgroundColor = "blue";
    document.getElementById("redirect-to-add-page").style.borderColor = "blue";
}