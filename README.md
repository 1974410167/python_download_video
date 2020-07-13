# python无水印下载皮皮虾，抖音

> 皮皮虾无水印下载基本思路是后台返回来的数据直接就有无水印链接，直接下载即可。            
> 抖音下载思路是把"User-Agent"修改为手机端，抖音给手机端返回无水印链接，给PC端返回有水印，下载无水印即可。


1. 新建一个.txt文件
2. 每一行分别放一个url
3. 在read_url()函数中修改你的.txt文件地址
4. 在download_path()函数中修改你要下载的地址
5. 运行


# python下载youtube

> 直接调用youtube-dl接口,分别下载en,zh-Hans字幕

1. 如上，修改read_url(),download_path()为你的地址
2. 调用ThreadPoolExecutor接口，多线程下载
3. 运行
4. 记得把梯子改为全局模式
