function work_space(obj) //验证是否有空格
{
  var pattern = /\s/;
  if (pattern.test(obj))
    return true;
  else
    return false;
}

function work_isNumber(obj) //验证浮点类型
{
  var pattern = /(^[0-9]$)|(^[1-9]([0-9]*)$)|(^[0-9].([0-9]+)$)|(^[1-9]([0-9]*).([0-9]+)$)/;
  if (pattern.test(obj))
    return true;
  else
    return false;
}

function work_isInteger(obj) //验证整数类型
{ 
  var pattern = /(^[0-9]$)|(^[1-9]([0-9]*)$)/;
  if (pattern.test(obj))
    return true;
  else
    return false;
}

function work_isDate(obj) //验整日期类型(目前只能判断格式，内容需要再扩展)
{
  var pattern = /^([12]\d\d\d)-((0[1-9])|(1[12]))-((0[1-9])|(1[0-9])|(2[0-9])|(3[01]))$/;
  if (pattern.test(obj))
    return true;
  else
    return false;
}

function work_select(slt, opt) //下拉列表选项定位
{
  for (var i = 0; i < slt.length; i++){
  
    if (slt.options[i].value == opt)
      slt.options[i].selected = true;
  }
}
function work_select2(slt, opt) //单选项定位
{
	
  for (var i = 0; i < slt.length; i++){
  	if (slt[i].value == opt){
      slt[i].checked = true;
    }
      
  }
}

function work_calendar() //获取当前日历
{
  calendar = new Date();
  day = calendar.getDay();
  month = calendar.getMonth();
  date = calendar.getDate();
  year = calendar.getYear();
  
  if (year < 100) 
    year = 1900 + year;
    
  cent = parseInt(year/100);
  g = year % 19;
  k = parseInt((cent - 17)/25);
  i = (cent - parseInt(cent/4) - parseInt((cent - k)/3) + 19*g + 15) % 30;
  i = i - parseInt(i/28)*(1 - parseInt(i/28)*parseInt(29/(i+1))*parseInt((21-g)/11));
  j = (year + parseInt(year/4) + i + 2 - cent + parseInt(cent/4)) % 7;
  l = i - j;
  emonth = 3 + parseInt((l + 40)/44);
  edate = l + 28 - 31*parseInt((emonth/4));
  emonth--;
  
  var dayname = new Array (" 星期日", " 星期一", " 星期二", " 星期三", " 星期四", " 星期五", " 星期六");
  var monthname = new Array ("1月","2月","3月","4月","5月","6月","7月","8月","9月","10月","11月","12月" );
  document.write("<font color=#FFFFFF>"+year +"年");
  document.write(monthname[month]);
  document.write(date + "日");
  document.write(dayname[day]+" ");
  
  if ((month == 0) && (date == 1)) document.write("元旦");
  if ((month == 4) && (date == 1)) document.write("国际劳动节");
  if ((month == 4) && (date == 4)) document.write("青年节");
  if ((month == 5) && (date == 1)) document.write("国际儿童节");
  if ((month == 11) && (date == 25)) document.write("圣诞节"); 
  if ((month == 1) && (date == 14)) document.write("情人节");
  if ((month == 2) && (date == 8)) document.write("妇女节");
  if ((month == 2) && (date == 9)) document.write("教师节");
  if ((month == 3) && (date == 1)) document.write("愚人节");
  if ((month == 6) && (date == 1)) document.write("党的生日");
  if ((month == 7) && (date == 1)) document.write("建军节");
  if ((month == 9) && (date == 1)) document.write("国庆节");
  
  document.write("</font>");
}

function work_StringToUnicode(obj)
{
  var s = '';
  for (var i = 0; i < obj.length; i++)
    s = s + obj.charCodeAt(i) + ';';
    
  return s;
}

function work_UnicodeToString(obj)
{
  var code = obj.split(";");

  var s = '';
  for (var i = 0; i < code.length; i++)
    s = s + String.fromCharCode(code[i]);
    
  return s;
}

function work_trim(obj) //去除字符串两边空格
{
  return obj.replace(/(^\s*)|(\s*$)/g, "");
}

function work_datetime() //当前日期时间
{
  var now = new Date();
  var year = now.getYear();
  var month = now.getMonth() + 1;
  var date =  now.getDate();
  var hour =  now.getHours();
  var minute = now.getMinutes();
  
  var second = now.getTime() % 60000;
  second = (second - (second % 1000)) / 1000;
  
  if (month < 10)
    month = "0" + month;
    
  if (date < 10)
    date = "0" + date;
  
  if (hour < 10)
    hour = "0" + hour;
    
  if (minute < 10)
    minute = "0" + minute;

  if (second < 10)
    second = "0" + second;

  var clock = year + "-" + month + "-" + date + " " + hour + ":" + minute + ":" + second;
  return(clock);
}  
