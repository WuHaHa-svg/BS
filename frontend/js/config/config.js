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
    const targetUrl = targetUrlInput.value;         //目标URL
    const max_depth = maxDepthInput.value;          //最大检测深度
    const isSqlScan = sqlScanRadio.value;           //SQL注入检测开关
    const isXssScan = xssScanRadio.value;           //XSS注入检测开关

    if (!targetUrl) {
        modalText.textContent = "请填写目标URL！";
            modal.style.display = "block";
        return;
    }

    fetch("http://127.0.0.1:8000/Spider/GetConfig/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        //打包成json字串发送给后端处理
        body: JSON.stringify({ targetURL: targetUrl, max_depth: max_depth, is_sql_scan: isSqlScan, is_xss_scan: isXssScan}),
    })
        .then((response) => response.json())
        .then((data) => {
            console.log(data.msg)
            modalText.textContent = "参数处理成功！";       //成功响应信息
            modal.style.display = "block";
        })
        .catch((error) => {
            modalText.textContent = "请求失败！";           //失败信息
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
