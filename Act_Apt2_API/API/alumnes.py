def alumne_schema(alumne) -> dict:
    return {
        "NomAlumne": alumne[2],
        "Cicle": alumne[3],
        "Curs": alumne[4],
        "Grup": alumne[5],
        "DescAula": alumne[8],
    }
def alumnes_schema(fetchAlumnes) -> dict:
    return [alumne_schema(alumne) for alumne in fetchAlumnes]

def aula_schema(aula) -> dict:
    return {
        "IdAula": aula[0],
        "DescAula": aula[1],
        "Edifici": aula[2],
        "Pis": aula[3],
        "CreatedAt": aula[4],
        "UpdatedAt": aula[5]
    }
def aules_schema(aules) -> dict:
    return [aula_schema(aula) for aula in aules]