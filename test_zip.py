from modules import create_zip, extract_zip_to, read_xlsx, read_pdf, read_csv, archive_path

create_zip(archive_path)


def test_zip():
    extract_zip_to('tmp')

    xlsx_file = read_xlsx('tmp/file_example_XLSX_50.xlsx')
    pdf_file = read_pdf('tmp/selene-readthedocs-io-en-latest.pdf')
    csv_file = read_csv('tmp/username.csv')

    assert 'Dulce' in xlsx_file
    assert 'yashaka' in pdf_file
    assert '48' in csv_file
