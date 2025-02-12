from modele import Classe
import services.eleves as svc_eleve


a=svc_eleve.get_all_eleves()
Classes=[Classe(1,'T09'),Classe(2,'T10'),Classe(3,'T11')]

def get_all_Classes() -> list[Classe]:
    return Classes

def get_Classes(id: int) -> Classe:
    return [e for e in Classes if e.id == id][0]

def update_Classes(id: int, nom: str) -> None:
    e = get_Classes(id)
    e.nom = nom

def delete_Classes(id: int) -> None:
    Classes.remove(get_Classes(id))

def create_Classes(nom: str) -> int:
    newid: int = max(Classes, key=lambda e: e.id).id + 1
    Classes.append(Classe(newid, nom))
    return newid