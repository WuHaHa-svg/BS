function startAllTask(button) {
    const modal = document.querySelector("#modal");
    const modalText = document.querySelector("#modal-text");
    closeBtn.addEventListener("click", () => {
        modal.style.display = "none";
    });
    $.ajax({
        url: 'http://127.0.0.1:8000/XSS/AllXssTaskStart/',
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            console.log(data);
            modalText.textContent = "所有XSS检测任务开始成功！";
            modal.style.display = "block";
        },
        error: function (xhr, textStatus, errorThrown) {
            console.error(xhr, textStatus, errorThrown);
            modalText.textContent = "请求失败！";
            modal.style.display = "block";
        }
    });
}
