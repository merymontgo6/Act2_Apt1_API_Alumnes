document.addEventListener("DOMContentLoaded", function() {
    // Cridem a l'endpoint de l'API fent un fetch
    fetch('http://127.0.0.1:8000/alumne/listAll')
        .then(response => {
            if (!response.ok) {
                throw new Error("Error a la resposta del servidor");
            }
            return response.json();
        })
        .then(data => {
            console.log(data);
            const alumnesTableBody = document.querySelector("#tablaAlumne tbody");
            alumnesTableBody.innerHTML = ""; // Netejar la taula abans d'afegir res
            
            // Iterar sobre los alumnos y agregarlos al DOM
            data.forEach(alumne => {
                const row = document.createElement("tr");

                const nomAlumne = document.createElement("td");
                nomAlumne.textContent = alumne.nomAlumne;
                row.appendChild(nomAlumne);
                
                // Repetir per tots els altres camps restants que retorna l'endpoint
                const cicle = document.createElement("td");
                cicle.textContent = alumne.cicle;
                row.appendChild(cicle);

                const curs = document.createElement("td");
                curs.textContent = alumne.curs;
                row.appendChild(curs);

                const grup = document.createElement("td");
                grup.textContent = alumne.grup;
                row.appendChild(grup);

                const descAula = document.createElement("td");
                descAula.textContent = alumne.descAula  || alumne.aula?.descAula || "No disponible";; ;
                row.appendChild(descAula);

                alumnesTableBody.appendChild(row);
            });
        })
        .catch(error => {
            console.error("Error capturat:", error);
            alert("Error al carregar la llista d'alumnes");
        });
});