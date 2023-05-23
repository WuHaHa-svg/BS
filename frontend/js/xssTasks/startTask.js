
function startTask(button) {
    // var row = button.parentNode.parentNode;  // 获取当前行
    var id = document.getElementById('startId').textContent;
    const closeBtn = document.querySelector(".close");
    const modal = document.querySelector("#modal");
    const modalText = document.querySelector("#modal-text");
    closeBtn.addEventListener("click", () => {
        modal.style.display = "none";
    });

    $.ajax({
        url: 'http://127.0.0.1:8000/XSS/XssTaskStart/',
        type: 'POST',
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify({ id: id }),
        success: function(data) {
            modalText.textContent = data.msg;
            modal.style.display = "block";
        },
        error: function(xhr, textStatus, errorThrown) {
            console.error(errorThrown);
        }
    });
}

