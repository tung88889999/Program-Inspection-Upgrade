import fontforge

# 创建一个新的字体
font = fontforge.font()

# 设置字体名
font.fontname = "SimSun"
font.fullname = "SinSun"

# 添加一个字形 (e.g., 'A')
glyph = font.createChar(65, "A")
glyph.importOutlines("/storage/emulated/0/Download/fonts/outline.svg")

# 保存字体
font.generate("MinSun.ttf")
