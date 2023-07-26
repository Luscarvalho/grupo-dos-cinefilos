function searchFilm() {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("search");
    filter = input.value.toUpperCase();
    table = document.getElementById("table");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0];
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}

function sortTable(columnIndex) {
    const table = document.getElementById("table");
    const rows = Array.from(table.rows).slice(1);
    const isAscending = table.dataset.sortOrder === "asc" || table.dataset.sortOrder === undefined;

    rows.sort((rowA, rowB) => {
        const cellA = rowA.cells[columnIndex].textContent.toLowerCase();;
        const cellB = rowB.cells[columnIndex].textContent.toLowerCase();;

        if (cellA < cellB) {
            return isAscending ? -1 : 1;
        } else if (cellA > cellB) {
            return isAscending ? 1 : -1;
        } else {
            return 0;
        }
    });
    rows.forEach(row => table.deleteRow(row.rowIndex));
    rows.forEach(row => table.tBodies[0].appendChild(row));
    table.dataset.sortOrder = isAscending ? "desc" : "asc";
}