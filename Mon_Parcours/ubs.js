document.addEventListener("DOMContentLoaded", () => {
    const descriptions = {
        "droit.jpg": "Installée dans des bâtiments modernes sur le campus de Tohannic.",
        "paquebot.jpg" : "La Faculté, située sur le campus de Lorient, accueille chaque année environ 2000 étudiant·es. Nous proposons des formations de la licence au doctorat dans les domaines des lettres & langues et sciences humaines & sociales.",
        "sciences.jpg" : "À la rentrée universitaire de septembre 2023, nous avons augmenté nos effectifs,  essentiellement au niveau Licence (L1, L2 et L3), de plus de 15% pour atteindre près de 3000 étudiants, en Licence et Master, dont 500 hors les murs.",
        "ensibs.jpg" : "Implantée au sein de l'Université de Bretagne-Sud, l’École Nationale Supérieure d’Ingénieurs de Bretagne-Sud (ENSIBS) propose six spécialités",
        "iut-vannes.jpg" : "Des formations dans les domaines de la Gestion, du Commerce, de l’Informatique, de la Science des Données.",
        "iut-pontivy.jpg" : "L’IUT Lorient - Pontivy, c'est : 2 sites, 6 Bachelors Universitaires de Technologie (B.U.T.), 3 licences professionnelles et 650 étudiants.",
        "iae.jpg" : "L'IAE Bretagne Sud propose une offre de formation diversifiée."
    };

    const zone = document.getElementById("description-text");

    document.addEventListener("click", (e) => {
        const nom= e.target.getAttribute("src");
        zone.textContent = descriptions[nom] || "Aucune description disponible";
    });
});