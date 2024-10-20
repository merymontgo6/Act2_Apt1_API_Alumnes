from fastapi import Query
from client import db_client
from typing import Optional

def fetch_all_alumnes():
    try:
        conn = db_client()
        cur = conn.cursor()

        # SQL uneix alumnat amb aula
        query = """
        SELECT a.NomAlumne, a.Cicle, a.Curs, a.Grup, au.descAula
        FROM alumnat a
        JOIN aula au ON a.IdAula = au.IdAula

        """
        
        cur.execute(query)
        alumnes = cur.fetchall()

        # Convertim els resultats a un format de diccionari
        alumnes_list = []
        for alumne in alumnes:
            alumnes_list.append({
                "nomAlumne": alumne[0],
                "cicle": alumne[1],
                "curs": alumne[2],
                "grup": alumne[3],
                "descAula": alumne[4],
            })

    except Exception as e:
        return {"status": -1, "message": f"Error de lectura: {e}" }
    
    finally:
        conn.close()

    return alumnes_list

def get_alumnes_paginated(orderby: Optional[str], contain: Optional[str], skip: int, limit: int):
    try:
        conn = db_client()
        cur = conn.cursor()

        # Iniciem la consulta SQL
        query = """
        SELECT a.NomAlumne, a.Cicle, a.Curs, a.Grup, au.descAula
        FROM alumnat a
        JOIN aula au ON a.IdAula = au.IdAula
        """

        # Afegim filtre per nom si 'contain' està present
        if contain:
            query += " WHERE a.NomAlumne LIKE %s"
            contain_value = f"%{contain}%"
        else:
            contain_value = None

        # Afegim ordenació si 'orderby' està present
        if orderby:
            if orderby.lower() == "asc":
                query += " ORDER BY a.NomAlumne ASC"
            elif orderby.lower() == "desc":
                query += " ORDER BY a.NomAlumne DESC"

        # Afegim la part de paginació
        query += " LIMIT %s OFFSET %s"

        # Executa la consulta amb els paràmetres corresponents
        if contain_value:
            cur.execute(query, (contain_value, limit, skip))
        else:
            cur.execute(query, (limit, skip))

        alumnes = cur.fetchall()

        # Convertim els resultats a un format de diccionari
        alumnes_list = []
        for alumne in alumnes:
            alumnes_list.append({
                "nomAlumne": alumne[0],
                "cicle": alumne[1],
                "curs": alumne[2],
                "grup": alumne[3],
                "descAula": alumne[4],
            })

    except Exception as e:
        return {"status": -1, "message": f"Error de lectura: {e}" }
    
    finally:
        conn.close()

    return alumnes_list


