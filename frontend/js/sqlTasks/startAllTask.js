function startAllTask(button) {
    const modal = document.querySelector("#modal");
    const modalText = document.querySelector("#modal-text");
    closeBtn.addEventListener("click", () => {
        modal.style.display = "none";
    });
    $.ajax({        //发起get请求调用后端执行任务
        url: 'http://127.0.0.1:8000/SQL/AllSqlTaskStart/',
        type: 'GET',
        dataType: 'json',
        success: function (data) {      //请求成功则弹窗提示
            console.log(data);
            modalText.textContent = "所有SQL检测任务开始成功！";
            modal.style.display = "block";
        },
        error: function (xhr, textStatus, errorThrown) {        //请求失败则弹窗提示
            console.error(xhr, textStatus, errorThrown);
            modalText.textContent = "请求失败！";
            modal.style.display = "block";
        }
    });
}
