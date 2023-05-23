const targetUrlInput = document.querySelector("#targetURL");
const maxDepthInput = document.querySelector("#max_depth");
const sqlScanRadio = document.querySelector("#is_sql_scan");
const xssScanRadio = document.querySelector("#is_xss_scan");
const submitBtn = document.querySelector("#submitBtn");

const modal = document.querySelector("#modal");
const modalText = document.querySelector("#modal-text");
const closeBtn = document.querySelector(".close");

submitBtn.addEventListener("click", (event) => {
    event.preventDefault();
    const targetUrl = targetUrlInput.value;
    const max_depth = maxDepthInput.value;
    const isSqlScan = sqlScanRadio.value;
    const isXssScan = xssScanRadio.value;

    if (!targetUrl) {
        alert("请填写目标URL！");
        return;
    }

    fetch("http://127.0.0.1:8000/GetConfig/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ targetURL: targetUrl, max_depth: max_depth, is_sql_scan: isSqlScan, is_xss_scan: isXssScan}),
    })
        .then((response) => response.json())
        .then((data) => {
            modalText.textContent = data.msg;
            modal.style.display = "block";
        })
        .catch((error) => {
            modalText.textContent = error;
            modal.style.display = "block";
        });
});

closeBtn.addEventListener("click", () => {
    modal.style.display = "none";
});

window.addEventListener("click", (event) => {
    if (event.target == modal) {
        modal.style.display = "none";
    }
});
