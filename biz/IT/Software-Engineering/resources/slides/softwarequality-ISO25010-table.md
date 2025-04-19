<style>
  /* Table Styling */
  .quality-table {
    width: 90%;
    max-width: 1200px;
    border-collapse: collapse;
    text-align: left;
    color: #002b36;
  }

  /* Header Row Styling */
  .quality-table th,
  .quality-table td {
    border: 1px solid #586e75;
    padding: 10px;
    vertical-align: top;
  line-height: 1.2; /* Set a consistent line height to accomodate reveal.js and Jekyll layouts*/
  }

  /* Main Header Styling */
  .quality-table .header-row{
    background-color: #268bd2;
    color: #fdf6e3;
    font-size: 0.9em;
    text-align: center;
    font-weight: bold;
    display: none;
  }

  /* Category Headers Styling */
  .quality-table th {
    background-color: #586e75;
    color: #002b36;
    font-weight: bold;
    font-size: 0.6em;
    text-align: center;
  }

  /* Sub-characteristics Cells */
  .quality-table td {
    background-color: #eee8d5;
    color: #073642;
    font-size: 0.5em;
  }

/* Highlight Styling */
.quality-table td span.highlight {
  color: #cb4b16;  /* Solarized Orange for emphasis */
  font-weight: bold;
}

/* Highlight Styling for Header */
.quality-table th.highlight-header {
  background-color: #cb4b16; /* Solarized Orange background */
  color: #fdf6e3; /* Light text for contrast */
  font-weight: bold; /* Ensures boldness */
  border-color: #cb4b16; /* Matches border color with background */
  cursor: pointer; /* Indicates interactivity */
}

/* Highlight Styling for Table Cells */
.quality-table td.highlight {
  background-color: #b58900; /* Solarized Yellow background */
  color: #fdf6e3; /* Light text for contrast */
  font-weight: bold; /* Emphasized text */
  border-color: #b58900; /* Matches border color with background */
  cursor: pointer; /* Indicates interactivity */
}

.quality-table td span {
  display: block; /* Ensure block layout */
  font-size: inherit; /* Inherit font size from parent */
  margin: 0; /* Remove any margin */
  padding: 0; /* Remove any padding */
margin-bottom: 0.5em; /* Adjust spacing as needed */
}


</style>

<table class="quality-table">
  <tr class="header-row">
    <th colspan="9" id="software_product_quality_header"><span>SOFTWARE PRODUCT QUALITY</span></th>
  </tr>
  <tr>
    <th id="functional_suitability_header"><span title="Funktionale Eignung">FUNCTIONAL SUITABILITY</span></th>
    <th id="performance_efficiency_header"><span title="Leistungsfähigkeit">PERFORMANCE EFFICIENCY</span></th>
    <th id="compatibility_header"><span title="Kompatibilität">COMPATIBILITY</span></th>
    <th id="interaction_capability_header"><span title="Interaktionsfähigkeit">INTERACTION CAPABILITY</span></th>
    <th id="reliability_header"><span title="Zuverlässigkeit">RELIABILITY</span></th>
    <th id="security_header"><span title="Sicherheit">SECURITY</span></th>
    <th id="maintainability_header"><span title="Wartbarkeit">MAINTAINABILITY</span></th>
    <th id="flexibility_header"><span title="Flexibilität">FLEXIBILITY</span></th>
    <th id="safety_header"><span title="Sicherheit">SAFETY</span></th>
  </tr>
  <tr>
    <td id="functional_suitability_cell">
      <span title="Vollständig hinsichtlich Softwarefunktionen">Functional Completeness</span>
      <span title="Funktional korrekt">Functional Correctness</span>
      <span title="Angemessene Funktionalität">Functional Appropriateness</span>
    </td>
    <td id="performance_efficiency_cell">
      <span title="Zeitverhalten">Time Behaviour</span>
      <span title="Ressourcen effektiv nutzen">Resource Utilization</span>
      <span title="Kapazitäten schonen">Capacity</span>
    </td>
    <td id="compatibility_cell">
      <span title="Optimale Co-Existenz zu weiterer Software">Co-existence</span>
      <span title="Interoperabilität">Interoperability</span>
    </td>
    <td id="interaction_capability_cell">
      <span title="Optimale Erkennbarkeit">Appropriateness Recognizability</span>
      <span title="Leicht erlernbar und lernfähig">Learnability</span>
      <span title="Gute Bedienbarkeit">Operability</span>
      <span title="Schutz vor Fehlbedienung durch den Nutzer">User Error Protection</span>
      <span title="Ästhetisches User-Interface">User Engagement</span>
      <span title="Leichter Zugang">Inclusivity</span>
      <span title="Leichte Nutzerunterstützung">User Assistance</span>
      <span title="Selbstbeschreibend">Self-descriptiveness</span>
    </td>
    <td id="reliability_cell">
      <span title="Ausgereifte Softwarequalität">Faultlessness</span>
      <span title="Verfügbarkeit">Availability</span>
      <span title="Fehlertoleranz">Fault Tolerance</span>
      <span title="Wiederherstellbarkeit">Recoverability</span>
    </td>
    <td id="security_cell">
      <span title="Datenschutz">Confidentiality</span>
      <span title="Integrität">Integrity</span>
      <span title="Nicht manipulierbar">Non-repudiation</span>
      <span title="Sichere Administration">Accountability</span>
      <span title="Authentizierbarkeit">Authenticity</span>
      <span title="Geschützte Benutzer-Accounts">Resistance</span>
    </td>
    <td id="maintainability_cell">
      <span title="Modularer Aufbau">Modularity</span>
      <span title="Wiederverwendbare Komponenten">Reusability</span>
      <span title="Gute Analyse-Funktionen">Analysability</span>
      <span title="Leicht modifizierbar">Modifiability</span>
      <span title="Umfangreiche Testoptionen">Testability</span>
    </td>
    <td id="flexibility_cell">
      <span title="Gute Adaptivität">Adaptability</span>
      <span title="Leicht zu skalieren">Scalability</span>
      <span title="Einfach zu installieren">Installability</span>
      <span title="Leicht portierbar">Replaceability</span>
    </td>
    <td id="safety_cell">
      <span title="Operative Einschränkungen">Operational Constraint</span>
      <span title="Risikobewertung">Risk Identification</span>
      <span title="Sicherer Betrieb">Fail Safe</span>
      <span title="Gefahrenwarnung">Hazard Warning</span>
      <span title="Sichere Integration">Safe Integration</span>
    </td>
  </tr>
</table>

<script>
// Add event listeners to all <span> elements inside the table
document.querySelectorAll('.quality-table td span').forEach(span => {
  span.addEventListener('click', function () {
    // Toggle the 'highlight' class on the clicked span
    this.classList.toggle('highlight');
  });
});

// Add event listeners to all header <th> elements
document.querySelectorAll('.quality-table th').forEach(header => {
  header.addEventListener('click', function () {
    const headerId = this.id; // Get the header's ID
    const cellId = headerId.replace('_header', '_cell'); // Derive the corresponding cell ID

    // Toggle the 'highlight-header' class on the clicked header <th>
    this.classList.toggle('highlight-header');

    // Find the corresponding cell and toggle the 'highlight' class
    const cell = document.getElementById(cellId);
    if (cell) {
      cell.classList.toggle('highlight');
    }
  });
});
 
</script>
<!-- prettier-ignore-end -->
