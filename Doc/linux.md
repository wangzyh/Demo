# Linux
1. Linux中进程的状态: 
    - 不可中断状态: 睡眠状态,但是此刻进程是不可中断的
    - 暂停/中断状态
    - 就绪状态
    - 运行状态
    - 可中断睡眠状态
    - 僵尸
    - 退出状态
2. 后台运行: &, 后台任务: job -l
3. 当按下Ctrl-c时发生了什么
    1. 终端产生 SIGINT 信号
    2. 前台进程组中的所有进程都会接收到 SIGINT 信号然后退出(默认动作)
    3. shell通过调用 waitpid 清理进程表中子进程信息
4. 多路复用: I/O复用就是多个进程共同使用一个I/O输入输出流
  