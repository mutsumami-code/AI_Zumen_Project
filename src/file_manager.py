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