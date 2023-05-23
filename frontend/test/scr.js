const sqlData = [120, 200, 150, 80, 70, 110, 200,52,26,31];
const xssData = [60, 100, 75, 40, 35, 55, 100,54,52,12];

// 定义一个数组，用于存储最近十天的时间
var lastTenDays = [];

// 循环遍历获取最近十天的时间
for (var i = 9; i >= 0; i--) {
  // 获取当前日期的时间戳
  var timestamp = new Date().getTime();
  // 计算 i 天前的日期的时间戳
  var dayTimestamp = timestamp - i * 24 * 3600 * 1000;
  // 将时间戳转换为日期字符串，格式为：yyyy-mm-dd
  var dayStr = new Date(dayTimestamp).toISOString().slice(0, 10);
  // 将日期字符串添加到数组中
  lastTenDays.push(dayStr);
}

// 打印最近十天的时间数组
console.log(lastTenDays);
for (var j = 0; j< 10 ; j++) {
    console.log(lastTenDays[j])
}