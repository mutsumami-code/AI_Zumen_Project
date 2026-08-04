
import config
import file_manager
import image_processor
import contour_processor

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

        image = file_manager.open_image(output_image)

        gray_image = image_processor.convert_to_gray(image)

        gray_output = f"output/{pdf.stem}_gray.png"

        image_processor.save_image(gray_image, gray_output)

        binary_image = image_processor.convert_to_binary(gray_image)

        binary_output = f"output/{pdf.stem}_binary.png"

        image_processor.save_image(binary_image, binary_output)

        contours = image_processor.detect_contours(binary_image)

        for i, contour in enumerate(contours[:10], start=1):

            area = contour_processor.get_contour_area(contour)

            print(f"輪郭{i}: 面積 = {area:.2f}")

    

        contour_image = image_processor.draw_contours(
            image,
            contours
        )

        contour_output = f"output/{pdf.stem}_contours.png"

        image_processor.save_image(
            contour_image,
            contour_output
        )

        image_width, image_height = file_manager.get_image_size(output_image)

        print(pdf.name)
        print(f"ページ数：{document.page_count}")
        print(f"ページサイズ：{width:.1f} × {height:.1f} pt")
        print(f"画像サイズ：{image_width} × {image_height} pixel")
        print(f"画像保存：{output_image}")
        print(f"画像配列サイズ：{image.shape}")
        print(f"グレースケール保存：{gray_output}")
        print(f"二値画像保存：{binary_output}")
        print(f"検出輪郭数：{len(contours)}")
        print(f"輪郭画像保存：{contour_output}")
        
        document.close()
if __name__ == "__main__":
    main()