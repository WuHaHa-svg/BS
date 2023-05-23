function GetTenDaySqlResGrade() {
    // 基于准备好的dom，初始化echarts实例
    var TenDaySqlResGradeChart = echarts.init(document.getElementById('TenDaySqlResGrade'));
    $.ajax({
        url: 'http://127.0.0.1:8000/Spider/TenDaySqlResGrade/',
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            // 在这里处理返回的数据，例如将数据传递给 echarts 进行渲染
            // data = JSON.parse(data)
            // console.log(data.sql_one)
            var one = data.sql_one
            var two = data.sql_two
            var three = data.sql_three
            var four = data.sql_four
            var five = data.sql_five
            var six = data.sql_six
            var TenDaySqlResGrade = {
                title: {
                    text: 'SQL注入漏洞等级比例',
                    left: 'center',
                    textStyle: {
                        fontSize: 12
                    }
                },
                tooltip: {
                    trigger: 'item',
                    formatter: '{a} <br/>{b}: {c} ({d}%)'
                },
                legend: {
                    orient: 'vertical',
                    left: 'left',
                    top: '11',
                    data: ['等级1', '等级2', '等级3', '等级4', '等级5', '等级6'],
                    textStyle: {
                        fontSize: 8
                    }
                },
                series: [
                    {
                        name: '占比',
                        type: 'pie',
                        radius: ['40%', '70%'],
                        avoidLabelOverlap: false,
                        label: {
                            show: false,
                            position: 'center',
                        },
                        emphasis: {
                            label: {
                                show: true,
                                fontSize: '20',
                                fontWeight: 'bold'
                            }
                        },
                        labelLine: {
                            show: false
                        },
                        data: [
                            { value: one, name: '等级1' },
                            { value: two, name: '等级2' },
                            { value: three, name: '等级3' },
                            { value: four, name: '等级4' },
                            { value: five, name: '等级5' },
                            { value: six, name: '等级6' }
                        ]
                    }
                ]
            };
            TenDaySqlResGradeChart.setOption(TenDaySqlResGrade)
        },
        error: function (xhr, textStatus, errorThrow) {
            console.log(textStatus);
        }
    });
}
// GetTenDaySqlResGrade()
setInterval(GetTenDaySqlResGrade, 1000);