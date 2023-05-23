function deleteSonOpt(button) {
    const taskUrlElement = document.getElementById('deleteUrl');
    const taskUrl = taskUrlElement.textContent;
    const closeBtn = document.querySelector(".close");
    const modal = document.querySelector("#modal");
    const modalText = document.querySelector("#modal-text");
    closeBtn.addEventListener("click", () => {
        modal.style.display = "none";
    });
    $.ajax({
        url: 'http://127.0.0.1:8000/XSS/XssDelSon/',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
          taskUrl: taskUrl,
          type: 'xssScan'
        }),
        success: function(data) {
          console.log(data);
          modalText.textContent = "子任务已经删除！";
          modal.style.display = "block";
        },
        error: function(error) {
          console.error(error);
        }
      });
}
