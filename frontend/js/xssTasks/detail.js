const detail = document.getElementById("detail");   // 获取弹窗元素
const closeIframe = detail.querySelector(".close-detail");// 获取弹窗关闭按钮元素
closeIframe.addEventListener("click", () => { // 当点击弹窗关闭按钮时，隐藏弹窗
  detail.style.display = "none";
});
function getRowObj(button) {
  var row = button.parentNode.parentNode;  // 获取当前行
  var id = row.getElementsByTagName('td')[0].textContent;  // 获取当前行的 ID 值
  // 发送 POST 请求
  fetch("http://127.0.0.1:8000/XSS/GetInfo/", {   //发起请求，获取数据
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    //打包成json字串发送给后端处理
    body: JSON.stringify({ id: id }),
  })
    .then((response) => response.json())
    .then((data) => {
      data = JSON.parse(data)       //解析数据
      console.log(data)
      const taskIdElement = document.getElementById('taskId');
      taskIdElement.innerHTML = data[0].pk
      const taskUrl = document.getElementById('taskUrl');
      taskUrl.innerHTML = data[0].fields.url
      const xssScan = document.getElementById('xssScan');
      xssScan.innerHTML = `${data[0].fields.is_xss_scan === "Y" ? "是" : "否"}`;
      const depth = document.getElementById('depth');
      depth.innerHTML = data[0].fields.depth
      const maxDepth = document.getElementById('maxDepth');
      maxDepth.innerHTML = data[0].fields.max_depth
      const statusXss = document.getElementById('statusXss');
      statusXss.innerHTML = `${data[0].fields.status_xss_scan === 'INIT' ? '刚生成' : data[0].fields.status_xss_scan === 'RECV' ? '处理中' : '已完成'}`;
      const superUrl = document.getElementById('superUrl');
      superUrl.innerHTML = data[0].fields.super_url
      let created_time = new Date(data[0].fields.created_time);
      let created_year = created_time.getFullYear();
      let created_month = created_time.getMonth() + 1 < 10 ? '0' + (created_time.getMonth() + 1) : created_time.getMonth() + 1;
      let created_day = created_time.getDate() < 10 ? '0' + created_time.getDate() : created_time.getDate();
      let created_hour = created_time.getHours() < 10 ? '0' + created_time.getHours() : created_time.getHours();
      let created_minute = created_time.getMinutes() < 10 ? '0' + created_time.getMinutes() : created_time.getMinutes();
      let created_second = created_time.getSeconds() < 10 ? '0' + created_time.getSeconds() : created_time.getSeconds();

      let recv_time = new Date(data[0].fields.recv_time);
      let recv_year = recv_time.getFullYear();
      let recv_month = recv_time.getMonth() + 1 < 10 ? '0' + (recv_time.getMonth() + 1) : recv_time.getMonth() + 1;
      let recv_day = recv_time.getDate() < 10 ? '0' + recv_time.getDate() : recv_time.getDate();
      let recv_hour = recv_time.getHours() < 10 ? '0' + recv_time.getHours() : recv_time.getHours();
      let recv_minute = recv_time.getMinutes() < 10 ? '0' + recv_time.getMinutes() : recv_time.getMinutes();
      let recv_second = recv_time.getSeconds() < 10 ? '0' + recv_time.getSeconds() : recv_time.getSeconds();

      let end_time = new Date(data[0].fields.end_time);
      let end_year = end_time.getFullYear();
      let end_month = end_time.getMonth() + 1 < 10 ? '0' + (end_time.getMonth() + 1) : end_time.getMonth() + 1;
      let end_day = end_time.getDate() < 10 ? '0' + end_time.getDate() : end_time.getDate();
      let end_hour = end_time.getHours() < 10 ? '0' + end_time.getHours() : end_time.getHours();
      let end_minute = end_time.getMinutes() < 10 ? '0' + end_time.getMinutes() : end_time.getMinutes();
      let end_second = end_time.getSeconds() < 10 ? '0' + end_time.getSeconds() : end_time.getSeconds();

      let created_formatted_time = created_year + '-' + created_month + '-' + created_day + ' ' + created_hour + ':' + created_minute + ':' + created_second;

      let recv_formatted_time = ''
      if (recv_year === 1970) {
        recv_formatted_time = ''
      } else {
        recv_formatted_time = recv_year + '-' + recv_month + '-' + recv_day + ' ' + recv_hour + ':' + recv_minute + ':' + recv_second;
      }

      let end_formatted_time = ''
      if (end_year === 1970) {
        end_formatted_time = ''
      } else {
        end_formatted_time = end_year + '-' + end_month + '-' + end_day + ' ' + end_hour + ':' + end_minute + ':' + end_second;
      }
      const create = document.getElementById('create');
      create.innerHTML = created_formatted_time
      const start = document.getElementById('start');
      start.innerHTML = recv_formatted_time
      const end = document.getElementById('end');
      end.innerHTML = end_formatted_time
      const sonNum = document.getElementById('sonNum');
      sonNum.innerHTML = data[0].fields.son_num
    })
    .catch((error) => {
      console.log(error)
    });
}

// 打开弹窗
function openDetail(button) {
  detail.style.display = "block";
  getRowObj(button)
}