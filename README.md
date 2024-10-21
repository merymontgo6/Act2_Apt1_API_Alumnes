# API d'alumnes
## Activitat 1 - Apartat 2
Aquest programa implementa una API que permet obtenir llistes d'alumnes amb opcions de filtratge, ordenació i paginació, fent servir la base de dades MariaDB per recuperar i gestionar les dades.
Els usuaris poden llistar tots els alumnes amb els detalls específics. 
Les dades de cada alumne inclouen el seu nom, cicle, curs, grup i l'aula assignada. 
Les consultes SQL interactuen amb les taules d'alumnes i aules, garantint la integritat de les dades i retornant missatges d'èxit o error segons el resultat de les operacions.

#### GET "/"
No realitza cap operació de gestió de dades, sinó que simplement indica que el servidor està funcionant correctament.

![image](https://github.com/user-attachments/assets/5388c8c9-6cef-49d9-b8ab-1af11fe9fc51)

#### GET "/alumne/listAll"
La funció read_alumnes en el controlador /alumnes/list està dissenyada per obtenir una llista d'alumnes des de la base de dades.

![image](https://github.com/user-attachments/assets/21e50f4d-886c-49a6-a568-7bcc9ee24e58)

#### GET "/alumnes/list"
Aquest mètode està dissenyat per obtenir una llista d'alumnes des de la base de dades Amb opcions de filtratge, ordenació, i paginació, a partir de paràmetres de consulta (query parameters). 
