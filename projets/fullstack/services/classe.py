from modele import Eleve
from modele import Classe
import services.eleves as svc_eleve


a=svc_eleve.get_all_eleves()
t09=[]
autre=[]
Classes=[]
for x in a:
    if x.classe == 'T09':
        truc=[x.prenom, x.nom]
        t09.append(truc)
    else:
        autre_eleves=[x.prenom , x.nom]
        autre.append(autre_eleves)

Classes.append(Classe(2,x.classe,autre))
Classes.append(Classe(1,'T09',t09))

def get_all_Classes() -> list[Classe]:
    return Classes

def get_Classes(id: int) -> Classe:
    return [e for e in Classes if e.id == id][0]

def update_Classes(id: int, nom: str, eleves: tuple[Eleve, ...]) -> None:
    e = get_Classes(id)
    e.nom = nom
    e.eleves = eleves

def delete_Classes(id: int) -> None:
    Classes.remove(get_Classes(id))

def create_Classes(nom: str, eleves: tuple[Eleve, ...]) -> int:
    newid: int = max(Classes, key=lambda e: e.id).id + 1
    Classes.append(Classe(newid, nom, eleves))
    return newid