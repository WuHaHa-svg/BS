function GetTaskHdr() {

    // 基于准备好的dom，初始化echarts实例
    var TaskHdrChart = echarts.init(document.getElementById('TaskHdr'));
    var timeArry = []
    $.ajax({
        url: 'http://127.0.0.1:8000/Spider/TaskHdr/',
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            // 在这里处理返回的数据，例如将数据传递给 echarts 进行渲染
            // 指定图表的配置项和数据
            var TaskHdr = {
                title: {
                    text: 'SQL注入检测任务和XSS注入检测任务总览',
                    left: 'left'
                },
                tooltip: {},
                legend: {
                    data: ['任务数', '漏洞数'],
                    left: 'right'
                },
                xAxis: {
                    type: 'value'
                },
                yAxis: {
                    type: 'category',
                    data: ['XSS注入', 'SQL注入']
                },
                series: [
                    {
                        name: '任务数',
                        type: 'bar',
                        data: [data.XssTask, data.SqlTask]
                    },
                    {
                        name: '漏洞数',
                        type: 'bar',
                        data: [data.XssNum, data.SqlNum]
                    }
                ]
            };
            // 使用刚指定的配置项和数据显示图表。
            TaskHdrChart.setOption(TaskHdr);
        },
        error: function (xhr, textStatus, errorThrow) {
            console.log(textStatus);
        }
    });
}
// GetTaskHdr()
setInterval(GetTaskHdr, 1000);