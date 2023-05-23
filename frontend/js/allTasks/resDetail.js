const detail = document.getElementById("detail");   // 获取弹窗元素
const closeIframe = detail.querySelector(".close-detail");// 获取弹窗关闭按钮元素
const content = document.getElementById("content");// 获取弹窗关闭按钮元素
closeIframe.addEventListener("click", () => { // 当点击弹窗关闭按钮时，隐藏弹窗
    detail.style.display = "none";
});

function getRowObj(button) {
    var row = button.parentNode.parentNode;  // 获取当前行
    var url = row.getElementsByTagName('td')[1].textContent;  // 获取当前行的 ID 值
    console.log(url)
    // 发送 POST 请求
    fetch("http://127.0.0.1:8000/Spider/GetRes/", {   //发起请求，获取数据
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        //打包成json字串发送给后端处理
        body: JSON.stringify({ url: url }),
    })
        .then((response) => response.json())
        .then((data) => {
            data = JSON.parse(data)
            if (data.length === 0) {
                content.innerHTML = "暂无数据！"
                content.classList.add("noData")
            } else {
                content.classList.remove("noData")
                content.innerHTML = ""
                for (var i = 0; i < data.length; i++) {
                    url = data[i].fields.url
                    type = data[i].fields.type
                    title = data[i].fields.title
                    injinjection = data[i].fields.injection
                    grade = data[i].fields.grade
                    content.innerHTML += `
                        <div>====结果${i+1}：=====================================<div>
                        <div>url : ${url}</div>
                        <div>type : ${type}</div>
                        <div>title : ${title}</div>
                        <div>injinjection : ${injinjection}</div>
                        <div>grade : ${grade}</div>
                    `
                }
            }

        })
}



// 打开弹窗
function ResDetail(button) {
    detail.style.display = "block";
    getRowObj(button)
}