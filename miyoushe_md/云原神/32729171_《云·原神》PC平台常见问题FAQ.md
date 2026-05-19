---
title: 《云·原神》PC平台常见问题FAQ
category: 云原神
post_id: 32729171
created_at: 2022-12-12 11:00:05
reply_count: 671
---
![image](https://upload-bbs.miyoushe.com/upload/2022/12/09/75276557/d0b2874fca2c58f8d4d465dd69f449f7_68269886597099468.png)亲爱的旅行者： 
《云·原神》PC平台限号不删档付费测试开启以来，项目组收到许多关于PC平台下载、启动、运行等方面的反馈。我们对大家的提问做了整理和汇总，想在此为大家一一进行解答。

**▌****机型适配**
**PC最低配置**
操作系统：Windows 7 SP1 64-bit | Windows 8.1 64-bit | Windows 10 64-bit
处理器：Intel Core i3 或同等处理器
内存：4 GB RAM
显卡：NVIDIA GeForce GTX 750
DirectX 版本: 9
*需要 64 位处理器和操作系统


**▌PC平台安装与启动相关问题**
**Q1：为什么在内存空间足够的情况下，提示无法安装？**
A1：①请确认当前设备的系统是否使用ramdisk内存分配了虚拟硬盘，且系统临时文件目录在虚拟硬盘中。如果是虚拟硬盘，请将系统临时文件目录暂时修改至真实的硬盘分区中。
        ②如问题仍未得到解决，请联系客服进行反馈。

**Q2：安装客户端后无法启动，并出现报错“应用程序无法正常启动(0xc000007b或0xc0000102)”的情况应该怎么办？**
A2：请尝试安装vc运行库。旅行者可以通过《云·原神》安装目录中的“vc_redist.x64.exe”进行安装，或从微软官网下载安装最新的VC_redist.x64.exe：[https://support.microsoft.com/zh-cn/help/2977003/the-latest-supported-visual-c-downloads](https://support.microsoft.com/zh-cn/help/2977003/the-latest-supported-visual-c-downloads)

**Q3：双击云原神.exe后，出现了直接闪退的情况应该怎么办？**
A3：①请检查更新驱动，并根据当前设备的显卡品牌前往下列网站更新对应驱动（在电脑搜索框内输入【设备管理器】-打开【显示适配器】即可查看）：
* intel: https://www.intel.cn/content/www/cn/zh/support/articles/000005629/graphics.html
* AMD:  https://www.amd.com/zh-hans/support 
* NVIDIA: https://www.nvidia.cn/Download/index.aspx?lang=cn2
       ②如更新驱动后仍然启动失败，请运行directx修复工具，下载地址为：[https://www.microsoft.com/en-us/Download/confirmation.aspx?id=35](https://www.microsoft.com/en-us/Download/confirmation.aspx?id=35)
       ③如问题仍未得到解决，请联系客服进行反馈。
PS：目前目前暂时不支持虚拟机，以及AMD的ATI显卡。

**Q4：启动PC平台时，出现未响应、卡死和崩溃等问题应该怎么办？**
A4：①请尝试更换一个更稳定、高速的网络环境重新连接。
        ②请尝试寻找出现问题时的dump文件，并携带文件（如有）联系客服进行反馈。
* dump文件获取路径：
云·原神目录(%USERPROFILE%\AppData\Local\GenshinImpactCloudGame\CrashDumps)或系统dump目录（%USERPROFILE%\AppData\Local\CrashDumps）
          旅行者可以直接将以上路径复制粘贴到文件资源管理器的地址栏中，按下回车键即可跳转到对应目录。
![image](https://upload-bbs.miyoushe.com/upload/2022/12/09/75276557/f3c8632c7ffd0ab9d250392fd7e39fb5_1848795063851576730.png)

**▌****游戏启动相关问题**
**Q5：在PC平台点击开始游戏时，出现“错误码：-1025”的报错码应该怎么办？**
A5：①请检查更新驱动，并根据当前设备的显卡品牌前往下列网站更新对应驱动（在电脑搜索框内输入【设备管理器】-打开【显示适配器】即可查看）：
* intel: https://www.intel.cn/content/www/cn/zh/support/articles/000005629/graphics.html
* AMD:  https://www.amd.com/zh-hans/support 
* NVIDIA: https://www.nvidia.cn/Download/index.aspx?lang=cn2
	   ②如更新驱动后仍然启动失败，请请运行directx修复工具，下载地址为：[https://www.microsoft.com/en-us/Download/confirmation.aspx?id=35](https://www.microsoft.com/en-us/Download/confirmation.aspx?id=35)
       ③如问题仍未得到解决，请联系客服进行反馈。
PS：目前目前暂时不支持虚拟机，以及AMD的ATI显卡。

**Q6：在PC平台点击开始游戏时，出现“错误码：-1026”的报错码应该怎么办？**
A6：①请检查是否有未安装驱动，或显卡被禁用的情况（在电脑搜索框内输入【设备管理器】-打开【显示适配器】即可查看）。
        ②请按照上述A5中的方式更新电脑驱动。如问题仍未得到解决，请联系客服进行反馈。

**Q7：在PC平台点击开始游戏时，出现“错误码：-1027”的报错码应该怎么办？**
A7：①请按照上述A6中的步骤检查是否有未安装驱动，或显卡被禁用的情况，并更新电脑驱动。
        ②若上述操作未能解决问题，请按住“Windows键 + R”，并输入“DxDiag.exe”，点击确定。随后点击系统-最下侧【保存所有信息】按键将相关信息存储为txt文件，并联系客服进行反馈。
![image](https://upload-bbs.miyoushe.com/upload/2022/12/09/75276557/0d853a05306b4e096e9bec333ff40248_3377341897794220477.png)
**Q8：启动游戏时，出现黑屏loading及”错误码：-1001“的报错码应该怎么办？**
A8：①请尝试更换一个更稳定、高速的网络环境重新连接。
        ②如问题仍未得到解决，请联系客服进行反馈。


**▌****游戏运行相关问题**
**Q9：为什么我的显示器支持超高分辨率，但游戏画面仍然有些模糊？**
A9：目前云游戏PC平台支持的最高画面传输分辨率为1920*1080，建议旅行者在此分辨率下进行游戏。

**Q10：启动游戏后，出现曝光过高、饱和度过低或黑白显示等非正常画面显示问题应该怎么办？**
A10：由于《云·原神》PC平台的显示依赖于视频传输，因此需要调试游戏内的视频颜色设置。请按照A5中的方法查看自己电脑设备的显卡型号：
①NVIDIA：点击鼠标右键-NVIDIA控制面板-调整视频颜色设置-通过NVIDIA设置调整。
![image](https://upload-bbs.miyoushe.com/upload/2022/12/09/75276557/b908fda587fb4839102aa27f7e683e03_547984483864601036.png)②intel：请安装”英特尔® Arc™ Graphics Windows* DCH 驱动程序“，在“intel显卡控制中心”软件中调整视频的色彩配置。
*下载地址：[https://www.intel.cn/content/www/cn/zh/support/intel-driver-support-assistant.html](https://www.intel.cn/content/www/cn/zh/support/intel-driver-support-assistant.html)
*下载”英特尔® Arc™ Graphics Windows* DCH 驱动程序“，安装完成后打开“intel驱动程序和支持助理”（如下图），通过视频标签页进行设置。
![image](https://upload-bbs.miyoushe.com/upload/2022/12/09/75276557/ead35f4d756d05e2bf21e79e844ef66a_3504960722609317152.png)③AMD：安装AMD显卡驱动后，打开AMD显卡驱动程序，在视频页签中进行设置。旅行者可直接选择【默认】，也可选择【自定义】自行调节视频亮度，如下图所示：
![image](https://upload-bbs.miyoushe.com/upload/2022/12/09/75276557/7850b27919abc5f5df035b29332ce279_91192144446790085.png)![image](https://upload-bbs.miyoushe.com/upload/2022/12/09/75276557/6a35d29273ce237355265e7ebf58da96_3431106179360367693.png)
**Q11：为什么启动游戏后，出现了如绿屏、曝光异常等非正常画面显示问题？**
A11：请按照上述A5中的方式更新电脑驱动。如问题仍未得到解决，请联系客服进行反馈。

**Q12：为什么在游戏过程中，画面上出现了明显锯齿？**
A12：①请尝试手动指定启动《云·原神》PC平台的显卡设备（在电脑搜索框内输入【设置】-【显示】-【图形设置】，添加《云·原神》的exe文件后即可进行设置）。推荐使用独显驱动，如切换独显后问题仍未得到解决，请尝试切换至集显。
![image](https://upload-bbs.miyoushe.com/upload/2022/12/09/75276557/b868019bb2df53d43a5bc84dae6184b6_6035973589497855858.png)![image](https://upload-bbs.miyoushe.com/upload/2022/12/09/75276557/14a88854049b0209ee4200cb46594d85_8249085706087945243.png)![image](https://upload-bbs.miyoushe.com/upload/2022/12/09/75276557/8c1a2d6539683ecc965cf2a42d9354e6_2491185710777507110.png)        ②请按照上述A5中的方式更新电脑驱动。
        ③如问题仍未得到解决，请向客服提供您的硬件信息进行反馈。
PS：切换显卡设备后需要重新启动《云·原神》PC平台。

**Q13：为什么启动游戏后可以听到声音，但显示黑屏没有画面？**
A13：①请尝试重启《云·原神》PC平台进行重试。
          ②请按照上述A5中的方式切换显卡及更新驱动。
          ③如问题仍未得到解决，请联系客服进行反馈。

