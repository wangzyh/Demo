log("*   �� The Animal Protecting ��");
log("*������������������+ +");
log("*�������ߩ��������ߩ� + +");
log("*��������������������");
log("*�������������������� ++ + + +");
log("*�������������������� ��+");
log("*�������������������� +");
log("*�����������ߡ�������")
log("*�������������������� + +");
log("*��������������������");
log("*����������������");
log("*���������������� + + + +");
log("*������������������������");
log("*���������������� + ��");
log("*����������������")
log("*��������������������+");
log("*������������������������ + +")
log("*�����������������������ǩ�+ + + ");
log("*��������������������������+ +");
log("*�����������������ש����� + ");
log("*�����������ϩϡ����ϩ�");
log("*�����������ߩ������ߩ�+ + ");
log("*    Code is far away from bug!");
log("*        ���ޱ���,������bug");
try {
    if (contextPASS != undefined) {
        log("[?]��ʱ���������ű�");
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
    var ScriptVersion = ("Beta1.2"); //�汾
    log("����ű��ѿ�ʼ���У����û�е����˵���ǿ��ֹͣ�ٴ򿪱������");
    var options_ = ["?? ��ʼ���нű�", "?? ��ʱ���нű�", "? ��ʱ���нű�", "? ֹͣ���нű�", "?? ���ط�������", "?? �ֶ���ģʽ", "?? ��˾/��־�л�"]
    var i = dialogs.select("*+*+*+* �����νű� *+*+*+*\n*+*+*+*  Orange Js *+*+*+*\n\n��ӭʹ�� (?????)?" + "\n" + "���ֶ��ö��Զ��ű���" + ScriptVersion + "\n��ѡ��һ��Ҫ���е�ѡ��", options_);
    if (i < 0) {
        toastLog("û��ѡ������رնԻ���\n  ��ѡ��ֹͣ���нű���");
        dialogs_js();
    } else if (i == 0) {
        toastLog(options_[i]);
        context_Manualstate = 0;
        Set_Back_way();
    } else if (i == 3) {
        toastLog(options_[i]);
        exit();
    } else if (i == 1) {
        toastLog("���Ժ����ڼ��Ȩ��...");
        context_Manualstate = 0;
        toastLog(options_[i]);
        device.keepScreenDim();
        toastLog("���Ȩ�����á���");
        context_Manualstate = 0;
        toastLog("�ȴ����ϰ�Ȩ�޿�������\n�������ֶ����豾������ϰ�Ȩ��\n����������޷�������");
        auto.waitFor();
        toastLog("���ϰ�Ȩ���ѿ���" + "\n" + "�������нű�����");
        sleep(2000);
        toastLog("Ϊ��֤�ű���������\n�����豾���������Ȩ��");
        sleep(2000);
        var test_rawWindow = floaty.rawWindow(
            <frame gravity="center" bg="#00000000"/>
        );
        test_rawWindow.setSize(-1, -1);
        test_rawWindow.setTouchable(false);
        setTimeout(() => {
            test_rawWindow.close();
        }, 1000);
        toastLog("������Ȩ���ѿ�����");
        sleep(2000);
        wait_Time_over();
    } else if (i == 2) {
        toastLog("���Ժ����ڼ��Ȩ��...");
        context_Manualstate = 0;
        toastLog(options_[i]);
        device.keepScreenDim();
        toastLog("���Ȩ�����á���");
        context_Manualstate = 0;
        toastLog("�ȴ����ϰ�Ȩ�޿�������\n�������ֶ����豾������ϰ�Ȩ��\n����������޷�������");
        auto.waitFor();
        toastLog("���ϰ�Ȩ���ѿ���" + "\n" + "�������нű�����");
        sleep(2000);
        toastLog("Ϊ��֤�ű���������\n�����豾���������Ȩ��");
        sleep(2000);
        var test_rawWindow = floaty.rawWindow(
            <frame gravity="center" bg="#00000000"/>
        );
        test_rawWindow.setSize(-1, -1);
        test_rawWindow.setTouchable(false);
        setTimeout(() => {
            test_rawWindow.close();
        }, 1000);
        toastLog("������Ȩ���ѿ�����");
        context_Manualstate = 0;
        Set_Back_way();
        DS();
        device.keepScreenDim();
    } else if (i == 4) {
        toastLog(options_[i]);
        try {
            if (files.exists("/storage/emulated/0/OrangeJs/�ֶ��ö��Զ��ű�/���ط�������.txt") == true && files.read("/storage/emulated/0/OrangeJs/�ֶ��ö��Զ��ű�/���ط�������.txt") > 2 && files.exists("/storage/emulated/0/OrangeJs/�ֶ��ö��Զ��ű�/���������ٶ�.txt") == false) {
                files.remove("/storage/emulated/0/OrangeJs/�ֶ��ö��Զ��ű�/���ط�������.txt");
                log("��ǰ���ط�������Ϊ�������ص�δ���û��������ٶ�");
            }
            if (files.exists("/storage/emulated/0/OrangeJs/�ֶ��ö��Զ��ű�/���ط�������.txt") == true) {
                files.rename("/storage/emulated/0/OrangeJs/�ֶ��ö��Զ��ű�/���ط�������.txt", "X���ط�������.txt");
                Set_Back_way();
            } else {
                dialogs.alert("��δ�����κη��ط����������нű����ٽ����޸�");
                dialogs_js();
            }
        } catch (e) {
            dialogs.alert("δ���豾������洢Ȩ�ޡ�", "����ڵ����ô洢����Ҫ���洢Ȩ�ޡ����������������ã�����Ҫ�������豾������洢Ȩ�ޡ���������ʹ�����ñ��湦��");
            dialogs_js();
        }
    } else if (i == 5) {
        toastLog(options_[i]);
        context_Manualstate = 1;
        Set_Back_way() //�����ֶ�ģʽ
    } else if (i == 6) {
        toastLog(options_[i]);
        context_Manualstate = 0;
        if (files.exists("/storage/emulated/0/OrangeJs/�ֶ��ö��Զ��ű�/��˾or��־.txt") == true) {
            var z = files.read("/storage/emulated/0/OrangeJs/�ֶ��ö��Զ��ű�/��˾or��־.txt");
            if (z != "��˾" && z != "��־") {
                alert("����˾or��־���ļ������ѳ���ɾ�������ļ�");
                try {
                    files.remove("/storage/emulated/0/OrangeJs/�ֶ��ö��Զ��ű�/��˾or��־.txt");
                } catch (e) {
                    toastLog("ɾ������˾or��־���ļ�ʧ�ܣ�");
                }
                var Z = "";
            } else {
                var Z = "��ǰ�ű�ʹ�ã�" + z + "\n";
            }
        } else {
            var Z = "";
        }
        let da = dialogs.select(Z + "��ѡ��һ��ѡ��", "ʹ����˾��Toast��", "ʹ�ýű�������־")
        if (da == 0) {
            toastLog("��ѡ���ˣ�ʹ����˾");
            try {
                var T = 0;
                files.createWithDirs("/storage/emulated/0/OrangeJs/�ֶ��ö��Զ��ű�/��˾or��־.txt");
                files.write("/storage/emulated/0/OrangeJs/�ֶ��ö��Զ��ű�/��˾or��־.txt", "��˾");
            } catch (e) {
                log("δ����洢Ȩ�޻�洢Ȩ�޴��󣬵�ǰ����Ϊ��˾");
                var T = 0;
            }
        } else if (da == 1) {
            toastLog("��ѡ���ˣ�ʹ��������־");
            try {
                var T = 1;
                files.createWithDirs("/storage/emulated/0/OrangeJs/�ֶ��ö��Զ��ű�/��˾or��־.txt");
                files.write("/storage/emulated/0/OrangeJs/�ֶ��ö��Զ��ű�/��˾or��־.txt", "��־");
            } catch (e) {
                log("δ����洢Ȩ�޻�洢Ȩ�޴��󣬿���������־");
                var T = 1;
            }
        }
        dialogs_js();
    }
}



function Set_Back_way() {
    try {
        if (files.exists("/storage/emulated/0/OrangeJs/�ֶ��ö��Զ��ű�/���ط�������.txt") == true) {
            context_i_back = files.read("/storage/emulated/0/OrangeJs/�ֶ��ö��Զ��ű�/���ط�������.txt");
            log("���ط�����" + context_i_back);
            if (context_i_back > 2) {
                try {
                    context_gestures_speed = files.read("/storage/emulated/0/OrangeJs/�ֶ��ö��Զ��ű�/���������ٶ�.txt")
                    log("���������ٶȣ�" + context_gestures_speed)
                } catch (e) {
                    log("�ϴ�δ��ɻ��������ٶ�����");
                    files.remove("/storage/emulated/0/OrangeJs/�ֶ��ö��Զ��ű�/���ط�������.txt");
                    Set_Back_way();
                }
            }
        } else {
            //?????�趨���ط����������ٶȵĴ���
            var options_hq = ["?? ��ͨ�ķ���\n(ʹ�����ϰ�Ȩ��)", "#? ʹ��ROOT����\n(�������豾���ROOTȨ��)", "?? ͨ�����������������\n�������߾ȹ����� ���������ؾ�ʧЧ\n    �����Դ˷����ɣ�", "?????????????????????? \n����Ļ�м�������ڻ���\n(ȫ�������Ʒ��� ����:С��MIUI)", "              ?????????????????????? \n����Ļ�м�������ڻ���\n(ȫ�������Ʒ��� ����:��ΪEMUI)", "?????????????????????? \n����Ļ����·����ϻ���\n(ȫ�������Ʒ��� ����:����Smartisan UI)", "               ????????????????? \n����Ļ�Ҳ��·����ϻ���\n(ȫ�������Ʒ���)"]
            var i_back = dialogs.select(" Hi! ( ?��? )\n��ѡ��һ������\n����ʵ�ַ��ز���", options_hq);
            if (i_back >= 0) {
                toastLog("��ѡ�����" + options_hq[i_back]);
                sleep(2000);
                var options_select = options_hq[i_back];
                context_i_back = i_back;
                files.createWithDirs("/storage/emulated/0/OrangeJs/�ֶ��ö��Զ��ű�/���ط�������.txt");
                files.write("/storage/emulated/0/OrangeJs/�ֶ��ö��Զ��ű�/���ط�������.txt", context_i_back);
            } else {
                toastLog("û��ѡ�񷵻ط�����");
                device.cancelKeepingAwake();
            }
            if (i_back > 2) {
                var options_hd = ["200����\n(Ĭ�ϣ����̫����ѡ����)", "500����", "800����", "1��(1000����)", "1.5�루1500���룩", "2�루2000���룩"]
                var iix = dialogs.select("Ok! (???) ��ѡ����:\n" + options_select + "\n��ѡ�񻬶��ٶ�\n��λ:���루1��=1000���룩", options_hd);
                if (iix < 0) {
                    toastLog("û��ѡ�񻬶��ٶ�");
                    Set_Back_way();
                } else {
                    if (iix == 0) {
                        context_gestures_speed = 200;
                        toastLog("�����ٶ��趨Ϊ\n" + context_gestures_speed + "����");
                        sleep(2000);
                    }
                    if (iix == 1) {
                        context_gestures_speed = 500;
                        toastLog("�����ٶ��趨Ϊ\n" + context_gestures_speed + "����");
                        sleep(2000);
                    }
                    if (iix == 2) {
                        context_gestures_speed = 800;
                        toastLog("�����ٶ��趨Ϊ\n" + context_gestures_speed + "����");
                        sleep(2000);
                    }
                    if (iix == 3) {
                        context_gestures_speed = 1000;
                        toastLog("�����ٶ��趨Ϊ\n" + context_gestures_speed + "����");
                        sleep(2000);
                    }
                    if (iix == 4) {
                        context_gestures_speed = 1500;
                        toastLog("�����ٶ��趨Ϊ\n" + context_gestures_speed + "����");
                        sleep(2000);
                    }
                    if (iix == 5) {
                        context_gestures_speed = 2000;
                        toastLog("�����ٶ��趨Ϊ\n" + context_gestures_speed + "����");
                        sleep(2000);
                    }
                    files.createWithDirs("/storage/emulated/0/OrangeJs/�ֶ��ö��Զ��ű�/���������ٶ�.txt");
                    files.write("/storage/emulated/0/OrangeJs/�ֶ��ö��Զ��ű�/���������ٶ�.txt", context_gestures_speed);
                }
            }
            if (files.exists("/storage/emulated/0/OrangeJs/�ֶ��ö��Զ��ű�/���ط�������.txt") == true && files.exists("/storage/emulated/0/OrangeJs/�ֶ��ö��Զ��ű�/X���ط�������.txt") == true) {
                log("ɾ��");
                files.remove("/storage/emulated/0/OrangeJs/�ֶ��ö��Զ��ű�/X���ط�������.txt");
                dialogs_js();
            } else if (files.exists("/storage/emulated/0/OrangeJs/�ֶ��ö��Զ��ű�/X���ط�������.txt") == true) {
                log("������");
                files.rename("/storage/emulated/0/OrangeJs/�ֶ��ö��Զ��ű�/X���ط�������.txt", "���ط�������.txt");
                dialogs_js();
            }
        }
    } catch (e) {
        log("δ���衰�洢Ȩ�ޡ�");
        var options_hq = ["?? ��ͨ�ķ���\n(ʹ�����ϰ�Ȩ��)", "#? ʹ��ROOT����\n(�������豾���ROOTȨ��)", "?? ͨ�����������������\n�������߾ȹ����� ���������ؾ�ʧЧ\n    �����Դ˷����ɣ�", "?????????????????????? \n����Ļ�м�������ڻ���\n(ȫ�������Ʒ��� ����:С��MIUI)", "              ?????????????????????? \n����Ļ�м�������ڻ���\n(ȫ�������Ʒ��� ����:��ΪEMUI)", "?????????????????????? \n����Ļ����·����ϻ���\n(ȫ�������Ʒ��� ����:����Smartisan UI)", "               ????????????????? \n����Ļ�Ҳ��·����ϻ���\n(ȫ�������Ʒ���)"]
        var i_back = dialogs.select(" Hi! ( ?��? )\n��ѡ��һ������\n����ʵ�ַ��ز���", options_hq);
        if (i_back >= 0) {
            toastLog("��ѡ�����" + options_hq[i_back]);
            sleep(2000);
            var options_select = options_hq[i_back];
            context_i_back = i_back;
        } else {
            toastLog("û��ѡ�񷵻ط�����");
            device.cancelKeepingAwake();
        }
        if (i_back > 2) {
            var options_hd = ["200����\n(Ĭ�ϣ����̫����ѡ����)", "500����", "800����", "1��(1000����)", "1.5�루1500���룩", "2�루2000���룩"]
            var iix = dialogs.select("Ok! (???) ��ѡ����:\n" + options_select + "\n��ѡ�񻬶��ٶ�\n��λ:���루1��=1000���룩", options_hd);
            if (iix < 0) {
                toastLog("û��ѡ�񻬶��ٶ�");
                Set_Back_way();
            } else {
                if (iix == 0) {
                    context_gestures_speed = 200;
                    toastLog("�����ٶ��趨Ϊ\n" + context_gestures_speed + "����");
                    sleep(2000);
                }
                if (iix == 1) {
                    context_gestures_speed = 500;
                    toastLog("�����ٶ��趨Ϊ\n" + context_gestures_speed + "����");
                    sleep(2000);
                }
                if (iix == 2) {
                    context_gestures_speed = 800;
                    toastLog("�����ٶ��趨Ϊ\n" + context_gestures_speed + "����");
                    sleep(2000);
                }
                if (iix == 3) {
                    context_gestures_speed = 1000;
                    toastLog("�����ٶ��趨Ϊ\n" + context_gestures_speed + "����");
                    sleep(2000);
                }
                if (iix == 4) {
                    context_gestures_speed = 1500;
                    toastLog("�����ٶ��趨Ϊ\n" + context_gestures_speed + "����");
                    sleep(2000);
                }
                if (iix == 5) {
                    context_gestures_speed = 2000;
                    toastLog("�����ٶ��趨Ϊ\n" + context_gestures_speed + "����");
                    sleep(2000);
                }
            }
        }
    }
}

sleep(1000);
toastLog("�ȴ����ϰ�Ȩ�޿�������\n�������ֶ����豾������ϰ�Ȩ��\n����������޷�������");
auto.waitFor();
toastLog("���ϰ�Ȩ���ѿ���" + "\n" + "�������нű�����");
if (files.exists("/storage/emulated/0/OrangeJs/�ֶ��ö��Զ��ű�/��˾or��־.txt") == true) {
    try {
        let z = files.read("/storage/emulated/0/OrangeJs/�ֶ��ö��Զ��ű�/��˾or��־.txt");
        if (z == "��˾") {
            var T = 0;
        } else if (z == "��־") {
            var T = 1;
        } else {
            toastLog("����˾or��־���ļ������ѳ���ɾ����ʹ��Ĭ����־");
            try {
                files.remove("/storage/emulated/0/OrangeJs/�ֶ��ö��Զ��ű�/��˾or��־.txt");
            } catch (e) {
                toastLog("ɾ������˾or��־���ļ�ʧ�ܣ�");
            }
            var T = 1;
        }
    } catch (e) {
        if (T == null) {
            log("δ����洢Ȩ�޻�洢Ȩ�޴���Ĭ�Ͽ���������־");
            var T = 1;
        }
    }
} else {
    try {
        files.createWithDirs("/storage/emulated/0/OrangeJs/�ֶ��ö��Զ��ű�/��˾or��־.txt");
        files.write("/storage/emulated/0/OrangeJs/�ֶ��ö��Զ��ű�/��˾or��־.txt", "��־");
        var T = 1;
        log("Ĭ��ʹ����־����������������˵�����");
    } catch (e) {
        log("δ����洢Ȩ�޻�洢Ȩ�޴���Ĭ�Ͽ���������־");
        var T = 1;
    }
}

function wait_Time_over() {
    var i_wait = dialogs.singleChoice("?? ��ʱ����\n\n(��?��)??\n��ѡ��һ��ѡ��\n��ʱ�������Զ�����", ["1���Ӻ�����", "5���Ӻ�����", "10���Ӻ�����", "30���Ӻ�����", "һСʱ������", "��Сʱ������", "��Сʱ������", "��Сʱ������", "��Сʱ������"], 2);
    if (i_wait < 0) {
        toast("��ȡ����ѡ��");
        device.cancelKeepingAwake();
        dialogs_js();
    }
    if (i_wait >= 0) {
        context_i_wait = i_wait;
    }
    if (i_wait == 0) {
        var choice_confirm = dialogs.confirm("��ѡ����1���Ӻ�����", "���ȷ������һ���趨���ز����ķ����󣬽ű��������趨��ʱ�������ʼ�Զ�����\n�벻Ҫ��������ĺ�̨���������ֻ��ȣ�������ܻ���ɶ�ʱ����ʧЧ");
        if (choice_confirm == false) {
            toastLog("ȡ���˶�ʱ����ȷ��");
            wait_Time_over();
        } else {
            Set_Back_way();
            waiting_time();
        }
    }
    if (i_wait == 1) {
        var choice_confirm = dialogs.confirm("��ѡ����5���Ӻ�����", "���ȷ������һ���趨���ز����ķ����󣬽ű��������趨��ʱ�������ʼ�Զ�����\n�벻Ҫ��������ĺ�̨���������ֻ��ȣ�������ܻ���ɶ�ʱ����ʧЧ");
        if (choice_confirm == false) {
            toastLog("ȡ���˶�ʱ����ȷ��");
            wait_Time_over();
        } else {
            Set_Back_way();
            waiting_time();
        }
    }
    if (i_wait == 2) {
        var choice_confirm = dialogs.confirm("��ѡ����10���Ӻ�����", "���ȷ������һ���趨���ز����ķ����󣬽ű��������趨��ʱ�������ʼ�Զ�����\n�벻Ҫ��������ĺ�̨���������ֻ��ȣ�������ܻ���ɶ�ʱ����ʧЧ");
        if (choice_confirm == false) {
            toastLog("ȡ���˶�ʱ����ȷ��");
            wait_Time_over();
        } else {
            Set_Back_way();
            waiting_time();
        }
    }
    if (i_wait == 3) {
        var choice_confirm = dialogs.confirm("��ѡ����30���Ӻ�����", "���ȷ������һ���趨���ز����ķ����󣬽ű��������趨��ʱ�������ʼ�Զ�����\n�벻Ҫ��������ĺ�̨���������ֻ��ȣ�������ܻ���ɶ�ʱ����ʧЧ");
        if (choice_confirm == false) {
            toastLog("ȡ���˶�ʱ����ȷ��");
            wait_Time_over();
        } else {
            Set_Back_way();
            waiting_time();
        }
    }
    if (i_wait == 4) {
        var choice_confirm = dialogs.confirm("��ѡ����һСʱ������", "���ȷ������һ���趨���ز����ķ����󣬽ű��������趨��ʱ�������ʼ�Զ�����\n�벻Ҫ��������ĺ�̨���������ֻ��ȣ�������ܻ���ɶ�ʱ����ʧЧ");
        if (choice_confirm == false) {
            toastLog("ȡ���˶�ʱ����ȷ��");
            wait_Time_over();
        } else {
            Set_Back_way();
            waiting_time();
        }
    }
    if (i_wait == 5) {
        var choice_confirm = dialogs.confirm("��ѡ������Сʱ������", "���ȷ������һ���趨���ز����ķ����󣬽ű��������趨��ʱ�������ʼ�Զ�����\n�벻Ҫ��������ĺ�̨���������ֻ��ȣ�������ܻ���ɶ�ʱ����ʧЧ");
        if (choice_confirm == false) {
            toastLog("ȡ���˶�ʱ����ȷ��");
            wait_Time_over();
        } else {
            Set_Back_way();
            waiting_time();
        }
    }
    if (i_wait == 6) {
        var choice_confirm = dialogs.confirm("��ѡ������Сʱ������", "���ȷ������һ���趨���ز����ķ����󣬽ű��������趨��ʱ�������ʼ�Զ�����\n�벻Ҫ��������ĺ�̨���������ֻ��ȣ�������ܻ���ɶ�ʱ����ʧЧ");
        if (choice_confirm == false) {
            toastLog("ȡ���˶�ʱ����ȷ��");
            wait_Time_over();
        } else {
            Set_Back_way();
            waiting_time();
        }
    }
    if (i_wait == 7) {
        var choice_confirm = dialogs.confirm("��ѡ������Сʱ������", "���ȷ������һ���趨���ز����ķ����󣬽ű��������趨��ʱ�������ʼ�Զ�����\n�벻Ҫ��������ĺ�̨���������ֻ��ȣ�������ܻ���ɶ�ʱ����ʧЧ");
        if (choice_confirm == false) {
            toastLog("ȡ���˶�ʱ����ȷ��");
            wait_Time_over
        } else {
            Set_Back_way();
            waiting_time();
        }
    }
    if (i_wait == 8) {
        var choice_confirm = dialogs.confirm("��ѡ���˰�Сʱ������", "���ȷ������һ���趨���ز����ķ����󣬽ű��������趨��ʱ�������ʼ�Զ�����\n�벻Ҫ��������ĺ�̨���������ֻ��ȣ�������ܻ���ɶ�ʱ����ʧЧ");
        if (choice_confirm == false) {
            toastLog("ȡ���˶�ʱ����ȷ��");
            wait_Time_over();
        } else {
            Set_Back_way();
            waiting_time();
        }
    }
}

function waiting_time() {
    //��ʱ���нű�
    if (context_i_wait == 0) {
        var Seconds = 60;
        for (Seconds == 60; Seconds > 0; Seconds--) {
            console.warn("����ʱ���С���ʱ�С���\n" + Seconds + "���ʼ����");
            sleep(1000);
        }
    }
    if (context_i_wait == 1) {
        var Minutes = 4;
        for (Minutes == 4; Minutes >= 0; Minutes--) {
            if (Minutes >= 0) {
                var Seconds = 60;
                for (Seconds == 60; Seconds > 0; Seconds--) {
                    console.warn("����ʱ���С���ʱ�С���\n" + Minutes + "����" + Seconds + "���ʼ����");
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
                    console.warn("����ʱ���С���ʱ�С���\n" + Minutes + "����" + Seconds + "���ʼ����");
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
                    console.warn("����ʱ���С���ʱ�С���\n" + Minutes + "����" + Seconds + "���ʼ����");
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
                    console.warn("����ʱ���С���ʱ�С���\n" + Minutes + "����" + Seconds + "���ʼ����");
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
                        console.warn("����ʱ���С���ʱ�С���\n" + Hours + "Сʱ" + Minutes + "����" + Seconds + "���ʼ����");
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
                        console.warn("����ʱ���С���ʱ�С���\n" + Hours + "Сʱ" + Minutes + "����" + Seconds + "���ʼ����");
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
                        console.warn("����ʱ���С���ʱ�С���\n" + Hours + "Сʱ" + Minutes + "����" + Seconds + "���ʼ����");
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
                        console.warn("����ʱ���С���ʱ�С���\n" + Hours + "Сʱ" + Minutes + "����" + Seconds + "���ʼ����");
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
        var ʱ = dialogs.rawInput("??��ʱ�����֡������ȷ��\n\n������0-23��Сʱ��\n����ʱ��ű����Զ�����");
        if (ʱ == null) {
            //û������
            toastLog("û�����룡�������˵�");
            var While = 0;
            dialogs_js();
        } else if (ʱ == "") {
            //û������
            toastLog("û�����룡�������˵�");
            var While = 0;
            dialogs_js();
        } else if (ʱ >= 0) {
            if (ʱ < 24) {
                var While = 2;
                while (While == 2) {
                    var �� = dialogs.rawInput("??��ʱ??���֡������ȷ��\n\n������0-59�ķ�����\n\n" + ʱ + "ʱ" + "?��?��");
                    if (�� == null) {
                        toastLog("û�����룡�����ϼ�");
                        var While = 1;
                    } else if (�� == null) {
                        toastLog("û�����룡�����ϼ�");
                        var While = 1;
                    } else if (�� >= 0) {
                        if (�� < 60) {
                            var While = 3;
                            while (While == 3) {
                                var �� = dialogs.rawInput("??��ʱ??����??�����ȷ��\n\n������0-59������\n\n" + ʱ + "ʱ" + �� + "��?��");
                                if (�� == null) {
                                    toastLog("û�����룡�����ϼ�");
                                    var While = 2;
                                } else if (�� == null) {
                                    toastLog("û�����룡�����ϼ�");
                                    var While = 2;
                                } else if (�� >= 0) {
                                    if (�� < 60) {
                                        var QR = dialogs.confirm("�ű�����\n?" + ʱ + "ʱ" + �� + "��" + �� + "��\n׼ʱ���У�", "�����������ȡ��\n���ȷ����ʱ����ʱ״̬��������־�в鿴");
                                        if (QR == false) {
                                            //�������˵�
                                            var While = 1;
                                        } else {
                                            var While = 0;
                                            //����ʱ����һ��
                                            while (true) {
                                                var myDate = new Date();
                                                if (myDate.getHours() == ʱ && myDate.getMinutes() == �� && myDate.getSeconds() == ��) {
                                                    console.warn("ʱ�䵽����ʼ���нű���" + myDate.getHours() + "ʱ" + myDate.getMinutes() + "��" + myDate.getSeconds() + "��");
                                                    device.wakeUpIfNeeded();
                                                    break;
                                                }
                                                sleep(1000);
                                                console.info("������" + myDate.getHours() + "ʱ" + myDate.getMinutes() + "��" + myDate.getSeconds() + "��\n�ű�����" + ʱ + "ʱ" + �� + "��" + �� + "�룬׼ʱ���У�\n�뱣���ֻ����ڹ���״̬����Ҫ�����ػ���");
                                            }
                                        }
                                    } else {
                                        toastLog("������������С�ڵ���60");
                                    }
                                } else {
                                    toastLog("��������������ڵ���0");
                                }
                            }
                        } else {
                            toastLog("������󣡷��ӱ���С��60");
                        }
                    } else {
                        toastLog("������󣡷��ӱ�����ڵ���0");
                    }
                }
            } else {
                toastLog("�������ʱ�����С��24");
            }
        } else {
            toastLog("�������ʱ�������ڵ���0");
        }
    }
}

//������������
var window = floaty.window(
    <frame>
        <button id="action" text="���ֹͣ�ű�" w="120" h="40" bg="#F0EB4336"/>
    </frame>
);
setInterval(() => {}, 1000);
var execution = null;
//��¼����������ʱ�Ĵ�������
var x = 0,
    y = 0;
//��¼����������ʱ��������λ��
var windowX, windowY;
//��¼���������µ�ʱ���Ա��жϳ����ȶ���
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
            //�ƶ���ָʱ����������λ��
            window.setPosition(windowX + (event.getRawX() - x),
                windowY + (event.getRawY() - y));
            //������µ�ʱ�䳬��1.5���ж�Ϊ�������˳��ű�
            if (new Date().getTime() - downTime > 1500) {
                toast("���������ƶ�λ��Ŷ��");
            }
            return true;
        case event.ACTION_UP:
            //��ָ����ʱ���ƫ�ƺ�С���ж�Ϊ���
            if (Math.abs(event.getRawY() - y) < 5 && Math.abs(event.getRawX() - x) < 5) {
                onClick();
            }
            return true;
    }
    return true;
});

function onClick() {
    dialogs.alert("��ֹͣ���нű���");
    log("�û������ֹͣ��ť");
    exit();
}

function Justback() {
    //??????????ʹ���û��趨�ķ��ط���
    if (context_i_back == 0) {
        sleep(1000);
        toastLog("ʹ����ͨ�ķ���");
        back();
        sleep(2000);
    }
    if (context_i_back == 1) {
        sleep(1000);
        toastLog("ʹ��ROOT����\n��ȷ���Ѹ�ROOTȨ�ޣ�");
        Back();
        sleep(2000);
    }
    if (context_i_back == 2) {
        openInTask();
    }
    if (context_i_back == 3) {
        sleep(1000);
        toastLog("����Ļ�м���������ڻ���������");
        gestures([context_gestures_speed, [0, height / 2],
            [500, height / 2]
        ]);
        sleep(2000);
    }
    if (context_i_back == 5) {
        sleep(1000);
        toastLog("����Ļ����·����ϻ���������");
        gestures([context_gestures_speed, [width / 2 - 300, height - 1],
            [width / 2 - 300, height - 500]
        ]);
        sleep(2000);
    }
    if (context_i_back == 4) {
        sleep(1000);
        toastLog("����Ļ�м���������ڻ���������");
        gestures([context_gestures_speed, [width - 1, height / 2],
            [width - 500, height / 2]
        ]);
        sleep(2000);
    }
    if (context_i_back == 6) {
        sleep(1000);
        toastLog("����Ļ������������滬��������");
        gestures([context_gestures_speed, [width / 2 + 300, height - 1],
            [width / 2 + 300, height - 500]
        ]);
        sleep(2000);
    }
}

if (T == 1) {
    log("ʹ�á�������־��");

    function toastLog(message) {
        log(message);
        var myDate = new Date();
        ui.run(() => {
            w.WZ.setText(myDate.getHours() + "ʱ" + myDate.getMinutes() + "��" + myDate.getSeconds() + "�룺" + message + "\n" + w.WZ.getText());
            return true;
        });
    }
    var w = floaty.rawWindow(
        <card bg="#80000000">
            <vertical align="center">
                <img src="{{getStorageData('APPbasic', 'URLprefix')}}/OrangeJs-logoWhite.png" h="30" margin="0 10 0 5"/>//��ɫlogo
                <text text="�� ��ǰ�ű�������־ ��" textSize="15" color="#FFFFFF" textStyle="bold" gravity="center" margin="0 0 0 5"/>
                <text id="WZ" text="" textSize="15" color="#FFFFFF" marginLeft="10" gravity="left"/>
            </vertical>
        </card>
    );
    w.setSize(device.width, 500);
    w.setTouchable(false);
    w.setPosition(0, device.height - 500);
} else if (T == 0) {
    log("ʹ�ýű��Դ�����˾��");
}


function openInTask() {
    while (true) {
        if (className("android.view.View").desc("�ҵ�").findOnce() != null && text("�ֶ��ö�").className("android.widget.TextView").findOnce() != null && text("�Ϸ����򾩶�").className("android.widget.TextView").findOnce() != null) {
            if (text("�ֶ��ö�").className("android.widget.TextView").findOnce().parent().clickable() == true) {
                text("�ֶ��ö�").className("android.widget.TextView").findOnce().parent().click();
                toastLog("�ѳ���ä�㡰�ֶ��ö�����ڰ�ť");
                sleep(3000);
            } else {
                let a = text("�ֶ��ö�").className("android.widget.TextView").findOnce().parent().bounds();
                click(a.centerX(), a.centerY());
                toastLog("�ѳ��Ե�����ֶ��ö�����ڰ�ť");
                sleep(3000);
            }
            break;
        } else if (className("android.view.View").desc("�ҵ�").findOnce() != null) {
            className("android.view.View").desc("�ҵ�").findOnce().click();
            toastLog("�ѳ��Ե��������ҳ���ҵġ���ť");
            sleep(2000);
        } else if (currentPackage() != "com.jingdong.app.mall") {
            app.startActivity({
                action: "android.intent.action.VIEW", //�˴���Ϊ����ֵ
                packageName: "com.jingdong.app.mall",
                className: "com.jingdong.app.mall.main.MainActivity"
                //�˴����Լ����������ݣ���data��extras
            });
            toastLog("��ǰδ���ھ���APP�У��������´򿪾�������");
            console.warn("��ǰ���" + currentActivity() + "����ǰ������" + currentPackage() + "��ǰӦ������" + getAppName(currentPackage()));
            sleep(2000);
        } else {
            if (className("android.widget.ImageView").desc("����").clickable(true).findOnce() != null) {
                className("android.widget.ImageView").desc("����").clickable(true).findOnce().click();
                toastLog("�ѳ��Ե�������ء���ť");
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
            toastLog("���ڵȴ����ֶ��ö����������أ�ʣ��" + d + "�롭��");
            sleep(2000);
        }
    }
    if (MakeSureInHD() == false) {
        openInTask();
    }
}

function MakeSureInHD() {
    if (className("android.widget.TextView").text("��ȡӪ��Һ").findOnce() != null) {
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
            toastLog("�ѳ���ä�㡰�ն��ɰ桱��ť");
        } else {
            let b = a.bounds();
            click(b.centerX(), b.centerY());
            toastLog("�ѳ��Ե�����ն��ɰ桱��ť");
        }
        sleep(3000);
        if (className("android.widget.TextView").text("�������Ķ����ɳ�ֵΪ").findOnce() != null && className("android.widget.TextView").text("�������Ķ����ɳ�ֵΪ").findOnce().parent().childCount() == 4 &&
            className("android.widget.TextView").text("�������Ķ����ɳ�ֵΪ").findOnce().parent().child(0).className() == "android.widget.TextView" && className("android.widget.TextView").text("�������Ķ����ɳ�ֵΪ").findOnce().parent().child(1).className() == "android.widget.TextView" && className("android.widget.TextView").text("�������Ķ����ɳ�ֵΪ").findOnce().parent().child(2).className() == "android.widget.TextView" && className("android.widget.TextView").text("�������Ķ����ɳ�ֵΪ").findOnce().parent().child(3).className() == "android.widget.TextView") {
            toastLog(className("android.widget.TextView").text("�������Ķ����ɳ�ֵΪ").findOnce().parent().child(0).text() + className("android.widget.TextView").text("�������Ķ����ɳ�ֵΪ").findOnce().parent().child(1).text() + className("android.widget.TextView").text("�������Ķ����ɳ�ֵΪ").findOnce().parent().child(2).text() + className("android.widget.TextView").text("�������Ķ����ɳ�ֵΪ").findOnce().parent().child(3).text())
        }
        if (className("android.widget.TextView").text("���¾���").findOnce() != null) {
            let b = className("android.widget.TextView").text("���¾���").findOnce().bounds();
            click(b.centerX(), b.centerY());
            sleep(3000);
        }
    }

    let ShouQu = ["���Ѱ���", "���᳡", "�����ȡ", "Ӫ��Һ", "ÿ��ǩ��", "618�", "�������", "��ѡ��Ʒ", "����˫ǩ", "������Ʒ", "��ȡ����"];
    for (let a = 0; a < ShouQu.length; a++) {
        while (className("android.widget.TextView").text(ShouQu[a]).findOnce() != null && className("android.widget.TextView").text(ShouQu[a]).findOnce().parent().child(0).childCount() > 2 && className("android.widget.TextView").text(ShouQu[a]).findOnce().parent().child(0).child(2).className() == "android.widget.TextView") {
            let b = className("android.widget.TextView").text(ShouQu[a]).findOnce().parent().child(0).child(2);
            click(b.bounds().centerX(), b.bounds().centerY());
            toastLog("�ѳ��Ե����" + ShouQu[a] + b.text() + "��");
            sleep(2000);
        }
    }

    if (className("android.widget.ScrollView").findOnce() != null && className("android.widget.ScrollView").findOnce().childCount() > 0 && className("android.widget.ScrollView").findOnce().child(0).childCount() > 2) {
        let a = className("android.widget.ScrollView").findOnce().child(0).child(className("android.widget.ScrollView").findOnce().child(0).childCount() - 2).bounds();
        click(a.centerX(), a.centerY());
        toastLog("�ѳ��Ե����ȫ�����񡱰�ť");
        sleep(2000);
    } else if (className("android.widget.TextView").text("��ȡӪ��Һ").findOnce() != null && className("android.widget.TextView").text("��ȡӪ��Һ").findOnce().parent().className() == "android.view.ViewGroup" && className("android.widget.TextView").text("��ȡӪ��Һ").findOnce().parent().parent().childCount() > 14) {
        let a = className("android.widget.TextView").text("��ȡӪ��Һ").findOnce().parent().parent().child(13).bounds();
        click(a.centerX(), a.centerY());
        toastLog("�ѳ��Ե����ȫ�����񡱰�ť");
        sleep(2000);
    }


    var ax = 0;
    var DoNotDoPJRW = null;
    var DoNotDoGGHC = null;
    while (true) {
        if (className("android.widget.TextView").text("ȫ������").findOnce() != null && className("android.widget.TextView").text("ȫ������").findOnce().parent().child(className("android.widget.TextView").text("ȫ������").findOnce().parent().childCount() - 1).className() == "android.widget.ScrollView") {
            var A = className("android.widget.TextView").text("ȫ������").findOnce().parent().child(className("android.widget.TextView").text("ȫ������").findOnce().parent().childCount() - 1);
            var B = A.child(0);
        }
        toastLog("�����б�ɻ�������Ϊ��" + B.bounds().top + "," + B.bounds().bottom);
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
                console.warn("��ǰ���" + currentActivity() + "����ǰ������" + currentPackage() + "��ǰӦ������" + getAppName(currentPackage()));
                toastLog("��ǰδ���ڡ������б�����򷵻������������������½���:" + e);
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
                log("�޷�ȷ���������޼���ǰ�����������ϵ�����߽��", "������״̬����" + ZhuangTai);
                alert("�޷�ȷ���������޼���ǰ�����������ϵ�����߽��", "������״̬����" + ZhuangTai);
                exit();
            }
            toastLog("��ǰ������������" + now + "�Σ���ǰ��������Ϊ" + xz + "��");
            if (Button.bounds().centerY() > B.bounds().bottom - 10) {
                swipe(B.bounds().centerX(), B.bounds().centerY(), B.bounds().centerX(), B.bounds().centerY() - 500, 500);
                toastLog("�ѳ����ϻ���ǰ����ҳ������ǰ��ť��" + Button.text() + "�����ĵ�Y����Ϊ��" + Button.bounds().centerY());
                sleep(1000);
            } else if (Button.bounds().centerY() < B.bounds().top) {
                swipe(B.bounds().centerX(), B.bounds().centerY(), B.bounds().centerX(), B.bounds().centerY() + 500, 500);
                toastLog("�ѳ����»���ǰ����ҳ������ǰ��ť��" + Button.text() + "�����ĵ�Y����Ϊ��" + Button.bounds().centerY());
                sleep(1000);
            } else if (now != xz && RwTitle != "���᳡" && RwTitle != "������Ʒ" && RwTitle != "��������" || now != xz && RwTitle == "���᳡" && DoNotDoGGHC == null && now == 0 || now != xz && RwTitle == "������Ʒ" && DoNotDoPJRW == null) {
                if (Button.clickable() == true) {
                    Button.click();
                    toastLog("�ѳ���ä�㡰" + Button.text() + "����ť");
                } else {
                    let a = Button.bounds();
                    click(a.centerX(), a.centerY());
                    toastLog("�ѳ��Ե����" + Button.text() + "����ť");
                }
                sleep(3000);
                for (var JustWait = 10; JustWait > 0; JustWait--) {
                    if (className("android.widget.TextView").text("��������").findOnce() != null) { //�������
                        var limit = Number(xz);
                        var over = 0;
                        var ALL = className("android.widget.TextView").text("���겢��ע").find().size();
                        try {
                            var X = className("android.widget.ScrollView").findOnce().bounds();
                            log(X);
                        } catch (e) {
                            console.warn("��ǰ���" + currentActivity() + "����ǰ������" + currentPackage() + "��ǰӦ������" + getAppName(currentPackage()));
                            toastLog("δ�ɹ����롰���겢��ע���˵����棬���������С���");
                            openInTask();
                            DoTask();

                        }
                        toastLog("�������겢��ע����������" + ALL + "���ɵ�����򡿣�" + X.top, X.bottom);
                        for (var i = 0; i <= ALL; i++) {
                            while (true) {
                                log(over, limit);
                                if (over >= limit) {
                                    toastLog("�����겢��ע�����Ӫ��Һ�Ѵ�ÿ������" + limit + "�����ؼ���������һ����");
                                    if (className("android.widget.ImageView").desc("����").clickable(true).findOnce() != null) {
                                        className("android.widget.ImageView").desc("����").clickable(true).findOnce().click();
                                    } else {
                                        Justback();
                                    }
                                    sleep(3000);
                                    var i = ALL;
                                    var JustWait = 0;
                                    break;
                                } else if (i >= ALL) {
                                    toastLog("������ȫ��" + ALL + "�����̣������" + i + "�����̺��ҵ�" + over + "ƿӪ��Һ����δ�ﵽ����" + limit + "������")
                                    if (className("android.widget.ImageView").desc("����").clickable(true).findOnce() != null) {
                                        className("android.widget.ImageView").desc("����").clickable(true).findOnce().click();
                                    } else {
                                        Justback();
                                    }
                                    sleep(3000);
                                    var JustWait = 0;
                                    break;
                                } else {
                                    let a = className("android.widget.TextView").text("���겢��ע").findOnce(i);
                                    if (a == null) {
                                        toastLog("�Ҳ��������겢��ע����ť���������³����С���");
                                        openInTask();
                                        DoTask();
                                        var JustWait = 0;
                                        break;
                                    } else if (a.bounds().top != X.top && a.bounds().bottom != X.bottom) {
                                        toastLog("���ѵ������" + i + "�������겢��ע����ΧΪ��" + a.bounds().centerX(), a.bounds().centerY(), "�ϱ�Ե���±�Ե��ֱ�Ϊ��" + a.bounds().top, a.bounds().bottom);
                                        click(a.bounds().centerX(), a.bounds().centerY());
                                        sleep(3000);
                                        if (currentActivity() == "com.jd.lib.jshop.jshop.JshopMainShopActivity" || className("android.widget.EditText").findOnce() != null) {
                                            for (var z = 5; z > 0; z--) {
                                                if (className("android.view.View").text("Ӫ��Һ�߶��ˡ�").findOnce() != null) {
                                                    var z = 0;
                                                    if (className("android.view.View").text("Ӫ��Һ�߶��ˡ�").findOnce().parent().parent().childCount() == 3) {
                                                        var za = className("android.view.View").text("Ӫ��Һ�߶��ˡ�").findOnce().parent().parent().child(2).child(1);
                                                    } else if (className("android.view.View").text("Ӫ��Һ�߶��ˡ�").findOnce().parent().parent().childCount() == 2) {
                                                        var za = className("android.view.View").text("Ӫ��Һ�߶��ˡ�").findOnce().parent().parent().child(1).child(1);
                                                    }
                                                    if (za.clickable() == true) {
                                                        za.click();
                                                        toastLog("Ӫ��Һ�߶��ˡ���ä�㡰������Ӫ��Һ��");
                                                    } else {
                                                        let zb = za.bounds();
                                                        click(zb.centerX(), zb.centerY());
                                                        toastLog("Ӫ��Һ�߶��ˡ��ѵ����������Ӫ��Һ��" + zb.centerX(), zb.centerY() + "����");
                                                    }
                                                    sleep(3000);
                                                } else if (className("android.view.View").text("1��Ӫ��Һ").findOnce() != null || className("android.view.View").textContains("��Ӫ��Һ").findOnce() != null) {
                                                    var z = 0;
                                                    if (className("android.view.View").text("1��Ӫ��Һ").findOnce() != null && className("android.view.View").text("1��Ӫ��Һ").findOnce().parent().parent().childCount() == 3) {
                                                        var zat = className("android.view.View").text("1��Ӫ��Һ").findOnce();
                                                        var za = className("android.view.View").text("1��Ӫ��Һ").findOnce().parent().parent().child(2).child(1);
                                                    } else if (className("android.view.View").textContains("��Ӫ��Һ").findOnce() != null && className("android.view.View").textContains("��Ӫ��Һ").findOnce().parent().parent().childCount() == 3) {
                                                        var zat = className("android.view.View").textContains("��Ӫ��Һ").findOnce();
                                                        var za = className("android.view.View").textContains("��Ӫ��Һ").findOnce().parent().parent().child(2).child(1);
                                                    } else if (className("android.view.View").text("1��Ӫ��Һ").findOnce() != null && className("android.view.View").text("1��Ӫ��Һ").findOnce().parent().parent().childCount() == 2) {
                                                        var zat = className("android.view.View").text("1��Ӫ��Һ").findOnce();
                                                        var za = className("android.view.View").text("1��Ӫ��Һ").findOnce().parent().parent().child(1).child(1);
                                                    } else if (className("android.view.View").textContains("��Ӫ��Һ").findOnce() != null && className("android.view.View").textContains("��Ӫ��Һ").findOnce().parent().parent().childCount() == 2) {
                                                        var zat = className("android.view.View").textContains("��Ӫ��Һ").findOnce();
                                                        var za = className("android.view.View").textContains("��Ӫ��Һ").findOnce().parent().parent().child(1).child(1);
                                                    }
                                                    if (za.clickable() == true) {
                                                        za.click();
                                                        toastLog("���ҵ�" + zat.text() + "����ä�㡰������Ӫ��Һ��");
                                                    } else {
                                                        let zb = za.bounds();
                                                        click(zb.centerX(), zb.centerY());
                                                        toastLog("���ҵ�" + zat.text() + "���ѵ����������Ӫ��Һ��" + zb.centerX(), zb.centerY() + "����");
                                                    }
                                                    over++;
                                                    sleep(3000);
                                                } else {
                                                    toastLog("���������" + i + "�����̣�ʣ��" + z + "��󷵻ء���");
                                                    sleep(2500);
                                                }
                                            }
                                            if (currentActivity() == "com.jd.lib.jshop.jshop.JshopMainShopActivity" || className("android.widget.EditText").findOnce() != null) {
                                                toastLog("��Ȼ���ڵ��������ڳ��Է����ֶ��ö�����");
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
                    } else if (text("��עƵ������").id("fd").findOnce() != null) {
                        var limit = Number(xz);
                        var over = 0;
                        try {
                            var X = id("fd").findOnce().bounds();
                        } catch (e) {
                            console.warn("��ǰ���" + currentActivity() + "����ǰ������" + currentPackage() + "��ǰӦ������" + getAppName(currentPackage()));
                            toastLog("δ�ɹ����롰���벢��ע���˵����棬���������С���");
                            openInTask();
                            DoTask();

                        }
                        var ALL = className("android.view.View").text("���벢��ע").find().size();
                        toastLog("�������벢��ע����������" + ALL + "���ɵ�����򡿣�" + X.bottom, device.height);
                        for (var i = 0; i <= ALL; i++) {
                            while (true) {
                                if (over >= limit) {
                                    toastLog("�����벢��ע�����Ӫ��Һ�Ѵ�ÿ������" + limit + "�����ؼ���������һ����");
                                    if (className("android.widget.ImageView").desc("����").clickable(true).findOnce() != null) {
                                        className("android.widget.ImageView").desc("����").clickable(true).findOnce().click();
                                    } else {
                                        Justback();
                                    }
                                    sleep(3000);
                                    var i = ALL;
                                    var JustWait = 0;

                                    break;
                                } else if (i >= ALL) {
                                    toastLog("������ȫ��" + ALL + "�����̣������" + i + "�����̺��ҵ�" + over + "ƿӪ��Һ����δ�ﵽ����" + limit + "������")
                                    if (className("android.widget.ImageView").desc("����").clickable(true).findOnce() != null) {
                                        className("android.widget.ImageView").desc("����").clickable(true).findOnce().click();
                                    } else {
                                        Justback();
                                    }
                                    sleep(3000);
                                    var JustWait = 0;

                                    break;
                                } else {
                                    let a = className("android.view.View").text("���벢��ע").findOnce(i);
                                    if (a == null) {
                                        toastLog("�Ҳ��������벢��ע����ť���������³����С���");
                                        openInTask();
                                        DoTask();
                                        var JustWait = 0;

                                        break;
                                    } else if (a.clickable() == true) {
                                        a.click();
                                        toastLog("��ä���" + i + "�������벢��ע��");
                                        for (let deng = 3; deng > 0; deng--) {
                                            if (className("android.view.View").text("��ϲ���1ƿӪ��Һ").findOnce() != null) {
                                                toastLog("��ϲ���1ƿӪ��Һ");
                                                over++;
                                                break;
                                            } else if (className("android.view.View").text("Ӫ��Һ�߶��ˣ�����Ѱ�Ұ�~").findOnce() != null) {
                                                toastLog("Ӫ��Һ�߶��ˣ�����Ѱ�Ұ�~");
                                                break;
                                            } else {
                                                toastLog("���ڳ��Բ��ҡ������ʾ����ʣ��" + deng + "�롭��");
                                                sleep(1000);
                                            }
                                        }
                                        for (let a = 5; a > 0; a--) {
                                            toastLog("���ڵȴ�����أ�ʣ��" + a + "�롭��");
                                            sleep(1000);
                                        }
                                        if (id("com.jingdong.app.mall:id/fd").text("��עƵ������").findOnce() == null) {
                                            if (className("android.widget.ImageView").desc("����").clickable(true).findOnce() != null) {
                                                className("android.widget.ImageView").desc("����").clickable(true).findOnce().click();
                                                sleep(3000);
                                            } else {
                                                Justback();
                                                sleep(3000);
                                            }
                                        } else {
                                            toastLog("�����δ��ɻ��δ�ɹ����");
                                            sleep(2000);
                                        }
                                        break;
                                    } else if (a.bounds().top > X.bottom && a.bounds().bottom != device.height) {
                                        toastLog("���ѵ������" + i + "�������벢��ע����ΧΪ��" + a.bounds().centerX(), a.bounds().centerY(), "�ϱ�Ե���±�Ե��ֱ�Ϊ��" + a.bounds().top, a.bounds().bottom);
                                        click(a.bounds().centerX(), a.bounds().centerY());
                                        if (className("android.view.View").text("��ϲ���1ƿӪ��Һ").findOne(5000) != null) {
                                            toastLog("��ϲ���1ƿӪ��Һ");
                                            over++;
                                        }
                                        for (let a = 5; a > 0; a--) {
                                            toastLog("���ڵȴ�����أ�ʣ��" + a + "�롭��");
                                            sleep(2500);
                                        }
                                        if (id("com.jingdong.app.mall:id/fd").text("��עƵ������").findOnce() == null) {
                                            if (className("android.widget.ImageView").desc("����").clickable(true).findOnce() != null) {
                                                className("android.widget.ImageView").desc("����").clickable(true).findOnce().click();
                                                toastLog("�ѳ���ä�㷵�ذ�ť");
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
                    } else if (currentActivity() == "com.jingdong.common.jdreactFramework.activities.JDReactNativeCommonActivity" && className("android.widget.TextView").text("�쾩��").findOnce() != null) {
                        if (className("android.widget.TextView").text("ǩ���쾩��").findOnce() != null) {
                            let a = className("android.widget.TextView").text("ǩ���쾩��").findOnce().bounds();
                            click(a.centerX(), a.centerY());
                            toastLog("�ѳ��Ե����ǩ���쾩������ť");
                            for (let dengw = 10; dengw > 0; dengw--) {
                                if (className("android.widget.Image").text("rqgw7ZXmQDKLeno6UJDwD4AAObPazg9A5AddKkSX").findOnce() != null) {
                                    click(className("android.widget.Image").text("rqgw7ZXmQDKLeno6UJDwD4AAObPazg9A5AddKkSX").findOnce().bounds().centerX(), className("android.widget.Image").text("rqgw7ZXmQDKLeno6UJDwD4AAObPazg9A5AddKkSX").findOnce().bounds().centerY());
                                    toastLog("�ѳ��Ե�����鿴ǩ���ɹ�����ť");
                                    sleep(2000);
                                } else if (className("android.view.View").text("����ǩ���ɹ�����").findOnce() != null && className("android.view.View").text("����ǩ���ɹ�����").findOnce().parent().parent().parent().childCount() > 1 &&
                                    className("android.view.View").text("����ǩ���ɹ�����").findOnce().parent().parent().parent().child(1).childCount() > 0 && className("android.view.View").text("����ǩ���ɹ�����").findOnce().parent().parent().parent().child(1).child(0).childCount() > 0 &&
                                    className("android.view.View").text("����ǩ���ɹ�����").findOnce().parent().parent().parent().child(1).child(0).child(0).childCount() > 2 && className("android.view.View").text("����ǩ���ɹ�����").findOnce().parent().parent().parent().child(1).child(0).child(0).child(2).text() != "" && className("android.view.View").text("����ǩ���ɹ�����").findOnce().parent().parent().parent().child(1).child(0).child(0).child(2).text() != null) {
                                    toastLog("����ǩ���ɹ�������" + className("android.view.View").text("����ǩ���ɹ�����").findOnce().parent().parent().parent().child(1).child(0).child(0).child(2).text() + "������");
                                    sleep(2000);
                                    break;
                                } else if (className("android.widget.TextView").text("����ǩ���ɹ�����").findOnce() != null && className("android.widget.TextView").text("����ǩ���ɹ�����").findOnce().parent().parent().parent().childCount() > 1 &&
                                    className("android.widget.TextView").text("����ǩ���ɹ�����").findOnce().parent().parent().parent().child(1).childCount() > 0 && className("android.widget.TextView").text("����ǩ���ɹ�����").findOnce().parent().parent().parent().child(1).child(0).childCount() > 0 &&
                                    className("android.widget.TextView").text("����ǩ���ɹ�����").findOnce().parent().parent().parent().child(1).child(0).child(0).childCount() > 2 && className("android.widget.TextView").text("����ǩ���ɹ�����").findOnce().parent().parent().parent().child(1).child(0).child(0).child(2).text() != "" && className("android.widget.TextView").text("����ǩ���ɹ�����").findOnce().parent().parent().parent().child(1).child(0).child(0).child(2).text() != null) {
                                    toastLog("����ǩ���ɹ�������" + className("android.widget.TextView").text("����ǩ���ɹ�����").findOnce().parent().parent().parent().child(1).child(0).child(0).child(2).text() + "������");
                                    sleep(2000);
                                    break;
                                } else {
                                    toastLog("���ڵȴ���ǩ���ɹ���������أ�ʣ��" + dengw + "�롭��");
                                    sleep(1000);
                                }
                            }
                            for (let f = 2; f > 0; f--) {
                                if (className("android.view.ViewGroup").depth(1).findOnce() != null) {
                                    let ba = className("android.view.ViewGroup").depth(1).findOnce().bounds();
                                    click(ba.centerX(), ba.centerY());
                                    toastLog("�ѳ��Ե�������ذ�ť��");
                                    sleep(2000);
                                } else {
                                    Justback();
                                    sleep(2000);
                                }
                            }
                            var JustWait = 0;
                        } else if (className("android.widget.TextView").text("������ǩ��").findOnce() != null) {
                            let b = className("android.widget.TextView").text("������ǩ��").findOne().parent();
                            console.warn("����������־�����ͼ���ѿ����ߣ��˴����벻Ӧ�����е�Ŷ��");
                            if (b.childCount() != 3) {
                                toastLog("������ǩ�����������벻Ӧ�����еġ�");
                            } else {
                                toastLog(b.child(0).text() + b.child(1).text() + b.child(2).text());
                            }
                            if (className("android.view.ViewGroup").depth(1).findOnce() != null) {
                                let ba = className("android.view.ViewGroup").depth(1).findOnce().bounds();
                                click(ba.centerX(), ba.centerY());
                                toastLog("�ѳ��Ե�������ذ�ť��");
                                sleep(2000);
                            } else {
                                Justback();
                                sleep(2000);
                            }
                            var JustWait = 0;
                        } else {
                            console.warn("��ǰ���" + currentActivity() + "����ǰ������" + currentPackage() + "��ǰӦ������" + getAppName(currentPackage()));
                            toastLog("����δ�ҵ���ǩ���쾩������ť�����½��벢�����С���");
                            openInTask();
                            DoTask();
                            var JustWait = 0;
                        }
                    } else if (className("android.widget.TextView").text("�ѻ��").findOnce() != null) {
                        var limit = Number(xz);
                        var over = 0;
                        var i = 1;
                        while (true) {
                            let as = className("android.widget.TextView").text("x6").find();
                            for (var ii = 0; ii < className("android.widget.TextView").text("x6").find().length; ii++) {
                                if (as.get(ii) != null &&
                                    as.get(ii).parent().childCount() > 0 &&
                                    as.get(ii).parent().child(as.get(ii).parent().childCount() - 1).childCount() > 0 &&
                                    as.get(ii).parent().child(as.get(ii).parent().childCount() - 1).child(0).text() == "�����") {
                                    toastLog("�ѳɹ���ɡ���ѡ��Ʒ���������ڳ��Է���");
                                    if (className("android.widget.ImageView").desc("����").clickable(true).findOnce() != null) {
                                        className("android.widget.ImageView").desc("����").clickable(true).findOnce().click();
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
                                    let p = className("android.widget.TextView").text("�ѻ��").findOnce().parent().parent();
                                    let o = p.parent().child(p.parent().childCount() - 2);
                                    var C = o.child(0).child(0).child(2).child(0);
                                    let n = o.child(1).text();
                                    var Now = Number(n);
                                    let b = o.child(2).text();
                                    var ALL = b.replace("/", "");
                                } catch (e) {
                                    log(e);
                                    console.warn("��ǰ���" + currentActivity() + "����ǰ������" + currentPackage() + "��ǰӦ������" + getAppName(currentPackage()));
                                    toastLog("δ���ڽ��롰ѡta����ע���˵����棬���������С���");
                                    openInTask();
                                    DoTask();
                                    var JustWait = 0;
                                    break;
                                }
                                toastLog("��ǰΪ��" + Now + "����Ƭ����Ƭ����Ϊ" + ALL);
                                if (over >= limit) {
                                    toastLog("��ѡta����ע�����Ӫ��Һ�Ѵ�ÿ������" + limit + "�����ؼ���������һ����");
                                    if (className("android.widget.ImageView").desc("����").clickable(true).findOnce() != null) {
                                        className("android.widget.ImageView").desc("����").clickable(true).findOnce().click();
                                    } else {
                                        Justback();
                                    }
                                    sleep(3000);
                                    var JustWait = 0;
                                    break;
                                } else if (i >= ALL) {
                                    toastLog("������ȫ��" + ALL + "�����̣������" + i + "�����̺��ҵ�" + over + "ƿӪ��Һ����δ�ﵽ����" + limit + "������")
                                    if (className("android.widget.ImageView").desc("����").clickable(true).findOnce() != null) {
                                        className("android.widget.ImageView").desc("����").clickable(true).findOnce().click();
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
                                        toastLog("�ѳ��԰�˳�򻬶�����" + i + "����Ƭ");
                                        sleep(2000);
                                    } else {
                                        let a = C.child(C.childCount() - 1).bounds();
                                        click(a.centerX(), a.centerY());
                                        toastLog("�ѳ��Ե����ѡta����ע����ť");
                                        if (text("��ע�ɹ������1ƿӪ��Һ").findOne(5000) != null) {
                                            toastLog("��ע�ɹ������1ƿӪ��Һ");
                                            over++;
                                        }
                                        for (let deng = 3; deng > 0; deng--) {
                                            if (text("��ע�ɹ������1ƿӪ��Һ").findOnce() != null || desc("��ע�ɹ������1ƿӪ��Һ").findOnce() != null) {
                                                toastLog("��ע�ɹ������1ƿӪ��Һ");
                                                over++;
                                                break;
                                            } else if (text("Ӫ��Һ�߶��ˣ�����Ѱ�Ұ�~").findOnce() != null) {
                                                toastLog("Ӫ��Һ�߶��ˣ�����Ѱ�Ұ�~");
                                                break;
                                            } else {
                                                toastLog("���ڳ��Բ��ҡ������ʾ����ʣ��" + deng + "�롭��");
                                                sleep(1000);
                                            }
                                        }
                                        for (var loop = 5; loop > 0; loop--) {
                                            if (currentActivity() == "com.jd.lib.productdetail.ProductDetailActivity" || id("com.jd.lib.productdetail:id/akl").findOnce() != null) {
                                                var loop = 0;
                                                sleep(2000);
                                                if (className("android.widget.ImageView").desc("����").clickable(true).findOnce() != null) {
                                                    className("android.widget.ImageView").desc("����").clickable(true).findOnce().click();
                                                    toastLog("��ä�㷵��");
                                                    sleep(3000);
                                                } else {
                                                    Justback();
                                                    sleep(3000);
                                                }
                                            } else {
                                                toastLog("���ڵȴ���Ʒҳ���أ�ʣ��" + loop + "�롭��");
                                                sleep(2000);
                                            }
                                        }
                                        i++;
                                    }
                                }
                            }
                        }
                    } else if (id("com.jingdong.app.mall:id/fd").text("��������").findOnce() != null && text("û�д����۵���ƷŶ~").findOnce() != null) {
                        var DoNotDoPJRW = 1;
                        toastLog("������Ʒ���������κ���Ʒ������");
                        if (className("android.widget.ImageView").desc("����").clickable(true).findOnce() != null) {
                            className("android.widget.ImageView").desc("����").clickable(true).findOnce().click();
                        } else {
                            Justback();
                        }
                        sleep(3000);
                        var JustWait = 0;
                    } else if (id("com.jingdong.app.mall:id/fd").text("��������").findOnce() != null) {
                        for (let i = 1; i > 0; i--) {
                            if (id("com.jd.lib.evaluatecenter:id/abm").className("android.widget.TextView").clickable(true).text("����").findOnce() != null) {
                                id("com.jd.lib.evaluatecenter:id/abm").className("android.widget.TextView").clickable(true).text("����").findOnce().click();
                                toastLog("�ѳ��Ե����" + i + "�����۰�ť");
                                sleep(3000);
                                if (id("com.jd.lib.evaluatecenter:id/akh").text("��������").findOnce() != null && id("com.jd.lib.evaluatecenter:id/akh").text("��������").findOnce().checked() == false) {
                                    id("com.jd.lib.evaluatecenter:id/akh").text("��������").findOnce().click();
                                    toastLog("�ѳ��Ե�����������ۡ���ť");
                                    sleep(3000);
                                }
                                if (id("com.jingdong.app.mall:id/a9b").className("android.widget.TextView").text("�ύ").clickable(true).findOnce() != null) {
                                    id("com.jingdong.app.mall:id/a9b").className("android.widget.TextView").text("�ύ").clickable(true).findOnce().click();
                                    toastLog("�ѳ��Ե�����ύ���ۡ���ť");
                                    sleep(3000);
                                    for (let a = 2; a > 0; a--) {
                                        if (desc("����").clickable(true).findOnce() != null) {
                                            desc("����").clickable(true).findOnce().click();
                                            toastLog("�ѳ���ä�㡰���ذ�ť��");
                                            sleep(2000);
                                        } else {
                                            Justback();
                                            sleep(1000);
                                        }
                                    }
                                }
                            } else {
                                toastLog("��ǰ�����κο�������Ʒ");
                                if (desc("����").clickable(true).findOnce() != null) {
                                    desc("����").clickable(true).findOnce().click();
                                    toastLog("�ѳ���ä�㡰���ذ�ť��");
                                    sleep(2000);
                                } else {
                                    Justback();
                                    sleep(1000);
                                }
                            }
                        }
                        var DoNotDoPJRW = 1;
                        toastLog("������Ʒ���������");
                        var JustWait = 0;
                    } else {
                        toastLog("���ڵȴ����������أ�ʣ��" + JustWait + "�롭��");
                        sleep(1000);
                    }
                }
                if (RwTitle == "���᳡") {
                    var DoNotDoGGHC = 1;
                }
                if (MakeSureInHD() == false) {
                    toastLog("���Է��ء������б�����");
                    if (className("android.widget.ImageView").desc("����").clickable(true).findOnce() != null) {
                        className("android.widget.ImageView").desc("����").clickable(true).findOnce().click();
                    } else {
                        Justback();
                    }
                    sleep(3000);
                }
            } else {
                if (now == xz) {
                    toastLog("����������ɡ�" + RwTitle + "(" + ZhuangTai + ")");
                } else {
                    toastLog("����������" + RwTitle + "(" + ZhuangTai + ")");
                }
                ax++;
            }
        }
    }
    alert("���ֶ��ö��Զ��ű�����\n���������");
    exit();
}
firstD();

function firstD() {
    if (context_Manualstate == 1) {
        toastLog("���ֶ�ģʽ���нű�");
        var options = ["�ȴ�20��", "�ȴ�30��", "�ȴ�50��", "�ȴ�60��", "�ȴ�10��"]
        var i = dialogs.select("??�ԡ��ֶ�ģʽ�����нű�\n\n����������Ҫ����ʾ���ֺ����д򿪾���APP���ҳ��\n\n��ѡ��ű��ȴ����򿪾�����ʱ��", options);
        if (i >= 0) {
            toast("��ѡ�����" + options[i]);
        } else if (i < 0) {
            toastLog("��ȡ����ѡ��");
            dialogs_js();
            firstD();
        }
        if (i == 0) {
            //�ȴ�20��
            var deng = 20;
        } else if (i == 1) {
            //�ȴ�30��
            var deng = 30;
        } else if (i == 2) {
            //�ȴ�50��
            var deng = 50;
        } else if (i == 3) {
            //�ȴ�60��
            var deng = 60;
        } else if (i == 4) {
            //�ȴ�10��
            var deng = 10;
        }
        for (deng = deng; deng > 0; deng--) {
            toastLog("��򿪾������ֶ��ö���������\nʣ��" + deng + "������нű�...");
            sleep(1111);
        }
        DoTask();
    } else {
        openInTask();
        DoTask();
    }
}