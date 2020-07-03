log("*   ╉ The Animal Protecting ╊");
log("*　　┏┓　　　┏┓+ +");
log("*　┏┛┻━━━┛┻┓ + +");
log("*　┃　　　　　　　┃");
log("*　┃　　　━　　　┃ ++ + + +");
log("*　████━████ 　+");
log("*　┃　　　　　　　┃ +");
log("*　┃　　　┻　　　┃")
log("*　┃　　　　　　　┃ + +");
log("*　┗━┓　　　┏━┛");
log("*　　　┃　　　┃");
log("*　　　┃　　　┃ + + + +");
log("*　　　┃　　　┃　　　　");
log("*　　　┃　　　┃ + 　");
log("*　　　┃　　　┃")
log("*　　　┃　　　┃　　+");
log("*　　　┃　　　┗━━━┓ + +")
log("*　　　┃　　　　　　　┣┓+ + + ");
log("*　　　┃　　　　　　　┏┛+ +");
log("*　　　┗┓┓┏━┳┓┏┛ + ");
log("*　　　　┃┫┫　┃┫┫");
log("*　　　　┗┻┛　┗┻┛+ + ");
log("*    Code is far away from bug!");
log("*        神兽保佑,代码无bug");
try {
    if (contextPASS != undefined) {
        log("[?]定时任务启动脚本");
    }
} catch (e) {
    contextPASS = 0;
}
if (contextPASS == 0) {
    dialogs_js();
} else {
    context_Manualstate = 0;
    Set_Back_way();
}

function dialogs_js() {
    var ScriptVersion = ("Beta1.2"); //版本
    log("软件脚本已开始运行，如果没有弹出菜单请强行停止再打开本软件！");
    var options_ = ["?? 开始运行脚本", "?? 计时运行脚本", "? 定时运行脚本", "? 停止运行脚本", "?? 返回方法设置", "?? 手动打开模式", "?? 吐司/日志切换"]
    var i = dialogs.select("*+*+*+* 橘衫の脚本 *+*+*+*\n*+*+*+*  Orange Js *+*+*+*\n\n欢迎使用 (?????)?" + "\n" + "“种豆得豆自动脚本”" + ScriptVersion + "\n请选择一个要进行的选项", options_);
    if (i < 0) {
        toastLog("没有选择，如需关闭对话框\n  请选择“停止运行脚本”");
        dialogs_js();
    } else if (i == 0) {
        toastLog(options_[i]);
        context_Manualstate = 0;
        Set_Back_way();
    } else if (i == 3) {
        toastLog(options_[i]);
        exit();
    } else if (i == 1) {
        toastLog("请稍候，正在检测权限...");
        context_Manualstate = 0;
        toastLog(options_[i]);
        device.keepScreenDim();
        toastLog("检测权限设置……");
        context_Manualstate = 0;
        toastLog("等待无障碍权限开启……\n您必须手动授予本软件无障碍权限\n否则本软件将无法工作！");
        auto.waitFor();
        toastLog("无障碍权限已开启" + "\n" + "继续运行脚本……");
        sleep(2000);
        toastLog("为保证脚本正常运行\n请授予本软件悬浮窗权限");
        sleep(2000);
        var test_rawWindow = floaty.rawWindow(
            <frame gravity="center" bg="#00000000"/>
        );
        test_rawWindow.setSize(-1, -1);
        test_rawWindow.setTouchable(false);
        setTimeout(() => {
            test_rawWindow.close();
        }, 1000);
        toastLog("悬浮窗权限已开启！");
        sleep(2000);
        wait_Time_over();
    } else if (i == 2) {
        toastLog("请稍候，正在检测权限...");
        context_Manualstate = 0;
        toastLog(options_[i]);
        device.keepScreenDim();
        toastLog("检测权限设置……");
        context_Manualstate = 0;
        toastLog("等待无障碍权限开启……\n您必须手动授予本软件无障碍权限\n否则本软件将无法工作！");
        auto.waitFor();
        toastLog("无障碍权限已开启" + "\n" + "继续运行脚本……");
        sleep(2000);
        toastLog("为保证脚本正常运行\n请授予本软件悬浮窗权限");
        sleep(2000);
        var test_rawWindow = floaty.rawWindow(
            <frame gravity="center" bg="#00000000"/>
        );
        test_rawWindow.setSize(-1, -1);
        test_rawWindow.setTouchable(false);
        setTimeout(() => {
            test_rawWindow.close();
        }, 1000);
        toastLog("悬浮窗权限已开启！");
        context_Manualstate = 0;
        Set_Back_way();
        DS();
        device.keepScreenDim();
    } else if (i == 4) {
        toastLog(options_[i]);
        try {
            if (files.exists("/storage/emulated/0/OrangeJs/种豆得豆自动脚本/返回方法设置.txt") == true && files.read("/storage/emulated/0/OrangeJs/种豆得豆自动脚本/返回方法设置.txt") > 2 && files.exists("/storage/emulated/0/OrangeJs/种豆得豆自动脚本/滑动返回速度.txt") == false) {
                files.remove("/storage/emulated/0/OrangeJs/种豆得豆自动脚本/返回方法设置.txt");
                log("当前返回方法设置为滑动返回但未设置滑动返回速度");
            }
            if (files.exists("/storage/emulated/0/OrangeJs/种豆得豆自动脚本/返回方法设置.txt") == true) {
                files.rename("/storage/emulated/0/OrangeJs/种豆得豆自动脚本/返回方法设置.txt", "X返回方法设置.txt");
                Set_Back_way();
            } else {
                dialogs.alert("您未保存任何返回方法，请运行脚本后再进行修改");
                dialogs_js();
            }
        } catch (e) {
            dialogs.alert("未授予本软件“存储权限”", "软件内的设置存储都需要“存储权限”才能正常保存设置，您需要自行授予本软件“存储权限”才能正常使用设置保存功能");
            dialogs_js();
        }
    } else if (i == 5) {
        toastLog(options_[i]);
        context_Manualstate = 1;
        Set_Back_way() //设置手动模式
    } else if (i == 6) {
        toastLog(options_[i]);
        context_Manualstate = 0;
        if (files.exists("/storage/emulated/0/OrangeJs/种豆得豆自动脚本/吐司or日志.txt") == true) {
            var z = files.read("/storage/emulated/0/OrangeJs/种豆得豆自动脚本/吐司or日志.txt");
            if (z != "吐司" && z != "日志") {
                alert("“吐司or日志”文件错误，已尝试删除错误文件");
                try {
                    files.remove("/storage/emulated/0/OrangeJs/种豆得豆自动脚本/吐司or日志.txt");
                } catch (e) {
                    toastLog("删除“吐司or日志”文件失败！");
                }
                var Z = "";
            } else {
                var Z = "当前脚本使用：" + z + "\n";
            }
        } else {
            var Z = "";
        }
        let da = dialogs.select(Z + "请选择一个选项", "使用吐司（Toast）", "使用脚本悬浮日志")
        if (da == 0) {
            toastLog("您选择了：使用吐司");
            try {
                var T = 0;
                files.createWithDirs("/storage/emulated/0/OrangeJs/种豆得豆自动脚本/吐司or日志.txt");
                files.write("/storage/emulated/0/OrangeJs/种豆得豆自动脚本/吐司or日志.txt", "吐司");
            } catch (e) {
                log("未授予存储权限或存储权限错误，当前设置为吐司");
                var T = 0;
            }
        } else if (da == 1) {
            toastLog("您选择了：使用悬浮日志");
            try {
                var T = 1;
                files.createWithDirs("/storage/emulated/0/OrangeJs/种豆得豆自动脚本/吐司or日志.txt");
                files.write("/storage/emulated/0/OrangeJs/种豆得豆自动脚本/吐司or日志.txt", "日志");
            } catch (e) {
                log("未授予存储权限或存储权限错误，开启悬浮日志");
                var T = 1;
            }
        }
        dialogs_js();
    }
}



function Set_Back_way() {
    try {
        if (files.exists("/storage/emulated/0/OrangeJs/种豆得豆自动脚本/返回方法设置.txt") == true) {
            context_i_back = files.read("/storage/emulated/0/OrangeJs/种豆得豆自动脚本/返回方法设置.txt");
            log("返回方法：" + context_i_back);
            if (context_i_back > 2) {
                try {
                    context_gestures_speed = files.read("/storage/emulated/0/OrangeJs/种豆得豆自动脚本/滑动返回速度.txt")
                    log("滑动返回速度：" + context_gestures_speed)
                } catch (e) {
                    log("上次未完成滑动返回速度设置");
                    files.remove("/storage/emulated/0/OrangeJs/种豆得豆自动脚本/返回方法设置.txt");
                    Set_Back_way();
                }
            }
        } else {
            //?????设定返回方法及滑动速度的代码
            var options_hq = ["?? 普通的返回\n(使用无障碍权限)", "#? 使用ROOT返回\n(必须授予本软件ROOT权限)", "?? 通过调用搜索界面进入\n（“曲线救国法” 若其它返回均失效\n    来尝试此方法吧）", "?????????????????????? \n从屏幕中间从左向内滑动\n(全面屏手势返回 例如:小米MIUI)", "              ?????????????????????? \n从屏幕中间从右向内滑动\n(全面屏手势返回 例如:华为EMUI)", "?????????????????????? \n从屏幕左侧下方向上滑动\n(全面屏手势返回 例如:锤子Smartisan UI)", "               ????????????????? \n从屏幕右侧下方向上滑动\n(全面屏手势返回)"]
            var i_back = dialogs.select(" Hi! ( ?▽? )\n请选择一个方法\n用于实现返回操作", options_hq);
            if (i_back >= 0) {
                toastLog("您选择的是" + options_hq[i_back]);
                sleep(2000);
                var options_select = options_hq[i_back];
                context_i_back = i_back;
                files.createWithDirs("/storage/emulated/0/OrangeJs/种豆得豆自动脚本/返回方法设置.txt");
                files.write("/storage/emulated/0/OrangeJs/种豆得豆自动脚本/返回方法设置.txt", context_i_back);
            } else {
                toastLog("没有选择返回方法！");
                device.cancelKeepingAwake();
            }
            if (i_back > 2) {
                var options_hd = ["200毫秒\n(默认，如果太快请选其它)", "500毫秒", "800毫秒", "1秒(1000毫秒)", "1.5秒（1500毫秒）", "2秒（2000毫秒）"]
                var iix = dialogs.select("Ok! (???) 您选择了:\n" + options_select + "\n请选择滑动速度\n单位:毫秒（1秒=1000毫秒）", options_hd);
                if (iix < 0) {
                    toastLog("没有选择滑动速度");
                    Set_Back_way();
                } else {
                    if (iix == 0) {
                        context_gestures_speed = 200;
                        toastLog("滑动速度设定为\n" + context_gestures_speed + "毫秒");
                        sleep(2000);
                    }
                    if (iix == 1) {
                        context_gestures_speed = 500;
                        toastLog("滑动速度设定为\n" + context_gestures_speed + "毫秒");
                        sleep(2000);
                    }
                    if (iix == 2) {
                        context_gestures_speed = 800;
                        toastLog("滑动速度设定为\n" + context_gestures_speed + "毫秒");
                        sleep(2000);
                    }
                    if (iix == 3) {
                        context_gestures_speed = 1000;
                        toastLog("滑动速度设定为\n" + context_gestures_speed + "毫秒");
                        sleep(2000);
                    }
                    if (iix == 4) {
                        context_gestures_speed = 1500;
                        toastLog("滑动速度设定为\n" + context_gestures_speed + "毫秒");
                        sleep(2000);
                    }
                    if (iix == 5) {
                        context_gestures_speed = 2000;
                        toastLog("滑动速度设定为\n" + context_gestures_speed + "毫秒");
                        sleep(2000);
                    }
                    files.createWithDirs("/storage/emulated/0/OrangeJs/种豆得豆自动脚本/滑动返回速度.txt");
                    files.write("/storage/emulated/0/OrangeJs/种豆得豆自动脚本/滑动返回速度.txt", context_gestures_speed);
                }
            }
            if (files.exists("/storage/emulated/0/OrangeJs/种豆得豆自动脚本/返回方法设置.txt") == true && files.exists("/storage/emulated/0/OrangeJs/种豆得豆自动脚本/X返回方法设置.txt") == true) {
                log("删除");
                files.remove("/storage/emulated/0/OrangeJs/种豆得豆自动脚本/X返回方法设置.txt");
                dialogs_js();
            } else if (files.exists("/storage/emulated/0/OrangeJs/种豆得豆自动脚本/X返回方法设置.txt") == true) {
                log("重命名");
                files.rename("/storage/emulated/0/OrangeJs/种豆得豆自动脚本/X返回方法设置.txt", "返回方法设置.txt");
                dialogs_js();
            }
        }
    } catch (e) {
        log("未授予“存储权限”");
        var options_hq = ["?? 普通的返回\n(使用无障碍权限)", "#? 使用ROOT返回\n(必须授予本软件ROOT权限)", "?? 通过调用搜索界面进入\n（“曲线救国法” 若其它返回均失效\n    来尝试此方法吧）", "?????????????????????? \n从屏幕中间从左向内滑动\n(全面屏手势返回 例如:小米MIUI)", "              ?????????????????????? \n从屏幕中间从右向内滑动\n(全面屏手势返回 例如:华为EMUI)", "?????????????????????? \n从屏幕左侧下方向上滑动\n(全面屏手势返回 例如:锤子Smartisan UI)", "               ????????????????? \n从屏幕右侧下方向上滑动\n(全面屏手势返回)"]
        var i_back = dialogs.select(" Hi! ( ?▽? )\n请选择一个方法\n用于实现返回操作", options_hq);
        if (i_back >= 0) {
            toastLog("您选择的是" + options_hq[i_back]);
            sleep(2000);
            var options_select = options_hq[i_back];
            context_i_back = i_back;
        } else {
            toastLog("没有选择返回方法！");
            device.cancelKeepingAwake();
        }
        if (i_back > 2) {
            var options_hd = ["200毫秒\n(默认，如果太快请选其它)", "500毫秒", "800毫秒", "1秒(1000毫秒)", "1.5秒（1500毫秒）", "2秒（2000毫秒）"]
            var iix = dialogs.select("Ok! (???) 您选择了:\n" + options_select + "\n请选择滑动速度\n单位:毫秒（1秒=1000毫秒）", options_hd);
            if (iix < 0) {
                toastLog("没有选择滑动速度");
                Set_Back_way();
            } else {
                if (iix == 0) {
                    context_gestures_speed = 200;
                    toastLog("滑动速度设定为\n" + context_gestures_speed + "毫秒");
                    sleep(2000);
                }
                if (iix == 1) {
                    context_gestures_speed = 500;
                    toastLog("滑动速度设定为\n" + context_gestures_speed + "毫秒");
                    sleep(2000);
                }
                if (iix == 2) {
                    context_gestures_speed = 800;
                    toastLog("滑动速度设定为\n" + context_gestures_speed + "毫秒");
                    sleep(2000);
                }
                if (iix == 3) {
                    context_gestures_speed = 1000;
                    toastLog("滑动速度设定为\n" + context_gestures_speed + "毫秒");
                    sleep(2000);
                }
                if (iix == 4) {
                    context_gestures_speed = 1500;
                    toastLog("滑动速度设定为\n" + context_gestures_speed + "毫秒");
                    sleep(2000);
                }
                if (iix == 5) {
                    context_gestures_speed = 2000;
                    toastLog("滑动速度设定为\n" + context_gestures_speed + "毫秒");
                    sleep(2000);
                }
            }
        }
    }
}

sleep(1000);
toastLog("等待无障碍权限开启……\n您必须手动授予本软件无障碍权限\n否则本软件将无法工作！");
auto.waitFor();
toastLog("无障碍权限已开启" + "\n" + "继续运行脚本……");
if (files.exists("/storage/emulated/0/OrangeJs/种豆得豆自动脚本/吐司or日志.txt") == true) {
    try {
        let z = files.read("/storage/emulated/0/OrangeJs/种豆得豆自动脚本/吐司or日志.txt");
        if (z == "吐司") {
            var T = 0;
        } else if (z == "日志") {
            var T = 1;
        } else {
            toastLog("“吐司or日志”文件错误，已尝试删除并使用默认日志");
            try {
                files.remove("/storage/emulated/0/OrangeJs/种豆得豆自动脚本/吐司or日志.txt");
            } catch (e) {
                toastLog("删除“吐司or日志”文件失败！");
            }
            var T = 1;
        }
    } catch (e) {
        if (T == null) {
            log("未授予存储权限或存储权限错误，默认开启悬浮日志");
            var T = 1;
        }
    }
} else {
    try {
        files.createWithDirs("/storage/emulated/0/OrangeJs/种豆得豆自动脚本/吐司or日志.txt");
        files.write("/storage/emulated/0/OrangeJs/种豆得豆自动脚本/吐司or日志.txt", "日志");
        var T = 1;
        log("默认使用日志，如需更改请在主菜单进行");
    } catch (e) {
        log("未授予存储权限或存储权限错误，默认开启悬浮日志");
        var T = 1;
    }
}

function wait_Time_over() {
    var i_wait = dialogs.singleChoice("?? 定时运行\n\n(＾?＾)??\n请选择一个选项\n计时结束会自动运行", ["1分钟后运行", "5分钟后运行", "10分钟后运行", "30分钟后运行", "一小时后运行", "两小时后运行", "三小时后运行", "五小时后运行", "八小时后运行"], 2);
    if (i_wait < 0) {
        toast("您取消了选择");
        device.cancelKeepingAwake();
        dialogs_js();
    }
    if (i_wait >= 0) {
        context_i_wait = i_wait;
    }
    if (i_wait == 0) {
        var choice_confirm = dialogs.confirm("您选择了1分钟后运行", "点击确定进行一次设定返回操作的方法后，脚本将在您设定的时间结束后开始自动运行\n请不要清理本软件的后台或者锁屏手机等，否则可能会造成定时任务失效");
        if (choice_confirm == false) {
            toastLog("取消了定时运行确认");
            wait_Time_over();
        } else {
            Set_Back_way();
            waiting_time();
        }
    }
    if (i_wait == 1) {
        var choice_confirm = dialogs.confirm("您选择了5分钟后运行", "点击确定进行一次设定返回操作的方法后，脚本将在您设定的时间结束后开始自动运行\n请不要清理本软件的后台或者锁屏手机等，否则可能会造成定时任务失效");
        if (choice_confirm == false) {
            toastLog("取消了定时运行确认");
            wait_Time_over();
        } else {
            Set_Back_way();
            waiting_time();
        }
    }
    if (i_wait == 2) {
        var choice_confirm = dialogs.confirm("您选择了10分钟后运行", "点击确定进行一次设定返回操作的方法后，脚本将在您设定的时间结束后开始自动运行\n请不要清理本软件的后台或者锁屏手机等，否则可能会造成定时任务失效");
        if (choice_confirm == false) {
            toastLog("取消了定时运行确认");
            wait_Time_over();
        } else {
            Set_Back_way();
            waiting_time();
        }
    }
    if (i_wait == 3) {
        var choice_confirm = dialogs.confirm("您选择了30分钟后运行", "点击确定进行一次设定返回操作的方法后，脚本将在您设定的时间结束后开始自动运行\n请不要清理本软件的后台或者锁屏手机等，否则可能会造成定时任务失效");
        if (choice_confirm == false) {
            toastLog("取消了定时运行确认");
            wait_Time_over();
        } else {
            Set_Back_way();
            waiting_time();
        }
    }
    if (i_wait == 4) {
        var choice_confirm = dialogs.confirm("您选择了一小时后运行", "点击确定进行一次设定返回操作的方法后，脚本将在您设定的时间结束后开始自动运行\n请不要清理本软件的后台或者锁屏手机等，否则可能会造成定时任务失效");
        if (choice_confirm == false) {
            toastLog("取消了定时运行确认");
            wait_Time_over();
        } else {
            Set_Back_way();
            waiting_time();
        }
    }
    if (i_wait == 5) {
        var choice_confirm = dialogs.confirm("您选择了两小时后运行", "点击确定进行一次设定返回操作的方法后，脚本将在您设定的时间结束后开始自动运行\n请不要清理本软件的后台或者锁屏手机等，否则可能会造成定时任务失效");
        if (choice_confirm == false) {
            toastLog("取消了定时运行确认");
            wait_Time_over();
        } else {
            Set_Back_way();
            waiting_time();
        }
    }
    if (i_wait == 6) {
        var choice_confirm = dialogs.confirm("您选择了三小时后运行", "点击确定进行一次设定返回操作的方法后，脚本将在您设定的时间结束后开始自动运行\n请不要清理本软件的后台或者锁屏手机等，否则可能会造成定时任务失效");
        if (choice_confirm == false) {
            toastLog("取消了定时运行确认");
            wait_Time_over();
        } else {
            Set_Back_way();
            waiting_time();
        }
    }
    if (i_wait == 7) {
        var choice_confirm = dialogs.confirm("您选择了五小时后运行", "点击确定进行一次设定返回操作的方法后，脚本将在您设定的时间结束后开始自动运行\n请不要清理本软件的后台或者锁屏手机等，否则可能会造成定时任务失效");
        if (choice_confirm == false) {
            toastLog("取消了定时运行确认");
            wait_Time_over
        } else {
            Set_Back_way();
            waiting_time();
        }
    }
    if (i_wait == 8) {
        var choice_confirm = dialogs.confirm("您选择了八小时后运行", "点击确定进行一次设定返回操作的方法后，脚本将在您设定的时间结束后开始自动运行\n请不要清理本软件的后台或者锁屏手机等，否则可能会造成定时任务失效");
        if (choice_confirm == false) {
            toastLog("取消了定时运行确认");
            wait_Time_over();
        } else {
            Set_Back_way();
            waiting_time();
        }
    }
}

function waiting_time() {
    //计时运行脚本
    if (context_i_wait == 0) {
        var Seconds = 60;
        for (Seconds == 60; Seconds > 0; Seconds--) {
            console.warn("【定时运行】计时中……\n" + Seconds + "秒后开始运行");
            sleep(1000);
        }
    }
    if (context_i_wait == 1) {
        var Minutes = 4;
        for (Minutes == 4; Minutes >= 0; Minutes--) {
            if (Minutes >= 0) {
                var Seconds = 60;
                for (Seconds == 60; Seconds > 0; Seconds--) {
                    console.warn("【定时运行】计时中……\n" + Minutes + "分钟" + Seconds + "秒后开始运行");
                    sleep(1000);
                }
            }
        }
    }
    if (context_i_wait == 2) {
        var Minutes = 9;
        for (Minutes == 9; Minutes >= 0; Minutes--) {
            if (Minutes >= 0) {
                var Seconds = 60;
                for (Seconds == 60; Seconds > 0; Seconds--) {
                    console.warn("【定时运行】计时中……\n" + Minutes + "分钟" + Seconds + "秒后开始运行");
                    sleep(1000);
                }
            }
        }
    }
    if (context_i_wait == 3) {
        var Minutes = 29;
        for (Minutes == 29; Minutes >= 0; Minutes--) {
            if (Minutes >= 0) {
                var Seconds = 60;
                for (Seconds == 60; Seconds > 0; Seconds--) {
                    console.warn("【定时运行】计时中……\n" + Minutes + "分钟" + Seconds + "秒后开始运行");
                    sleep(1000);
                }
            }
        }
    }
    if (context_i_wait == 4) {
        var Minutes = 59;
        for (Minutes == 59; Minutes >= 0; Minutes--) {
            if (Minutes >= 0) {
                var Seconds = 60;
                for (Seconds == 60; Seconds > 0; Seconds--) {
                    console.warn("【定时运行】计时中……\n" + Minutes + "分钟" + Seconds + "秒后开始运行");
                    sleep(1000);
                }
            }
        }
    }
    if (context_i_wait == 5) {
        var Hours = 1;
        for (Hours == 1; Hours >= 0; Hours--) {
            var Minutes = 59;
            for (Minutes == 59; Minutes >= 0; Minutes--) {
                if (Minutes >= 0) {
                    var Seconds = 60;
                    for (Seconds == 60; Seconds > 0; Seconds--) {
                        console.warn("【定时运行】计时中……\n" + Hours + "小时" + Minutes + "分钟" + Seconds + "秒后开始运行");
                        sleep(1000);
                    }
                }
            }
        }
    }
    if (context_i_wait == 6) {
        var Hours = 2;
        for (Hours == 2; Hours >= 0; Hours--) {
            var Minutes = 59;
            for (Minutes == 59; Minutes >= 0; Minutes--) {
                if (Minutes >= 0) {
                    var Seconds = 60;
                    for (Seconds == 60; Seconds > 0; Seconds--) {
                        console.warn("【定时运行】计时中……\n" + Hours + "小时" + Minutes + "分钟" + Seconds + "秒后开始运行");
                        sleep(1000);
                    }
                }
            }
        }
    }
    if (context_i_wait == 7) {
        var Hours = 4;
        for (Hours == 4; Hours >= 0; Hours--) {
            var Minutes = 59;
            for (Minutes == 59; Minutes >= 0; Minutes--) {
                if (Minutes >= 0) {
                    var Seconds = 60;
                    for (Seconds == 60; Seconds > 0; Seconds--) {
                        console.warn("【定时运行】计时中……\n" + Hours + "小时" + Minutes + "分钟" + Seconds + "秒后开始运行");
                        sleep(1000);
                    }
                }
            }
        }
    }
    if (context_i_wait == 8) {
        var Hours = 7;
        for (Hours == 7; Hours >= 0; Hours--) {
            var Minutes = 59;
            for (Minutes == 59; Minutes >= 0; Minutes--) {
                if (Minutes >= 0) {
                    var Seconds = 60;
                    for (Seconds == 60; Seconds > 0; Seconds--) {
                        console.warn("【定时运行】计时中……\n" + Hours + "小时" + Minutes + "分钟" + Seconds + "秒后开始运行");
                        sleep(1000);
                    }
                }
            }
        }
    }
}

function DS() {
    var While = 1;
    while (While == 1) {
        var 时 = dialogs.rawInput("??定时→定分→定秒→确认\n\n请输入0-23的小时数\n到此时间脚本会自动运行");
        if (时 == null) {
            //没有输入
            toastLog("没有输入！返回主菜单");
            var While = 0;
            dialogs_js();
        } else if (时 == "") {
            //没有输入
            toastLog("没有输入！返回主菜单");
            var While = 0;
            dialogs_js();
        } else if (时 >= 0) {
            if (时 < 24) {
                var While = 2;
                while (While == 2) {
                    var 分 = dialogs.rawInput("??定时??定分→定秒→确认\n\n请输入0-59的分钟数\n\n" + 时 + "时" + "?分?秒");
                    if (分 == null) {
                        toastLog("没有输入！返回上级");
                        var While = 1;
                    } else if (分 == null) {
                        toastLog("没有输入！返回上级");
                        var While = 1;
                    } else if (分 >= 0) {
                        if (分 < 60) {
                            var While = 3;
                            while (While == 3) {
                                var 秒 = dialogs.rawInput("??定时??定分??定秒→确认\n\n请输入0-59的秒数\n\n" + 时 + "时" + 分 + "分?秒");
                                if (秒 == null) {
                                    toastLog("没有输入！返回上级");
                                    var While = 2;
                                } else if (秒 == null) {
                                    toastLog("没有输入！返回上级");
                                    var While = 2;
                                } else if (秒 >= 0) {
                                    if (秒 < 60) {
                                        var QR = dialogs.confirm("脚本将在\n?" + 时 + "时" + 分 + "分" + 秒 + "秒\n准时运行！", "如需更改请点击取消\n点击确定定时，定时状态可以在日志中查看");
                                        if (QR == false) {
                                            //返回主菜单
                                            var While = 1;
                                        } else {
                                            var While = 0;
                                            //仅定时运行一次
                                            while (true) {
                                                var myDate = new Date();
                                                if (myDate.getHours() == 时 && myDate.getMinutes() == 分 && myDate.getSeconds() == 秒) {
                                                    console.warn("时间到！开始运行脚本！" + myDate.getHours() + "时" + myDate.getMinutes() + "分" + myDate.getSeconds() + "秒");
                                                    device.wakeUpIfNeeded();
                                                    break;
                                                }
                                                sleep(1000);
                                                console.info("现在是" + myDate.getHours() + "时" + myDate.getMinutes() + "分" + myDate.getSeconds() + "秒\n脚本将在" + 时 + "时" + 分 + "分" + 秒 + "秒，准时运行！\n请保持手机处于工作状态，不要锁屏关机等");
                                            }
                                        }
                                    } else {
                                        toastLog("输入错误！秒必须小于等于60");
                                    }
                                } else {
                                    toastLog("输入错误！秒必须大于等于0");
                                }
                            }
                        } else {
                            toastLog("输入错误！分钟必须小于60");
                        }
                    } else {
                        toastLog("输入错误！分钟必须大于等于0");
                    }
                }
            } else {
                toastLog("输入错误！时间必须小于24");
            }
        } else {
            toastLog("输入错误！时间必须大于等于0");
        }
    }
}

//下面是悬浮窗
var window = floaty.window(
    <frame>
        <button id="action" text="点击停止脚本" w="120" h="40" bg="#F0EB4336"/>
    </frame>
);
setInterval(() => {}, 1000);
var execution = null;
//记录按键被按下时的触摸坐标
var x = 0,
    y = 0;
//记录按键被按下时的悬浮窗位置
var windowX, windowY;
//记录按键被按下的时间以便判断长按等动作
var downTime;
window.action.setOnTouchListener(function(view, event) {
    switch (event.getAction()) {
        case event.ACTION_DOWN:
            x = event.getRawX();
            y = event.getRawY();
            windowX = window.getX();
            windowY = window.getY();
            downTime = new Date().getTime();
            return true;
        case event.ACTION_MOVE:
            //移动手指时调整悬浮窗位置
            window.setPosition(windowX + (event.getRawX() - x),
                windowY + (event.getRawY() - y));
            //如果按下的时间超过1.5秒判断为长按，退出脚本
            if (new Date().getTime() - downTime > 1500) {
                toast("长按可以移动位置哦～");
            }
            return true;
        case event.ACTION_UP:
            //手指弹起时如果偏移很小则判断为点击
            if (Math.abs(event.getRawY() - y) < 5 && Math.abs(event.getRawX() - x) < 5) {
                onClick();
            }
            return true;
    }
    return true;
});

function onClick() {
    dialogs.alert("已停止运行脚本！");
    log("用户点击了停止按钮");
    exit();
}

function Justback() {
    //??????????使用用户设定的返回方法
    if (context_i_back == 0) {
        sleep(1000);
        toastLog("使用普通的返回");
        back();
        sleep(2000);
    }
    if (context_i_back == 1) {
        sleep(1000);
        toastLog("使用ROOT返回\n请确保已给ROOT权限！");
        Back();
        sleep(2000);
    }
    if (context_i_back == 2) {
        openInTask();
    }
    if (context_i_back == 3) {
        sleep(1000);
        toastLog("从屏幕中间向从左向内滑动来返回");
        gestures([context_gestures_speed, [0, height / 2],
            [500, height / 2]
        ]);
        sleep(2000);
    }
    if (context_i_back == 5) {
        sleep(1000);
        toastLog("从屏幕左侧下方向上滑动来返回");
        gestures([context_gestures_speed, [width / 2 - 300, height - 1],
            [width / 2 - 300, height - 500]
        ]);
        sleep(2000);
    }
    if (context_i_back == 4) {
        sleep(1000);
        toastLog("从屏幕中间向从右向内滑动来返回");
        gestures([context_gestures_speed, [width - 1, height / 2],
            [width - 500, height / 2]
        ]);
        sleep(2000);
    }
    if (context_i_back == 6) {
        sleep(1000);
        toastLog("从屏幕左侧下面向上面滑动来返回");
        gestures([context_gestures_speed, [width / 2 + 300, height - 1],
            [width / 2 + 300, height - 500]
        ]);
        sleep(2000);
    }
}

if (T == 1) {
    log("使用“悬浮日志”");

    function toastLog(message) {
        log(message);
        var myDate = new Date();
        ui.run(() => {
            w.WZ.setText(myDate.getHours() + "时" + myDate.getMinutes() + "分" + myDate.getSeconds() + "秒：" + message + "\n" + w.WZ.getText());
            return true;
        });
    }
    var w = floaty.rawWindow(
        <card bg="#80000000">
            <vertical align="center">
                <img src="{{getStorageData('APPbasic', 'URLprefix')}}/OrangeJs-logoWhite.png" h="30" margin="0 10 0 5"/>//黑色logo
                <text text="─ 当前脚本运行日志 ─" textSize="15" color="#FFFFFF" textStyle="bold" gravity="center" margin="0 0 0 5"/>
                <text id="WZ" text="" textSize="15" color="#FFFFFF" marginLeft="10" gravity="left"/>
            </vertical>
        </card>
    );
    w.setSize(device.width, 500);
    w.setTouchable(false);
    w.setPosition(0, device.height - 500);
} else if (T == 0) {
    log("使用脚本自带“吐司”");
}


function openInTask() {
    while (true) {
        if (className("android.view.View").desc("我的").findOnce() != null && text("种豆得豆").className("android.widget.TextView").findOnce() != null && text("瓜分亿万京豆").className("android.widget.TextView").findOnce() != null) {
            if (text("种豆得豆").className("android.widget.TextView").findOnce().parent().clickable() == true) {
                text("种豆得豆").className("android.widget.TextView").findOnce().parent().click();
                toastLog("已尝试盲点“种豆得豆”入口按钮");
                sleep(3000);
            } else {
                let a = text("种豆得豆").className("android.widget.TextView").findOnce().parent().bounds();
                click(a.centerX(), a.centerY());
                toastLog("已尝试点击“种豆得豆”入口按钮");
                sleep(3000);
            }
            break;
        } else if (className("android.view.View").desc("我的").findOnce() != null) {
            className("android.view.View").desc("我的").findOnce().click();
            toastLog("已尝试点击京东主页“我的”按钮");
            sleep(2000);
        } else if (currentPackage() != "com.jingdong.app.mall") {
            app.startActivity({
                action: "android.intent.action.VIEW", //此处可为其他值
                packageName: "com.jingdong.app.mall",
                className: "com.jingdong.app.mall.main.MainActivity"
                //此处可以加入其他内容，如data、extras
            });
            toastLog("当前未处于京东APP中，正在重新打开京东……");
            console.warn("当前活动：" + currentActivity() + "，当前包名：" + currentPackage() + "当前应用名：" + getAppName(currentPackage()));
            sleep(2000);
        } else {
            if (className("android.widget.ImageView").desc("返回").clickable(true).findOnce() != null) {
                className("android.widget.ImageView").desc("返回").clickable(true).findOnce().click();
                toastLog("已尝试点击“返回”按钮");
            } else {
                Justback();
            }
            sleep(2000);
        }
    }
    for (var d = 10; d > 0; d--) {
        if (MakeSureInHD() == true) {
            break
        } else {
            toastLog("正在等待“种豆得豆”活动界面加载，剩余" + d + "秒……");
            sleep(2000);
        }
    }
    if (MakeSureInHD() == false) {
        openInTask();
    }
}

function MakeSureInHD() {
    if (className("android.widget.TextView").text("收取营养液").findOnce() != null) {
        return true;
    } else {
        return false;
    }
}

function DoTask() {
    if (id("com.jingdong.app.mall:id/aba").findOnce() != null &&
        id("com.jingdong.app.mall:id/aba").findOnce().childCount() > 0 &&
        id("com.jingdong.app.mall:id/aba").findOnce().child(0).childCount() > 0 &&
        id("com.jingdong.app.mall:id/aba").findOnce().child(0).child(0).childCount() > 0 &&
        id("com.jingdong.app.mall:id/aba").findOnce().child(0).child(0).child(0).childCount() > 0 &&
        id("com.jingdong.app.mall:id/aba").findOnce().child(0).child(0).child(0).child(0).childCount() > 0 &&
        id("com.jingdong.app.mall:id/aba").findOnce().child(0).child(0).child(0).child(0).child(0).childCount() > 0 &&
        id("com.jingdong.app.mall:id/aba").findOnce().child(0).child(0).child(0).child(0).child(0).child(0).childCount() > 0 &&
        id("com.jingdong.app.mall:id/aba").findOnce().child(0).child(0).child(0).child(0).child(0).child(0).child(0).childCount() > 0 &&
        id("com.jingdong.app.mall:id/aba").findOnce().child(0).child(0).child(0).child(0).child(0).child(0).child(0).child(0).childCount() == 2 &&
        id("com.jingdong.app.mall:id/aba").findOnce().child(0).child(0).child(0).child(0).child(0).child(0).child(0).child(0).child(0).className() == "android.view.ViewGroup" &&
        id("com.jingdong.app.mall:id/aba").findOnce().child(0).child(0).child(0).child(0).child(0).child(0).child(0).child(0).child(1).className() == "android.widget.ImageView"
    ) {
        let a = id("com.jingdong.app.mall:id/aba").findOnce().child(0).child(0).child(0).child(0).child(0).child(0).child(0).child(0).child(1);
        if (a.clickable() == true) {
            a.click();
            toastLog("已尝试盲点“收豆蒙版”按钮");
        } else {
            let b = a.bounds();
            click(b.centerX(), b.centerY());
            toastLog("已尝试点击“收豆蒙版”按钮");
        }
        sleep(3000);
        if (className("android.widget.TextView").text("上轮您的豆豆成长值为").findOnce() != null && className("android.widget.TextView").text("上轮您的豆豆成长值为").findOnce().parent().childCount() == 4 &&
            className("android.widget.TextView").text("上轮您的豆豆成长值为").findOnce().parent().child(0).className() == "android.widget.TextView" && className("android.widget.TextView").text("上轮您的豆豆成长值为").findOnce().parent().child(1).className() == "android.widget.TextView" && className("android.widget.TextView").text("上轮您的豆豆成长值为").findOnce().parent().child(2).className() == "android.widget.TextView" && className("android.widget.TextView").text("上轮您的豆豆成长值为").findOnce().parent().child(3).className() == "android.widget.TextView") {
            toastLog(className("android.widget.TextView").text("上轮您的豆豆成长值为").findOnce().parent().child(0).text() + className("android.widget.TextView").text("上轮您的豆豆成长值为").findOnce().parent().child(1).text() + className("android.widget.TextView").text("上轮您的豆豆成长值为").findOnce().parent().child(2).text() + className("android.widget.TextView").text("上轮您的豆豆成长值为").findOnce().parent().child(3).text())
        }
        if (className("android.widget.TextView").text("收下京豆").findOnce() != null) {
            let b = className("android.widget.TextView").text("收下京豆").findOnce().bounds();
            click(b.centerX(), b.centerY());
            sleep(3000);
        }
    }

    let ShouQu = ["好友帮收", "逛逛会场", "点击领取", "营养液", "每日签到", "618活动", "浏览店铺", "挑选商品", "金融双签", "疯抢爆品", "收取好友"];
    for (let a = 0; a < ShouQu.length; a++) {
        while (className("android.widget.TextView").text(ShouQu[a]).findOnce() != null && className("android.widget.TextView").text(ShouQu[a]).findOnce().parent().child(0).childCount() > 2 && className("android.widget.TextView").text(ShouQu[a]).findOnce().parent().child(0).child(2).className() == "android.widget.TextView") {
            let b = className("android.widget.TextView").text(ShouQu[a]).findOnce().parent().child(0).child(2);
            click(b.bounds().centerX(), b.bounds().centerY());
            toastLog("已尝试点击“" + ShouQu[a] + b.text() + "”");
            sleep(2000);
        }
    }

    if (className("android.widget.ScrollView").findOnce() != null && className("android.widget.ScrollView").findOnce().childCount() > 0 && className("android.widget.ScrollView").findOnce().child(0).childCount() > 2) {
        let a = className("android.widget.ScrollView").findOnce().child(0).child(className("android.widget.ScrollView").findOnce().child(0).childCount() - 2).bounds();
        click(a.centerX(), a.centerY());
        toastLog("已尝试点击“全部任务”按钮");
        sleep(2000);
    } else if (className("android.widget.TextView").text("收取营养液").findOnce() != null && className("android.widget.TextView").text("收取营养液").findOnce().parent().className() == "android.view.ViewGroup" && className("android.widget.TextView").text("收取营养液").findOnce().parent().parent().childCount() > 14) {
        let a = className("android.widget.TextView").text("收取营养液").findOnce().parent().parent().child(13).bounds();
        click(a.centerX(), a.centerY());
        toastLog("已尝试点击“全部任务”按钮");
        sleep(2000);
    }


    var ax = 0;
    var DoNotDoPJRW = null;
    var DoNotDoGGHC = null;
    while (true) {
        if (className("android.widget.TextView").text("全部任务").findOnce() != null && className("android.widget.TextView").text("全部任务").findOnce().parent().child(className("android.widget.TextView").text("全部任务").findOnce().parent().childCount() - 1).className() == "android.widget.ScrollView") {
            var A = className("android.widget.TextView").text("全部任务").findOnce().parent().child(className("android.widget.TextView").text("全部任务").findOnce().parent().childCount() - 1);
            var B = A.child(0);
        }
        toastLog("任务列表可滑动区域为：" + B.bounds().top + "," + B.bounds().bottom);
        if (ax >= B.childCount()) {
            break;
        } else {
            try {
                if (B.child(ax).child(0).childCount() > 1 && B.child(ax).child(0).child(1).className() == "android.widget.TextView") {
                    var RwTitle = B.child(ax).child(0).child(1).text();
                } else if (B.child(ax).child(0).childCount() > 0 && B.child(ax).child(0).child(0).childCount() > 1 && B.child(ax).child(0).child(0).child(1).className() == "android.widget.TextView") {
                    var RwTitle = B.child(ax).child(0).child(0).child(1).text();
                }
                if (B.child(ax).childCount() > 0 &&
                    B.child(ax).child(0).childCount() > 2 &&
                    B.child(ax).child(0).child(2).childCount() > 1 &&
                    B.child(ax).child(0).child(2).child(1).className() == "android.widget.TextView") {
                    var ZhuangTai = B.child(ax).child(0).child(2).child(1).text();
                } else if (B.child(ax).childCount() > 0 &&
                    B.child(ax).child(0).childCount() > 2 &&
                    B.child(ax).child(0).child(2).childCount() > 0 &&
                    B.child(ax).child(0).child(2).child(0).className() == "android.widget.TextView") {
                    var ZhuangTai = B.child(ax).child(0).child(2).child(0).text();
                }
                log(ZhuangTai);
                if (B.child(ax).childCount() > 0 &&
                    B.child(ax).child(0).childCount() > 5 &&
                    B.child(ax).child(0).child(5).className() == "android.view.ViewGroup") {
                    var Button = B.child(ax).child(0).child(5).child(0);
                } else if (B.child(ax).childCount() > 0 &&
                    B.child(ax).child(0).childCount() > 4 &&
                    B.child(ax).child(0).child(4).className() == "android.widget.TextView") {
                    var Button = B.child(ax).child(0).child(4);
                } else if (B.child(ax).childCount() > 0 &&
                    B.child(ax).child(0).childCount() > 4 &&
                    B.child(ax).child(0).child(4).className() == "android.view.ViewGroup") {
                    var Button = B.child(ax).child(0).child(4).child(0);
                }
                log(RwTitle, ZhuangTai, Button.text());
            } catch (e) {
                console.warn("当前活动：" + currentActivity() + "，当前包名：" + currentPackage() + "当前应用名：" + getAppName(currentPackage()));
                toastLog("当前未处于“任务列表”界面或返回任务界面出错，正在重新进入:" + e);
                openInTask();
                DoTask();
            }
            if (ZhuangTai.search("/") > 0) {
                let Start = ZhuangTai.search("/");
                now = null;
                xz = null;
                i = Start - 1;
                while (true) {
                    if (now != null && isNaN(ZhuangTai[i]) == true) {
                        break;
                    } else if (now == null) {
                        var now = ZhuangTai[i];
                    } else {
                        var now = ZhuangTai[i] + now;
                    }
                    i--;
                }
                i = Start + 1;
                while (true) {
                    if (xz != null && isNaN(ZhuangTai[i]) == true) {
                        break;
                    } else if (xz == null) {
                        var xz = ZhuangTai[i];
                    } else {
                        var xz = xz + ZhuangTai[i];
                    }
                    i++;
                }
            } else {
                log("无法确定任务上限及当前完成数，请联系开发者解决", "任务名状态名：" + ZhuangTai);
                alert("无法确定任务上限及当前完成数，请联系开发者解决", "任务名状态名：" + ZhuangTai);
                exit();
            }
            toastLog("当前任务完成已完成" + now + "次，当前任务上限为" + xz + "次");
            if (Button.bounds().centerY() > B.bounds().bottom - 10) {
                swipe(B.bounds().centerX(), B.bounds().centerY(), B.bounds().centerX(), B.bounds().centerY() - 500, 500);
                toastLog("已尝试上滑当前任务页，滑动前按钮“" + Button.text() + "”中心点Y坐标为：" + Button.bounds().centerY());
                sleep(1000);
            } else if (Button.bounds().centerY() < B.bounds().top) {
                swipe(B.bounds().centerX(), B.bounds().centerY(), B.bounds().centerX(), B.bounds().centerY() + 500, 500);
                toastLog("已尝试下滑当前任务页，滑动前按钮“" + Button.text() + "”中心点Y坐标为：" + Button.bounds().centerY());
                sleep(1000);
            } else if (now != xz && RwTitle != "逛逛会场" && RwTitle != "评价商品" && RwTitle != "好友助力" || now != xz && RwTitle == "逛逛会场" && DoNotDoGGHC == null && now == 0 || now != xz && RwTitle == "评价商品" && DoNotDoPJRW == null) {
                if (Button.clickable() == true) {
                    Button.click();
                    toastLog("已尝试盲点“" + Button.text() + "”按钮");
                } else {
                    let a = Button.bounds();
                    click(a.centerX(), a.centerY());
                    toastLog("已尝试点击“" + Button.text() + "”按钮");
                }
                sleep(3000);
                for (var JustWait = 10; JustWait > 0; JustWait--) {
                    if (className("android.widget.TextView").text("进店任务").findOnce() != null) { //浏览店铺
                        var limit = Number(xz);
                        var over = 0;
                        var ALL = className("android.widget.TextView").text("进店并关注").find().size();
                        try {
                            var X = className("android.widget.ScrollView").findOnce().bounds();
                            log(X);
                        } catch (e) {
                            console.warn("当前活动：" + currentActivity() + "，当前包名：" + currentPackage() + "当前应用名：" + getAppName(currentPackage()));
                            toastLog("未成功进入“进店并关注”菜单界面，正在重试中……");
                            openInTask();
                            DoTask();

                        }
                        toastLog("【“进店并关注”数量】：" + ALL + "【可点击区域】：" + X.top, X.bottom);
                        for (var i = 0; i <= ALL; i++) {
                            while (true) {
                                log(over, limit);
                                if (over >= limit) {
                                    toastLog("“进店并关注”获得营养液已达每日上限" + limit + "，返回继续进行下一任务");
                                    if (className("android.widget.ImageView").desc("返回").clickable(true).findOnce() != null) {
                                        className("android.widget.ImageView").desc("返回").clickable(true).findOnce().click();
                                    } else {
                                        Justback();
                                    }
                                    sleep(3000);
                                    var i = ALL;
                                    var JustWait = 0;
                                    break;
                                } else if (i >= ALL) {
                                    toastLog("已找完全部" + ALL + "个店铺，在浏览" + i + "个店铺后共找到" + over + "瓶营养液，但未达到今日" + limit + "个上限")
                                    if (className("android.widget.ImageView").desc("返回").clickable(true).findOnce() != null) {
                                        className("android.widget.ImageView").desc("返回").clickable(true).findOnce().click();
                                    } else {
                                        Justback();
                                    }
                                    sleep(3000);
                                    var JustWait = 0;
                                    break;
                                } else {
                                    let a = className("android.widget.TextView").text("进店并关注").findOnce(i);
                                    if (a == null) {
                                        toastLog("找不到“进店并关注”按钮，正在重新尝试中……");
                                        openInTask();
                                        DoTask();
                                        var JustWait = 0;
                                        break;
                                    } else if (a.bounds().top != X.top && a.bounds().bottom != X.bottom) {
                                        toastLog("【已点击】第" + i + "个“进店并关注”范围为：" + a.bounds().centerX(), a.bounds().centerY(), "上边缘点下边缘点分别为：" + a.bounds().top, a.bounds().bottom);
                                        click(a.bounds().centerX(), a.bounds().centerY());
                                        sleep(3000);
                                        if (currentActivity() == "com.jd.lib.jshop.jshop.JshopMainShopActivity" || className("android.widget.EditText").findOnce() != null) {
                                            for (var z = 5; z > 0; z--) {
                                                if (className("android.view.View").text("营养液走丢了～").findOnce() != null) {
                                                    var z = 0;
                                                    if (className("android.view.View").text("营养液走丢了～").findOnce().parent().parent().childCount() == 3) {
                                                        var za = className("android.view.View").text("营养液走丢了～").findOnce().parent().parent().child(2).child(1);
                                                    } else if (className("android.view.View").text("营养液走丢了～").findOnce().parent().parent().childCount() == 2) {
                                                        var za = className("android.view.View").text("营养液走丢了～").findOnce().parent().parent().child(1).child(1);
                                                    }
                                                    if (za.clickable() == true) {
                                                        za.click();
                                                        toastLog("营养液走丢了～已盲点“继续找营养液”");
                                                    } else {
                                                        let zb = za.bounds();
                                                        click(zb.centerX(), zb.centerY());
                                                        toastLog("营养液走丢了～已点击“继续找营养液（" + zb.centerX(), zb.centerY() + "）”");
                                                    }
                                                    sleep(3000);
                                                } else if (className("android.view.View").text("1个营养液").findOnce() != null || className("android.view.View").textContains("个营养液").findOnce() != null) {
                                                    var z = 0;
                                                    if (className("android.view.View").text("1个营养液").findOnce() != null && className("android.view.View").text("1个营养液").findOnce().parent().parent().childCount() == 3) {
                                                        var zat = className("android.view.View").text("1个营养液").findOnce();
                                                        var za = className("android.view.View").text("1个营养液").findOnce().parent().parent().child(2).child(1);
                                                    } else if (className("android.view.View").textContains("个营养液").findOnce() != null && className("android.view.View").textContains("个营养液").findOnce().parent().parent().childCount() == 3) {
                                                        var zat = className("android.view.View").textContains("个营养液").findOnce();
                                                        var za = className("android.view.View").textContains("个营养液").findOnce().parent().parent().child(2).child(1);
                                                    } else if (className("android.view.View").text("1个营养液").findOnce() != null && className("android.view.View").text("1个营养液").findOnce().parent().parent().childCount() == 2) {
                                                        var zat = className("android.view.View").text("1个营养液").findOnce();
                                                        var za = className("android.view.View").text("1个营养液").findOnce().parent().parent().child(1).child(1);
                                                    } else if (className("android.view.View").textContains("个营养液").findOnce() != null && className("android.view.View").textContains("个营养液").findOnce().parent().parent().childCount() == 2) {
                                                        var zat = className("android.view.View").textContains("个营养液").findOnce();
                                                        var za = className("android.view.View").textContains("个营养液").findOnce().parent().parent().child(1).child(1);
                                                    }
                                                    if (za.clickable() == true) {
                                                        za.click();
                                                        toastLog("已找到" + zat.text() + "～已盲点“继续找营养液”");
                                                    } else {
                                                        let zb = za.bounds();
                                                        click(zb.centerX(), zb.centerY());
                                                        toastLog("已找到" + zat.text() + "～已点击“继续找营养液（" + zb.centerX(), zb.centerY() + "）”");
                                                    }
                                                    over++;
                                                    sleep(3000);
                                                } else {
                                                    toastLog("正在浏览第" + i + "个店铺，剩余" + z + "秒后返回……");
                                                    sleep(2500);
                                                }
                                            }
                                            if (currentActivity() == "com.jd.lib.jshop.jshop.JshopMainShopActivity" || className("android.widget.EditText").findOnce() != null) {
                                                toastLog("仍然处于店铺中正在尝试返回种豆得豆界面");
                                                Justback();
                                                sleep(3000);
                                            }
                                        }
                                        break;
                                    } else if (a.bounds().top == X.top) {
                                        swipe(X.centerX(), X.centerY(), X.centerX(), X.centerY() + 300, 500);
                                    } else if (a.bounds().bottom == X.bottom) {
                                        swipe(X.centerX(), X.centerY(), X.centerX(), X.centerY() - 300, 500);
                                    }
                                }
                            }
                        }
                    } else if (text("关注频道任务").id("fd").findOnce() != null) {
                        var limit = Number(xz);
                        var over = 0;
                        try {
                            var X = id("fd").findOnce().bounds();
                        } catch (e) {
                            console.warn("当前活动：" + currentActivity() + "，当前包名：" + currentPackage() + "当前应用名：" + getAppName(currentPackage()));
                            toastLog("未成功进入“进入并关注”菜单界面，正在重试中……");
                            openInTask();
                            DoTask();

                        }
                        var ALL = className("android.view.View").text("进入并关注").find().size();
                        toastLog("【“进入并关注”数量】：" + ALL + "【可点击区域】：" + X.bottom, device.height);
                        for (var i = 0; i <= ALL; i++) {
                            while (true) {
                                if (over >= limit) {
                                    toastLog("“进入并关注”获得营养液已达每日上限" + limit + "，返回继续进行下一任务");
                                    if (className("android.widget.ImageView").desc("返回").clickable(true).findOnce() != null) {
                                        className("android.widget.ImageView").desc("返回").clickable(true).findOnce().click();
                                    } else {
                                        Justback();
                                    }
                                    sleep(3000);
                                    var i = ALL;
                                    var JustWait = 0;

                                    break;
                                } else if (i >= ALL) {
                                    toastLog("已找完全部" + ALL + "个店铺，在浏览" + i + "个店铺后共找到" + over + "瓶营养液，但未达到今日" + limit + "个上限")
                                    if (className("android.widget.ImageView").desc("返回").clickable(true).findOnce() != null) {
                                        className("android.widget.ImageView").desc("返回").clickable(true).findOnce().click();
                                    } else {
                                        Justback();
                                    }
                                    sleep(3000);
                                    var JustWait = 0;

                                    break;
                                } else {
                                    let a = className("android.view.View").text("进入并关注").findOnce(i);
                                    if (a == null) {
                                        toastLog("找不到“进入并关注”按钮，正在重新尝试中……");
                                        openInTask();
                                        DoTask();
                                        var JustWait = 0;

                                        break;
                                    } else if (a.clickable() == true) {
                                        a.click();
                                        toastLog("已盲点第" + i + "个“进入并关注”");
                                        for (let deng = 3; deng > 0; deng--) {
                                            if (className("android.view.View").text("恭喜获得1瓶营养液").findOnce() != null) {
                                                toastLog("恭喜获得1瓶营养液");
                                                over++;
                                                break;
                                            } else if (className("android.view.View").text("营养液走丢了，继续寻找吧~").findOnce() != null) {
                                                toastLog("营养液走丢了，继续寻找吧~");
                                                break;
                                            } else {
                                                toastLog("正在尝试查找“点击提示”，剩余" + deng + "秒……");
                                                sleep(1000);
                                            }
                                        }
                                        for (let a = 5; a > 0; a--) {
                                            toastLog("正在等待活动加载，剩余" + a + "秒……");
                                            sleep(1000);
                                        }
                                        if (id("com.jingdong.app.mall:id/fd").text("关注频道任务").findOnce() == null) {
                                            if (className("android.widget.ImageView").desc("返回").clickable(true).findOnce() != null) {
                                                className("android.widget.ImageView").desc("返回").clickable(true).findOnce().click();
                                                sleep(3000);
                                            } else {
                                                Justback();
                                                sleep(3000);
                                            }
                                        } else {
                                            toastLog("点击后未完成活动或未成功点击");
                                            sleep(2000);
                                        }
                                        break;
                                    } else if (a.bounds().top > X.bottom && a.bounds().bottom != device.height) {
                                        toastLog("【已点击】第" + i + "个“进入并关注”范围为：" + a.bounds().centerX(), a.bounds().centerY(), "上边缘点下边缘点分别为：" + a.bounds().top, a.bounds().bottom);
                                        click(a.bounds().centerX(), a.bounds().centerY());
                                        if (className("android.view.View").text("恭喜获得1瓶营养液").findOne(5000) != null) {
                                            toastLog("恭喜获得1瓶营养液");
                                            over++;
                                        }
                                        for (let a = 5; a > 0; a--) {
                                            toastLog("正在等待活动加载，剩余" + a + "秒……");
                                            sleep(2500);
                                        }
                                        if (id("com.jingdong.app.mall:id/fd").text("关注频道任务").findOnce() == null) {
                                            if (className("android.widget.ImageView").desc("返回").clickable(true).findOnce() != null) {
                                                className("android.widget.ImageView").desc("返回").clickable(true).findOnce().click();
                                                toastLog("已尝试盲点返回按钮");
                                                sleep(3000);
                                            } else {
                                                Justback();
                                                sleep(3000);
                                            }
                                        }
                                        break;
                                    } else if (a.bounds().top <= X.bottom) {
                                        swipe(device.width / 2, device.height / 2, device.width / 2, device.height / 2 + 300, 500);
                                    } else if (a.bounds().bottom == device.height) {
                                        swipe(device.width / 2, device.height / 2, device.width / 2, device.height / 2 - 300, 500);
                                    }
                                }
                            }
                        }
                    } else if (currentActivity() == "com.jingdong.common.jdreactFramework.activities.JDReactNativeCommonActivity" && className("android.widget.TextView").text("领京豆").findOnce() != null) {
                        if (className("android.widget.TextView").text("签到领京豆").findOnce() != null) {
                            let a = className("android.widget.TextView").text("签到领京豆").findOnce().bounds();
                            click(a.centerX(), a.centerY());
                            toastLog("已尝试点击“签到领京豆”按钮");
                            for (let dengw = 10; dengw > 0; dengw--) {
                                if (className("android.widget.Image").text("rqgw7ZXmQDKLeno6UJDwD4AAObPazg9A5AddKkSX").findOnce() != null) {
                                    click(className("android.widget.Image").text("rqgw7ZXmQDKLeno6UJDwD4AAObPazg9A5AddKkSX").findOnce().bounds().centerX(), className("android.widget.Image").text("rqgw7ZXmQDKLeno6UJDwD4AAObPazg9A5AddKkSX").findOnce().bounds().centerY());
                                    toastLog("已尝试点击“查看签到成功”按钮");
                                    sleep(2000);
                                } else if (className("android.view.View").text("今日签到成功奖励").findOnce() != null && className("android.view.View").text("今日签到成功奖励").findOnce().parent().parent().parent().childCount() > 1 &&
                                    className("android.view.View").text("今日签到成功奖励").findOnce().parent().parent().parent().child(1).childCount() > 0 && className("android.view.View").text("今日签到成功奖励").findOnce().parent().parent().parent().child(1).child(0).childCount() > 0 &&
                                    className("android.view.View").text("今日签到成功奖励").findOnce().parent().parent().parent().child(1).child(0).child(0).childCount() > 2 && className("android.view.View").text("今日签到成功奖励").findOnce().parent().parent().parent().child(1).child(0).child(0).child(2).text() != "" && className("android.view.View").text("今日签到成功奖励").findOnce().parent().parent().parent().child(1).child(0).child(0).child(2).text() != null) {
                                    toastLog("今日签到成功奖励：" + className("android.view.View").text("今日签到成功奖励").findOnce().parent().parent().parent().child(1).child(0).child(0).child(2).text() + "个京豆");
                                    sleep(2000);
                                    break;
                                } else if (className("android.widget.TextView").text("今日签到成功奖励").findOnce() != null && className("android.widget.TextView").text("今日签到成功奖励").findOnce().parent().parent().parent().childCount() > 1 &&
                                    className("android.widget.TextView").text("今日签到成功奖励").findOnce().parent().parent().parent().child(1).childCount() > 0 && className("android.widget.TextView").text("今日签到成功奖励").findOnce().parent().parent().parent().child(1).child(0).childCount() > 0 &&
                                    className("android.widget.TextView").text("今日签到成功奖励").findOnce().parent().parent().parent().child(1).child(0).child(0).childCount() > 2 && className("android.widget.TextView").text("今日签到成功奖励").findOnce().parent().parent().parent().child(1).child(0).child(0).child(2).text() != "" && className("android.widget.TextView").text("今日签到成功奖励").findOnce().parent().parent().parent().child(1).child(0).child(0).child(2).text() != null) {
                                    toastLog("今日签到成功奖励：" + className("android.widget.TextView").text("今日签到成功奖励").findOnce().parent().parent().parent().child(1).child(0).child(0).child(2).text() + "个京豆");
                                    sleep(2000);
                                    break;
                                } else {
                                    toastLog("正在等待“签到成功”界面加载，剩余" + dengw + "秒……");
                                    sleep(1000);
                                }
                            }
                            for (let f = 2; f > 0; f--) {
                                if (className("android.view.ViewGroup").depth(1).findOnce() != null) {
                                    let ba = className("android.view.ViewGroup").depth(1).findOnce().bounds();
                                    click(ba.centerX(), ba.centerY());
                                    toastLog("已尝试点击“返回按钮”");
                                    sleep(2000);
                                } else {
                                    Justback();
                                    sleep(2000);
                                }
                            }
                            var JustWait = 0;
                        } else if (className("android.widget.TextView").text("已连续签到").findOnce() != null) {
                            let b = className("android.widget.TextView").text("已连续签到").findOne().parent();
                            console.warn("若看到此日志，请截图提醒开发者！此处代码不应该运行的哦。");
                            if (b.childCount() != 3) {
                                toastLog("今日已签到，本处代码不应该运行的。");
                            } else {
                                toastLog(b.child(0).text() + b.child(1).text() + b.child(2).text());
                            }
                            if (className("android.view.ViewGroup").depth(1).findOnce() != null) {
                                let ba = className("android.view.ViewGroup").depth(1).findOnce().bounds();
                                click(ba.centerX(), ba.centerY());
                                toastLog("已尝试点击“返回按钮”");
                                sleep(2000);
                            } else {
                                Justback();
                                sleep(2000);
                            }
                            var JustWait = 0;
                        } else {
                            console.warn("当前活动：" + currentActivity() + "，当前包名：" + currentPackage() + "当前应用名：" + getAppName(currentPackage()));
                            toastLog("错误！未找到“签到领京豆”按钮，重新进入并重试中……");
                            openInTask();
                            DoTask();
                            var JustWait = 0;
                        }
                    } else if (className("android.widget.TextView").text("已获得").findOnce() != null) {
                        var limit = Number(xz);
                        var over = 0;
                        var i = 1;
                        while (true) {
                            let as = className("android.widget.TextView").text("x6").find();
                            for (var ii = 0; ii < className("android.widget.TextView").text("x6").find().length; ii++) {
                                if (as.get(ii) != null &&
                                    as.get(ii).parent().childCount() > 0 &&
                                    as.get(ii).parent().child(as.get(ii).parent().childCount() - 1).childCount() > 0 &&
                                    as.get(ii).parent().child(as.get(ii).parent().childCount() - 1).child(0).text() == "已完成") {
                                    toastLog("已成功完成“挑选商品”任务，正在尝试返回");
                                    if (className("android.widget.ImageView").desc("返回").clickable(true).findOnce() != null) {
                                        className("android.widget.ImageView").desc("返回").clickable(true).findOnce().click();
                                    } else {
                                        Justback();
                                    }
                                    sleep(3000);
                                    var JustWait = 0;
                                    var ii = -1;
                                }
                            }
                            if (ii == -1) {
                                break;
                            } else {
                                try {
                                    let p = className("android.widget.TextView").text("已获得").findOnce().parent().parent();
                                    let o = p.parent().child(p.parent().childCount() - 2);
                                    var C = o.child(0).child(0).child(2).child(0);
                                    let n = o.child(1).text();
                                    var Now = Number(n);
                                    let b = o.child(2).text();
                                    var ALL = b.replace("/", "");
                                } catch (e) {
                                    log(e);
                                    console.warn("当前活动：" + currentActivity() + "，当前包名：" + currentPackage() + "当前应用名：" + getAppName(currentPackage()));
                                    toastLog("未处于进入“选ta并关注”菜单界面，正在重试中……");
                                    openInTask();
                                    DoTask();
                                    var JustWait = 0;
                                    break;
                                }
                                toastLog("当前为第" + Now + "个卡片，卡片总数为" + ALL);
                                if (over >= limit) {
                                    toastLog("“选ta并关注”获得营养液已达每日上限" + limit + "，返回继续进行下一任务");
                                    if (className("android.widget.ImageView").desc("返回").clickable(true).findOnce() != null) {
                                        className("android.widget.ImageView").desc("返回").clickable(true).findOnce().click();
                                    } else {
                                        Justback();
                                    }
                                    sleep(3000);
                                    var JustWait = 0;
                                    break;
                                } else if (i >= ALL) {
                                    toastLog("已找完全部" + ALL + "个店铺，在浏览" + i + "个店铺后共找到" + over + "瓶营养液，但未达到今日" + limit + "个上限")
                                    if (className("android.widget.ImageView").desc("返回").clickable(true).findOnce() != null) {
                                        className("android.widget.ImageView").desc("返回").clickable(true).findOnce().click();
                                    } else {
                                        Justback();
                                    }
                                    sleep(3000);
                                    var JustWait = 0;
                                    break;
                                } else {
                                    if (Now != i) {
                                        if (Now < i) {
                                            swipe(C.bounds().centerX(), C.bounds().centerY(), 0, C.bounds().centerY(), 500);
                                        } else if (Now > i) {
                                            swipe(C.bounds().centerX(), C.bounds().centerY(), C.bounds().width(), C.bounds().centerY(), 500);
                                        }
                                        toastLog("已尝试按顺序滑动至第" + i + "个卡片");
                                        sleep(2000);
                                    } else {
                                        let a = C.child(C.childCount() - 1).bounds();
                                        click(a.centerX(), a.centerY());
                                        toastLog("已尝试点击“选ta并关注”按钮");
                                        if (text("关注成功，获得1瓶营养液").findOne(5000) != null) {
                                            toastLog("关注成功，获得1瓶营养液");
                                            over++;
                                        }
                                        for (let deng = 3; deng > 0; deng--) {
                                            if (text("关注成功，获得1瓶营养液").findOnce() != null || desc("关注成功，获得1瓶营养液").findOnce() != null) {
                                                toastLog("关注成功，获得1瓶营养液");
                                                over++;
                                                break;
                                            } else if (text("营养液走丢了，继续寻找吧~").findOnce() != null) {
                                                toastLog("营养液走丢了，继续寻找吧~");
                                                break;
                                            } else {
                                                toastLog("正在尝试查找“点击提示”，剩余" + deng + "秒……");
                                                sleep(1000);
                                            }
                                        }
                                        for (var loop = 5; loop > 0; loop--) {
                                            if (currentActivity() == "com.jd.lib.productdetail.ProductDetailActivity" || id("com.jd.lib.productdetail:id/akl").findOnce() != null) {
                                                var loop = 0;
                                                sleep(2000);
                                                if (className("android.widget.ImageView").desc("返回").clickable(true).findOnce() != null) {
                                                    className("android.widget.ImageView").desc("返回").clickable(true).findOnce().click();
                                                    toastLog("已盲点返回");
                                                    sleep(3000);
                                                } else {
                                                    Justback();
                                                    sleep(3000);
                                                }
                                            } else {
                                                toastLog("正在等待商品页加载，剩余" + loop + "秒……");
                                                sleep(2000);
                                            }
                                        }
                                        i++;
                                    }
                                }
                            }
                        }
                    } else if (id("com.jingdong.app.mall:id/fd").text("评价中心").findOnce() != null && text("没有待评价的商品哦~").findOnce() != null) {
                        var DoNotDoPJRW = 1;
                        toastLog("评价商品任务内无任何商品可评价");
                        if (className("android.widget.ImageView").desc("返回").clickable(true).findOnce() != null) {
                            className("android.widget.ImageView").desc("返回").clickable(true).findOnce().click();
                        } else {
                            Justback();
                        }
                        sleep(3000);
                        var JustWait = 0;
                    } else if (id("com.jingdong.app.mall:id/fd").text("评价中心").findOnce() != null) {
                        for (let i = 1; i > 0; i--) {
                            if (id("com.jd.lib.evaluatecenter:id/abm").className("android.widget.TextView").clickable(true).text("评价").findOnce() != null) {
                                id("com.jd.lib.evaluatecenter:id/abm").className("android.widget.TextView").clickable(true).text("评价").findOnce().click();
                                toastLog("已尝试点击第" + i + "个评价按钮");
                                sleep(3000);
                                if (id("com.jd.lib.evaluatecenter:id/akh").text("匿名评价").findOnce() != null && id("com.jd.lib.evaluatecenter:id/akh").text("匿名评价").findOnce().checked() == false) {
                                    id("com.jd.lib.evaluatecenter:id/akh").text("匿名评价").findOnce().click();
                                    toastLog("已尝试点击“匿名评价”按钮");
                                    sleep(3000);
                                }
                                if (id("com.jingdong.app.mall:id/a9b").className("android.widget.TextView").text("提交").clickable(true).findOnce() != null) {
                                    id("com.jingdong.app.mall:id/a9b").className("android.widget.TextView").text("提交").clickable(true).findOnce().click();
                                    toastLog("已尝试点击“提交评价”按钮");
                                    sleep(3000);
                                    for (let a = 2; a > 0; a--) {
                                        if (desc("返回").clickable(true).findOnce() != null) {
                                            desc("返回").clickable(true).findOnce().click();
                                            toastLog("已尝试盲点“返回按钮”");
                                            sleep(2000);
                                        } else {
                                            Justback();
                                            sleep(1000);
                                        }
                                    }
                                }
                            } else {
                                toastLog("当前已无任何可评价商品");
                                if (desc("返回").clickable(true).findOnce() != null) {
                                    desc("返回").clickable(true).findOnce().click();
                                    toastLog("已尝试盲点“返回按钮”");
                                    sleep(2000);
                                } else {
                                    Justback();
                                    sleep(1000);
                                }
                            }
                        }
                        var DoNotDoPJRW = 1;
                        toastLog("评价商品任务已完成");
                        var JustWait = 0;
                    } else {
                        toastLog("正在等待任务界面加载，剩余" + JustWait + "秒……");
                        sleep(1000);
                    }
                }
                if (RwTitle == "逛逛会场") {
                    var DoNotDoGGHC = 1;
                }
                if (MakeSureInHD() == false) {
                    toastLog("尝试返回“任务列表”界面");
                    if (className("android.widget.ImageView").desc("返回").clickable(true).findOnce() != null) {
                        className("android.widget.ImageView").desc("返回").clickable(true).findOnce().click();
                    } else {
                        Justback();
                    }
                    sleep(3000);
                }
            } else {
                if (now == xz) {
                    toastLog("【任务已完成】" + RwTitle + "(" + ZhuangTai + ")");
                } else {
                    toastLog("【已跳过】" + RwTitle + "(" + ZhuangTai + ")");
                }
                ax++;
            }
        }
    }
    alert("“种豆得豆自动脚本”：\n任务已完成");
    exit();
}
firstD();

function firstD() {
    if (context_Manualstate == 1) {
        toastLog("已手动模式运行脚本");
        var options = ["等待20秒", "等待30秒", "等待50秒", "等待60秒", "等待10秒"]
        var i = dialogs.select("??以“手动模式”运行脚本\n\n接下来您需要在提示出现后自行打开京东APP至活动页”\n\n请选择脚本等待您打开京东的时间", options);
        if (i >= 0) {
            toast("您选择的是" + options[i]);
        } else if (i < 0) {
            toastLog("您取消了选择");
            dialogs_js();
            firstD();
        }
        if (i == 0) {
            //等待20秒
            var deng = 20;
        } else if (i == 1) {
            //等待30秒
            var deng = 30;
        } else if (i == 2) {
            //等待50秒
            var deng = 50;
        } else if (i == 3) {
            //等待60秒
            var deng = 60;
        } else if (i == 4) {
            //等待10秒
            var deng = 10;
        }
        for (deng = deng; deng > 0; deng--) {
            toastLog("请打开京东至种豆得豆的主界面\n剩余" + deng + "秒后运行脚本...");
            sleep(1111);
        }
        DoTask();
    } else {
        openInTask();
        DoTask();
    }
}