fork 是类Unix操作系统上创建进程的主要方法，fork用于创建子进程

exec 装载一个新的程序覆盖当前进程空间中的映像，从而执行不同的任务
exec 系列函数在执行时会直接替换掉当前进程的地址空间。  


Copy On Write 写时复制

fork之后，kernel把副进程中所有的内存页的权限都设置为read-only，然后子进程的地址空间指向父进程。当父子进程都制度内存时，相安五十，当某个进程写内存是，CPU硬件检测内存页是read-only的，于是触发页异常中断page-fault，陷入kernel的一个中断例程。中断例程中，kernel就会把触发的额异常的页复制一份，于是父子进程各自持有独立的一份

好处
- 减少分配和复制大量资源时带来的瞬时延迟
- 减少不必要的资源分配

- fork之后父子进程都还需要继续进程写操作，那么会产生大量的分页错误