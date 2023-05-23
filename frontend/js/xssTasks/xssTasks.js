function GetXssTasks() {
    const taskTable = document.getElementById("xss-table");     //获取表格标签
    const url = "http://127.0.0.1:8000/Spider/GetXssTasks/";
    fetch(url)
        .then(response => response.json())
        // 请求成功处理
        .then(data => {
            // 请求成功，但是所得任务列表数据为空列表则表格内容显示无数据
            if (data === "[]") {
                // 获取tbody元素的引用
                var tbody = document.querySelector("#xss-table tbody");
                // 清空tbody中的行
                tbody.innerHTML = "";
                const noDataRow = document.createElement("tr");
                noDataRow.className = "no-data";
                noDataRow.innerHTML = '<td colspan="9">暂无数据</td>';
                taskTable.tBodies[0].appendChild(noDataRow);
            } else {
                // 获取tbody元素的引用
                var tbody = document.querySelector("#xss-table tbody");
                // 清空tbody中的行
                tbody.innerHTML = "";
                const jsonData = JSON.parse(data);
                for (const item of jsonData) {
                    // let item = { fields: { recv_time: '2023-04-29T15:42:19.656Z' } };
                    let created_time = new Date(item.fields.created_time);
                    let created_year = created_time.getFullYear();
                    let created_month = created_time.getMonth() + 1 < 10 ? '0' + (created_time.getMonth() + 1) : created_time.getMonth() + 1;
                    let created_day = created_time.getDate() < 10 ? '0' + created_time.getDate() : created_time.getDate();
                    let created_hour = created_time.getHours() < 10 ? '0' + created_time.getHours() : created_time.getHours();
                    let created_minute = created_time.getMinutes() < 10 ? '0' + created_time.getMinutes() : created_time.getMinutes();
                    let created_second = created_time.getSeconds() < 10 ? '0' + created_time.getSeconds() : created_time.getSeconds();

                    let recv_time = new Date(item.fields.recv_time);
                    let recv_year = recv_time.getFullYear();
                    let recv_month = recv_time.getMonth() + 1 < 10 ? '0' + (recv_time.getMonth() + 1) : recv_time.getMonth() + 1;
                    let recv_day = recv_time.getDate() < 10 ? '0' + recv_time.getDate() : recv_time.getDate();
                    let recv_hour = recv_time.getHours() < 10 ? '0' + recv_time.getHours() : recv_time.getHours();
                    let recv_minute = recv_time.getMinutes() < 10 ? '0' + recv_time.getMinutes() : recv_time.getMinutes();
                    let recv_second = recv_time.getSeconds() < 10 ? '0' + recv_time.getSeconds() : recv_time.getSeconds();

                    let end_time = new Date(item.fields.end_time);
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

                    let statusText = ''; // 定义一个变量用于存储展示的内容

                    if (status === 'INIT') {
                        statusText = '初始化';
                    } else if (status === 'RECV') {
                        statusText = '接收中';
                    } else if (status === 'DONE') {
                        statusText = '完成';
                    } else {
                        statusText = '未知状态';
                    }
                    const row = document.createElement("tr");
                    row.innerHTML = `
            <td id="xss-fields">${item.pk}</td>
            <td id="xss-fields">${item.fields.url}</td>
            <td id="xss-fields">${item.fields.status_xss_scan === 'INIT' ? '刚生成' : item.fields.status_xss_scan === 'RECV' ? '处理中' : '已完成'}</td>                      
            <td id="xss-fields">${created_formatted_time}</td>
            <td id="xss-fields">${recv_formatted_time}</td>
            <td id="xss-fields">${end_formatted_time}</td>
            <td><button id="xss-start" onclick="startOption(this)">开始任务</button></td>
            <td><button id="xss-del" onclick="deleteOption(this)">删除任务</button></td>
            <td><button id="xss-res" onclick="openDetail(this)">查看详情</button></td>
          `;
                    taskTable.tBodies[0].appendChild(row);
                }
            }
        })
        // 请求失败处理，同样设置表格显示暂无数据
        .catch(error => {
            // 获取tbody元素的引用
            var tbody = document.querySelector("#xss-table tbody");
            // 清空tbody中的行
            tbody.innerHTML = "";
            const noDataRow = document.createElement("tr");
            noDataRow.className = "no-data";
            noDataRow.innerHTML = '<td colspan="9">请求失败！</td>';
            taskTable.tBodies[0].appendChild(noDataRow);
        });
}
GetXssTasks()
// setInterval(GetXssTasks, 1000);//每一秒刷新一次任务列表
