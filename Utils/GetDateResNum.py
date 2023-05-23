def GetDateResNum(model, start_time, end_time):
    # 查询当天的 SqlResult 数据
    sql_results = model.objects.filter(task_created_time__range=(start_time, end_time))
    # 处理查询结果
    m = 0
    for sql_result in sql_results:
        m += 1
    time = str(start_time).split(' ')[0]
    return {time: m}
