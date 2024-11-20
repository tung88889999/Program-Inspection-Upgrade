import subprocess

def check_epub(epub_file_path, epubcheck_path):
    try:
        # 构建命令
        command = ['java', '-jar', epubcheck_path, epub_file_path]
        
        # 运行命令并捕获输出
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # 输出结果
        if result.returncode == 0:
            print(f"EPUB 文件 {epub_file_path} 验证成功，无错误。")
        else:
            print(f"EPUB 文件 {epub_file_path} 验证失败，发现错误：")
            print(result.stdout)
            print(result.stderr)
    except Exception as e:
        print(f"运行 epubcheck 时出错: {e}")

# 示例使用
epub_file_path = "./小说家/77.epub"  # 替换为你的 EPUB 文件路径
epubcheck_path = "./小说家/epubcheck.jar"  # 替换为 epubcheck.jar 的路径

check_epub(epub_file_path, epubcheck_path)
