import time
from rich.progress import Progress
from rich.console import Console
from rich.panel import Panel
from rich.align import Align

console = Console()

def neuro_priming():
    """心流启动神经 priming"""
    console.print(Panel.fit("🧠 [bold cyan]神经启动协议激活[/]", border_style="blue"))
    for i in range(10, 0, -1):
        console.print(f"[bright_black]深度专注倒计时: {i}秒[/]", end="\r")
        time.sleep(1)
    console.print("\n✅ [bold green]前额叶皮层准备就绪[/]\n")

def flow_timer(total_mins=50, chunk_mins=15):
    """动态心流进度可视化"""
    with Progress() as progress:
        task = progress.add_task("[cyan]心流进程", total=total_mins)
        
        while not progress.finished:
            # 进度条动态刷新
            for min_passed in range(total_mins):
                progress.update(task, advance=1)
                
                # 每15分钟难度微调提示
                if min_passed > 0 and min_passed % chunk_mins == 0:
                    console.print(
                        Panel.fit(
                            f"[yellow]❗ 第{min_passed}分钟检查点[/]\n"
                            f"1. 当前专注度评分（1-10）: [bold]{input('你的评分: ') or '7'}[/]\n"
                            f"2. 是否需要[red]降低[/]/[green]提高[/]难度?",
                            title="认知负荷调节"
                        )
                    )
                
                # 神经锚点提示
                if min_passed == 8:
                    console.print(Align.center("[blue]🎯 乙酰胆碱分泌峰值期[/]"))
                elif min_passed == 25:
                    console.print(Align.center("[purple]⚡ 多巴胺协同效应触发[/]"))
                
                time.sleep(60)  # 真实分钟计时

            # 完成后的脑科学提示
            console.print(
                Panel.fit(
                    "[bold green]💡 立即执行:[/]\n"
                    "1. 用非惯用手写3个关键词（右脑激活）\n"
                    "2. 冷水洗脸（刺激蓝斑核）\n"
                    "3. 站立拉伸（增加脑脊液流动）",
                    title="心流固化程序"
                )
            )

if __name__ == "__main__":
    neuro_priming()
    flow_timer(total_mins=50, chunk_mins=15)
  
