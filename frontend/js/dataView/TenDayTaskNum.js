function GetTenDayTaskNum() {

// 基于准备好的dom，初始化echarts实例
    var TenDayTaskNumChart = echarts.init(document.getElementById('TenDayTaskNum'));
    var timeArry = []
    var sqlNumArry = []
    var xssNumArry = []
    $.ajax({
        url: 'http://127.0.0.1:8000/Spider/TenDayTaskNum/',
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            // 在这里处理返回的数据，例如将数据传递给 echarts 进行渲染
            data = JSON.parse(data)
            for (var i = 0; i < data.length; i++) {
                timeArry[i] = data[i].time
                sqlNumArry[i] = data[i].sqlNum
                xssNumArry[i] = data[i].xssNum
            }
            // 指定图表的配置项和数据
            var TenDayTaskNum = {
                title: {
                    text: '近十日任务创建统计',
                    left: 'left'
                },
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                        type: 'shadow'
                    }
                },
                legend: {
                    data: ['SQL注入检测任务', 'XSS注入检测任务'],
                    left:'right',
                    top:'top'
                },
                grid: {
                    left: '3%',
                    right: '4%',
                    bottom: '3%',
                    containLabel: true
                },
                xAxis: {
                    type: 'category',
                    data: timeArry,//时间轴
                    axisLabel: {
                        rotate: 45
                    }
                },
                yAxis: {
                    type: 'value'
                },
                series: [{
                    name: 'SQL注入检测任务',
                    type: 'bar',
                    data: sqlNumArry,//sql任务数
                    color: '#1E90FF'
                }, {
                    name: 'XSS注入检测任务',
                    type: 'bar',
                    data: xssNumArry,//xss任务数
                    color: '#FF7F50'
                }]
            };
            TenDayTaskNumChart.setOption(TenDayTaskNum)


        },
        error: function (xhr, textStatus, errorThrow) {
            console.log(textStatus);
        }
    });
}
// GetTenDayTaskNum()
setInterval(GetTenDayTaskNum, 1000);