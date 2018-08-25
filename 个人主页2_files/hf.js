var listactive = "listactive01";

//个性化选择预览
function work_ys(obj)
{
  var_ys = obj;
  var which = obj;
  var bodybg,
      topbg,
      btncolor,
      bgimg,
      bannerimg,
      lxfsbtncolor;

	switch (Number(which)) {
		case 1:
			bodybg = "#ECECEC";
			topbg = "#798399";
			btncolor = "#939fb8";
			bgimg = "url(" + var_path + "web/hf/img0_02.jpg)";
			bannerimg = "url(" + var_path + "web/hf/img0_03.jpg)";
			lxfsbtncolor = "#939fb8";
			listactive = "listactive20";
			break;
		case 2:
			bodybg = "#fffdca";
			topbg = "#716f24";
			btncolor = "#b5b136";
			bgimg = "url(" + var_path + "web/hf/bgimg-02.jpg)";
			bannerimg = "url(" + var_path + "web/hf/banner-02.jpg)";
			lxfsbtncolor = "#858228";
			listactive = "listactive02";
			break;
		case 3:
			bodybg = "#d6c5a7";
			topbg = "#665f4f";
			btncolor = "#9b8353";
			bgimg = "url(" + var_path + "web/hf/bgimg-03.jpg)";
			bannerimg = "url(" + var_path + "web/hf/banner-03.jpg)";
			lxfsbtncolor = "#826e46";
			listactive = "listactive03";
			break;
    case 4:
      bodybg = "#ebeceb";
      topbg = "#1d324e";
      btncolor = "#204473";
      bgimg = "url(" + var_path + "web/hf/bgimg-04.jpg)";
      bannerimg = "url(" + var_path + "web/hf/banner-04.jpg)";
      lxfsbtncolor = "#204473";
			listactive = "listactive04";
			break;
    case 5:
      bodybg = "#edfdfb";
      topbg = "#46886e";
      btncolor = "#78b19b";
      bgimg = "url(" + var_path + "web/hf/bgimg-05.jpg)";
      bannerimg = "url(" + var_path + "web/hf/banner-05.jpg)";
      lxfsbtncolor = "#78b19b";
			listactive = "listactive05";
			break;
    case 6:
      bodybg = "#eaeef6";
      topbg = "#2462ae";
      btncolor = "#3075c9";
      bgimg = "url(" + var_path + "web/hf/bgimg-06.jpg)";
      bannerimg = "url(" + var_path + "web/hf/banner-06.jpg)";
      lxfsbtncolor = "#3075c9";
			listactive = "listactive06";
			break;
    case 7:
      bodybg = "#f6f6e4";
      topbg = "#b0ac90";
      btncolor = "#cdc8a9";
      bgimg = "url(" + var_path + "web/hf/bgimg-07.jpg)";
      bannerimg = "url(" + var_path + "web/hf/banner-07.jpg)";
      lxfsbtncolor = "#cdc8a9";
			listactive = "listactive07";
			break;
    case 8:
      bodybg = "#e9f0f5";
      topbg = "#4d697a";
      btncolor = "#628ca4";
      bgimg = "url(" + var_path + "web/hf/bgimg-08.jpg)";
      bannerimg = "url(" + var_path + "web/hf/banner-08.jpg)";
      lxfsbtncolor = "#628ca4";
			listactive = "listactive08";
			break;
    case 9:
      bodybg = "#ffffff";
      topbg = "#e04421";
      btncolor = "#f25e3d";
      bgimg = "url(" + var_path + "web/hf/bgimg-09.jpg)";
      bannerimg = "url(" + var_path + "web/hf/banner-09.jpg)";
      lxfsbtncolor = "#f25e3d";
			listactive = "listactive09";
			break;
		case 11:
			bodybg = "#ffddc7";
			topbg = "#d97058";
			btncolor = "#ffc156";
			bgimg = "url(" + var_path + "web/hf/bgimg-01.jpg)";
			bannerimg = "url(" + var_path + "web/hf/banner-01.jpg)";
			lxfsbtncolor = "#bd8e3e";
			listactive = "listactive01";
			break;
		case 13:
			bodybg = "#fff";
			topbg = "#1f5992";
			btncolor = "#276fb5";
			bgimg = "url(" + var_path + "web/hf/1-1.jpg)";
			bannerimg = "url(" + var_path + "web/hf/1-11.jpg)";
			lxfsbtncolor = "#276fb5";
			listactive = "listactive11";
			break;
		case 14:
			bodybg = "#fff";
			topbg = "#1d61ec";
			btncolor = "#296fff";
			bgimg = "url(" + var_path + "web/hf/4-4.jpg)";
			bannerimg = "url(" + var_path + "web/hf/4-44.jpg)";
			lxfsbtncolor = "#296fff";
			listactive = "listactive14";
			break;
		case 21:
			bodybg = "#ECECEC";
			topbg = "#89551d";
			btncolor = "#a9671f";
			bgimg = "url(" + var_path + "web/hf/img1_02.jpg)";
			bannerimg = "url(" + var_path + "web/hf/img1_03.jpg)";
			lxfsbtncolor = "#a9671f";
			listactive = "listactive21";
			break;
		case 22:
			bodybg = "#ECECEC";
			topbg = "#d18524";
			btncolor = "#e3932d";
			bgimg = "url(" + var_path + "web/hf/img2_02.jpg)";
			bannerimg = "url(" + var_path + "web/hf/img2_03.jpg)";
			lxfsbtncolor = "#e3932d";
			listactive = "listactive22";
			break;
		case 23:
			bodybg = "#fff";
			topbg = "#84828d";
			btncolor = "#8c8b92";
			bgimg = "url(" + var_path + "web/hf/img3_02.jpg)";
			bannerimg = "url(" + var_path + "web/hf/img3_03.jpg)";
			lxfsbtncolor = "#8c8b92";
			listactive = "listactive23";
			break;
		case 24:
			bodybg = "#ECECEC";
			topbg = "#a3408f";
			btncolor = "#d254b9";
			bgimg = "url(" + var_path + "web/hf/img4_02.jpg)";
			bannerimg = "url(" + var_path + "web/hf/img4_03.jpg)";
			lxfsbtncolor = "#d254b9";
			listactive = "listactive24";
			break;
		case 25:
			bodybg = "#ECECEC";
			topbg = "#0c1036";
			btncolor = "#29317f";
			bgimg = "url(" + var_path + "web/hf/img5_02.jpg)";
			bannerimg = "url(" + var_path + "web/hf/img5_03.jpg)";
			lxfsbtncolor = "#29317f";
			listactive = "listactive25";
			break;
		case 26:
			bodybg = "#ECECEC";
			topbg = "#565b45";
			btncolor = "#7c855e";
			bgimg = "url(" + var_path + "web/hf/img6_02.jpg)";
			bannerimg = "url(" + var_path + "web/hf/img6_03.jpg)";
			lxfsbtncolor = "#7c855e";
			listactive = "listactive26";
			break;
		case 27:
			bodybg = "#ECECEC";
			topbg = "#494546";
			btncolor = "#746e6f";
			bgimg = "url(" + var_path + "web/hf/img7_02.jpg)";
			bannerimg = "url(" + var_path + "web/hf/img7_03.jpg)";
			lxfsbtncolor = "#746e6f";
			listactive = "listactive27";
			break;
		case 31:
			bodybg = "#ECECEC";
			topbg = "#f69c5c";
			btncolor = "#f8ae7a";
			bgimg = "url(" + var_path + "web/hf/img31_02.jpg)";
			bannerimg = "url(" + var_path + "web/hf/img31_03.jpg)";
			lxfsbtncolor = "#f8ae7a";
			listactive = "listactive31";
			break;
		case 32:
			bodybg = "#ECECEC";
			topbg = "#6d6e25";
			btncolor = "#8d8e25";
			bgimg = "url(" + var_path + "web/hf/img32_02.jpg)";
			bannerimg = "url(" + var_path + "web/hf/img32_03.jpg)";
			lxfsbtncolor = "#8d8e25";
			listactive = "listactive32";
			break;
		case 33:
			bodybg = "#ECECEC";
			topbg = "#313c47";
			btncolor = "#475562";
			bgimg = "url(" + var_path + "web/hf/img33_02.jpg)";
			bannerimg = "url(" + var_path + "web/hf/img33_03.jpg)";
			lxfsbtncolor = "#475562";
			listactive = "listactive33";
			break;
		case 34:
			bodybg = "#ECECEC";
			topbg = "#494546";
			btncolor = "#746e6f";
			bgimg = "url(" + var_path + "web/hf/img34_02.jpg)";
			bannerimg = "url(" + var_path + "web/hf/img34_03.jpg)";
			lxfsbtncolor = "#746e6f";
			listactive = "listactive34";
			break;
		case 35:
			bodybg = "#ECECEC";
			topbg = "#102633";
			btncolor = "#1d4a65";
			bgimg = "url(" + var_path + "web/hf/img35_02.jpg)";
			bannerimg = "url(" + var_path + "web/hf/img35_03.jpg)";
			lxfsbtncolor = "#1d4a65";
			listactive = "listactive35";
			break;
		case 36:
			bodybg = "#ECECEC";
			topbg = "#fea701";
			btncolor = "#feba39";
			bgimg = "url(" + var_path + "web/hf/img36_02.jpg)";
			bannerimg = "url(" + var_path + "web/hf/img36_03.jpg)";
			lxfsbtncolor = "#feba39";
			listactive = "listactive36";
			break;
		case 37:
			bodybg = "#ECECEC";
			topbg = "#1f5992";
			btncolor = "#276fb5";
			bgimg = "url(" + var_path + "web/hf/img37_02.jpg)";
			bannerimg = "url(" + var_path + "web/hf/img37_03.jpg)";
			lxfsbtncolor = "#276fb5";
			listactive = "listactive37";
			break;
		case 38:
			bodybg = "#ECECEC";
			topbg = "#a82b3a";
			btncolor = "#c73244";
			bgimg = "url(" + var_path + "web/hf/img38_02.jpg)";
			bannerimg = "url(" + var_path + "web/hf/img38_03.jpg)";
			lxfsbtncolor = "#c73244";
			listactive = "listactive38";
			break;
	}
	$(".hf-bodybg").css("background-color", bodybg);
	$(".hf-topbg,.bqxz").css("background-color", topbg);
	//$(".hf-bordor").css("border-color", topbg);
	$(".hf-btncolor").css("background-color", btncolor);
	$(".hf-bgimg").css("background-image", bgimg);
	$(".hf-bannerimg").css("background-image", bannerimg);
	$(".hf-lxfsbtn").css("background-color", lxfsbtncolor);
	$(".hf-color").css("color", topbg);
	$(".biaoqianline a").removeClass();
	$(".biaoqianline a").eq(0).addClass(listactive);
	$(".biaoqianline a").click(function(){
    $(".biaoqianline a").removeClass();
    $(this).addClass(listactive);
  });
  
  try {
    if (typeof(var_yqid) != "undefined"){ 
      work_dh(var_yqid);
    }
  }catch(e){}
}
//个性化选择保存
function work_submit(yhid) {
  which = var_ys;
  
  $.ajax({
    type: "post",
    url: var_path + "web/stage2/grxx_do.jsp",
    data: {
      operate: "ys",
      ys: which,
      yhid: yhid
    },
    success: function(data) {
      $('#myModal').modal('hide');
      var_java_ys = which;
      work_ys(which);
      work_dh(var_yqid);
    }
  });
}