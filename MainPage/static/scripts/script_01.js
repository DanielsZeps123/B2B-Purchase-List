var filters = []

function funct1(value) {
    filters.push(value);
    target = document.getElementById("filters1");
    target.innnerHTL = "";
    filters.forEach(element => {
        target.innnerHTML += "<button>" + element + "</button>";
    });
}