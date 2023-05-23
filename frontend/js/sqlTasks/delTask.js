// const modal = document.querySelector("#modal");
// const modalText = document.querySelector("#modal-text");
// const closeBtn = document.querySelector(".close");
// function deleteRow(button) {
//     try {
//         var row = button.parentNode.parentNode;  // 获取当前行
//         var id = row.getElementsByTagName('td')[0].textContent;  // 获取当前行的 ID 值
//     } catch {
//         var id = document.getElementById('taskId').textContent;
//     }
//     // var row = button.parentNode.parentNode;  // 获取当前行
//     // var id = row.getElementsByTagName('td')[0].textContent;  // 获取当前行的 ID 值
//     var xhr = new XMLHttpRequest();
//     xhr.open('POST', 'http://127.0.0.1:8000/Spider/DelSqlTask/', true);
//     xhr.setRequestHeader('Content-Type', 'application/json');
//     xhr.onreadystatechange = function () {
//         if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
//             modalText.textContent = "删除成功！";
//             modal.style.display = "block";
//             try {
//                 var row = button.parentNode.parentNode;  // 获取当前行
//                 var id = row.getElementsByTagName('td')[0].textContent;  // 获取当前行的 ID 值
//                 row.parentNode.removeChild(row);  // 从表格中删除当前行
//             } catch {
//                 var id = document.getElementById('taskId').textContent;
//             }
//         }
//     };
//     xhr.send(JSON.stringify({ id: id }));  // 发送 POST 请求，包含当前行的 ID 值
// }

// closeBtn.addEventListener("click", () => {
//     modal.style.display = "none";
// });

// window.addEventListener("click", (event) => {
//     if (event.target == modal) {
//         modal.style.display = "none";
//     }
// });

const closeBtn = document.querySelector(".close");
function deleteTask(button) {
    var id = document.getElementById('deleteId').textContent;
    const modal = document.querySelector("#modal");
    const modalText = document.querySelector("#modal-text");

    $.ajax({
        url: 'http://127.0.0.1:8000/Spider/DelSqlTask/',
        type: 'POST',
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify({ id: id }),
        success: function (data) {
            modalText.textContent = "任务删除成功！";
            modal.style.display = "block";
        },
        error: function (xhr, textStatus, errorThrown) {
            console.error(errorThrown);
        }
    });
}

closeBtn.addEventListener("click", () => {
    modal.style.display = "none";
});