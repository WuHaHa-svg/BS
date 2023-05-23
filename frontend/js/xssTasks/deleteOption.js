function deleteOption(button) {
    var row = button.parentNode.parentNode;  // 获取当前行
    var id = row.getElementsByTagName('td')[0].textContent;  // 获取当前行的 ID 值
    var url = row.getElementsByTagName('td')[1].textContent;  // 获取当前行的 URL 值
    const modal = document.getElementById('modal-deleteButtons');
    modal.style.display = "block";
    const taskId = document.getElementById('deleteId');
    taskId.innerHTML = id
    const taskUrl = document.getElementById('deleteUrl');
    taskUrl.innerHTML = url
}

function deleteClose(button) {
    const modal = document.getElementById('modal-deleteButtons');
    modal.style.display = "none";
} 