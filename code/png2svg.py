from PIL import Image
import cairosvg

# 打开彩色 SVG 图像
color_svg_path = "/Users/lilianli/Documents/GitHub/Font-Awesome/svgs/brands/xiaohongshu.svg"
bw_svg_path = "bw_image.svg"

# 将彩色 SVG 转换为黑白 PNG
cairosvg.svg2png(url=color_svg_path, write_to=bw_svg_path, output_width=500, output_height=500)

# 打开黑白 PNG 图像
bw_image = Image.open(bw_svg_path)

# 将黑白 PNG 图像转换为黑白模式
bw_image = bw_image.convert("L")

# 保存黑白 PNG 图像
bw_image.save("bw_image.png")
