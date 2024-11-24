
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
  display: block; /* Treat each line like a block for spacing */
  margin-bottom: 0.6em; /* Adjust spacing as needed */
}

</style>

<table class="quality-table">
  <tr class="header-row">
    <th colspan="9" id="software_product_quality_header"><span>SOFTWARE PRODUCT QUALITY</span></th>
  </tr>
  <tr>
    <th id="functional_suitability_header"><span>FUNCTIONAL SUITABILITY</span></th>
    <th id="performance_efficiency_header"><span>PERFORMANCE EFFICIENCY</span></th>
    <th id="compatibility_header"><span>COMPATIBILITY</span></th>
    <th id="interaction_capability_header"><span>INTERACTION CAPABILITY</span></th>
    <th id="reliability_header"><span>RELIABILITY</span></th>
    <th id="security_header"><span>SECURITY</span></th>
    <th id="maintainability_header"><span>MAINTAINABILITY</span></th>
    <th id="flexibility_header"><span>FLEXIBILITY</span></th>
    <th id="safety_header"><span>SAFETY</span></th>
  </tr>
  <tr>
    <td id="functional_suitability_cell">
      <span>Functional Completeness</span>
      <span>Functional Correctness</span>
      <span>Functional Appropriateness</span>
    </td>
    <td id="performance_efficiency_cell">
      <span>Time Behaviour</span>
      <span>Resource Utilization</span>
      <span>Capacity</span>
    </td>
    <td id="compatibility_cell">
      <span>Co-existence</span>
      <span>Interoperability</span>
    </td>
    <td id="interaction_capability_cell">
      <span>Appropriateness Recognizability</span>
      <span>Learnability</span>
      <span>Operability</span>
      <span>User Error Protection</span>
      <span>User Engagement</span>
      <span>Inclusivity</span>
      <span>User Assistance</span>
      <span>Self-descriptiveness</span>
    </td>
    <td id="reliability_cell">
      <span>Faultlessness</span>
      <span>Availability</span>
      <span>Fault Tolerance</span>
      <span>Recoverability</span>
    </td>
    <td id="security_cell">
      <span>Confidentiality</span>
      <span>Integrity</span>
      <span>Non-repudiation</span>
      <span>Accountability</span>
      <span>Authenticity</span>
      <span>Resistance</span>
    </td>
    <td id="maintainability_cell">
      <span>Modularity</span>
      <span>Reusability</span>
      <span>Analysability</span>
      <span>Modifiability</span>
      <span>Testability</span>
    </td>
    <td id="flexibility_cell">
      <span>Adaptability</span>
      <span>Scalability</span>
      <span>Installability</span>
      <span>Replaceability</span>
    </td>
    <td id="safety_cell">
      <span>Operational Constraint</span>
      <span>Risk Identification</span>
      <span>Fail Safe</span>
      <span>Hazard Warning</span>
      <span>Safe Integration</span>
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
<p>Source: iso25000.com</p>
<!-- prettier-ignore-end -->