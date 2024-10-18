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