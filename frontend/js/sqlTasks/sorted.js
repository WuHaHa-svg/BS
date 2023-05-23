function sortTable(columnIndex) {
    var table = document.getElementById("sql-table");
    var tbody = table.querySelector("tbody");
    var rows = Array.from(tbody.querySelectorAll("tr"));
  
    rows.sort(function(rowA, rowB) {
      var cellA = rowA.querySelectorAll("td")[columnIndex].textContent;
      var cellB = rowB.querySelectorAll("td")[columnIndex].textContent;
      return cellA.localeCompare(cellB);
    });
  
    rows.forEach(function(row) {
      tbody.appendChild(row);
    });
  }
  