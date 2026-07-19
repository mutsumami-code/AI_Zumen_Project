from pathlib import Path
import config
import fitz


def get_pdf_files():
    """
    pdfフォルダ内のPDFファイル一覧を取得する
    """

    pdf_path = Path(config.PDF_FOLDER)
    pdf_files = sorted(pdf_path.glob("*.pdf"))

    return pdf_files
 


def open_pdf(pdf_path):
    """
    PDFを開く
    """

    document = fitz.open(pdf_path)

    return document

def pdf_to_image(document, output_path):
    """
    PDFの1ページ目をPNG画像として保存する
    """

    page = document.load_page(0)

    pix = page.get_pixmap(dpi=300)

    pix.save(output_path)