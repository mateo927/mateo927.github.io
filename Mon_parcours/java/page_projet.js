
function projets(Id){
    var text;

    if (Id=="ecole"){
        text="NAVAL"
    }

    if (Id=="bois"){
        text="Thales"
    }

    if (Id=="travail"){
        text="Orange-cyberdefense"
    }
    document.getElementById("prochain-projet").textContent=text;
}
