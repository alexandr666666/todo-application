function changeColor() { // изменит цвет при наведении мыши
    document.getElementById("add-task").style.backgroundColor = "green";
    document.getElementById("add-task").style.borderColor = "green";
}

function resetColor() { // вернуть прежний цвет при отведении мыши
    document.getElementById("add-task").style.backgroundColor = "blue";
    document.getElementById("add-task").style.borderColor = "blue";
}