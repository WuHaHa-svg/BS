function deleteSon(button) {
    const taskUrlElement = document.getElementById('taskUrl');
    const taskUrl = taskUrlElement.textContent;
    var type = ''
    var url = ''
    try {
        const taskType = document.getElementById('xssScan');
        type = 'xssScan'
        url = 'http://127.0.0.1:8000/XSS/XssDelSon/'
    }
    catch {
        const taskType = document.getElementById('sqlScan');
        type = 'sqlScan'
        url = 'http://127.0.0.1:8000/SQL/SqlDelSon/'
    }
    $.ajax({
        url: url,
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
          taskUrl: taskUrl,
          type: type
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
