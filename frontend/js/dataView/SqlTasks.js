function GetSqlTasks() {
    // 基于准备好的dom，初始化echarts实例
    var SqlTasksChart = echarts.init(document.getElementById('SqlTasks'));
    $.ajax({
        url: 'http://127.0.0.1:8000/Spider/SqlTasks/',
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            // 饼图的配置项和数据
            var SqlTasks = {
                title: {
                    text: '当前SQL注入任务饼图',
                    x: 'center',
                    textStyle: {
                        fontSize: 12,
                        fontWeight: 'bold'
                    }
                },
                tooltip: {
                    trigger: 'item',
                    formatter: '{a} <br/>{b}: {c} ({d}%)'
                },
                legend: {
                    orient: 'vertical',
                    top: 8,
                    left: 10,
                    data: ['刚生成', '处理中', '已完成'],
                    textStyle: {
                        fontSize: 8
                    }
                },
                series: [
                    {
                        name: '当前SQL注入任务',
                        type: 'pie',
                        radius: '55%',
                        center: ['50%', '60%'],
                        data: [
                            { value: data.INIT, name: '刚生成' },
                            { value: data.RECV, name: '处理中' },
                            { value: data.DONE, name: '已完成' }
                        ],
                        emphasis: {
                            itemStyle: {
                                shadowBlur: 10,
                                shadowOffsetX: 0,
                                shadowColor: 'rgba(0, 0, 0, 0.5)'
                            }
                        }
                    }
                ]
            };
            // 使用刚指定的配置项和数据显示图表
            SqlTasksChart.setOption(SqlTasks);
        },
        error: function (xhr, textStatus, errorThrow) {
            console.log(textStatus);
        }
    });

}
// GetSqlTasks()

setInterval(GetSqlTasks, 1000);