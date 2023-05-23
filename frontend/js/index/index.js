const menuItems = document.querySelectorAll('.menu-item');
const tabPanes = document.querySelectorAll('.tab-pane');

menuItems.forEach((menuItem, index) => {
  menuItem.addEventListener('click', () => {
    // 切换菜单项的选中状态
    menuItems.forEach(item => {
      item.classList.remove('active');
    });
    menuItem.classList.add('active');

    // 切换内容区域的可见状态
    tabPanes.forEach(pane => {
      pane.classList.remove('active');
    });
    tabPanes[index].classList.add('active');
  });
});


// $(function () {
//   // 页面加载完成后，遍历所有具有data-src属性的容器
//   $('[data-src]').each(function () {
//       var $tabPane = $(this);
//       var src = $tabPane.data('src');
//       // 发送Ajax请求，获取对应的HTML文件内容
//       $.ajax({
//           url: src,
//           dataType: 'html',
//           success: function (html) {
//               // 将HTML内容填充到容器中
//               $tabPane.html(html);
//           }
//       });
//   });
// });

