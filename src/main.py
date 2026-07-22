
import config
import file_manager

"""
AI_Zumen_Project
Main Program

板金加工業向けAI図面解析システム
"""

def main():

    print("===================================")
    print(f" {config.PROJECT_NAME}")
    print(f" Version {config.VERSION}")
    print(" 板金加工業向けAI図面解析システム")
    print("===================================")
    print("システム起動")
    print("準備完了")
    print()
    print("PDFファイル一覧")

    pdf_files = file_manager.get_pdf_files()

    for pdf in pdf_files:


        document = file_manager.open_pdf(pdf)

        width, height = file_manager.get_page_size(document)

        output_image = f"output/{pdf.stem}.png"
        
        file_manager.pdf_to_image(document, output_image)

        image_width, image_height = file_manager.get_image_size(output_image)

        print(pdf.name)
        print(f"ページ数：{document.page_count}")
        print(f"ページサイズ：{width:.1f} × {height:.1f} pt")
        print(f"画像サイズ：{image_width} × {image_height} pixel")
        print(f"画像保存：{output_image}")
        
        document.close()
if __name__ == "__main__":
    main()