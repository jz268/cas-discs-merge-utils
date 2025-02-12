from pypdf import PdfWriter
from pathlib import Path
from tqdm import tqdm

# def find_pdfs_assignments(oc):
#     base_dir = Path(__file__).parent.resolve() / oc / 'assignments'
#     pdfs = []
#     for i in range(1, 100):
#         for j in range(1, 100):
#             path = base_dir / f'disc_{oc}_{i}.{j}.pdf'
#             if path.is_file():
#                 pdfs.append(str(path))
#             else:
#                 break
#             for k in range(1, 100):
#                 path = base_dir / f'disc_{oc}_{i}.{j}_ex{k}.pdf'
#                 if path.is_file():
#                     pdfs.append(str(path))
#                 else:
#                     break
#     return pdfs


def find_pdfs_outlines(oc):
    base_dir = Path(__file__).parent.resolve() / oc / 'outlines'

    if oc == 'ia':
        spec = f'2_5e_DISC_{oc.upper()}'
    elif oc == 'rm':
        spec = f'1_4e_DISC_{oc.upper()}'
    elif oc == 'da':
        spec = f'3_1e'
    else:
        raise ValueError
    
    fname_base = f'CAS_{spec}_'
    pdfs = []

    ctname = fname_base + 'CourseTopics.pdf'
    ctpath = base_dir / ctname
    if ctpath.is_file():
        pdfs.append(str(ctpath))

    if oc != 'da':
        wb_sfx = 'PM_WORKBOOK_A'
    else:
        wb_sfx = 'WORKBOOK_A'
    
    fnwb_base = fname_base + wb_sfx
    for i in range(1, 100):
        fname = fnwb_base + f'{i:02d}.pdf'
        path = base_dir / fname
        if path.is_file():
            pdfs.append(path)
        else:
            break
    return pdfs


def find_pdfs_extras(oc):
    base_dir = Path(__file__).parent.resolve() / oc / 'extras'
    p = base_dir.glob('**/*.pdf')
    pdfs = [str(x) for x in p if x.is_file()]
    return pdfs


def merge_pdfs(pdfs, oc, type):

    base_dir = Path(__file__).parent.resolve() / oc / 'merged'
    base_dir.mkdir(parents=True, exist_ok=True)

    merger = PdfWriter()

    for pdf in tqdm(pdfs):
        merger.append(pdf)

    merger.write(base_dir / f'{oc}_{type}.pdf')
    merger.close()


# def merge_all_groups(oc):
#     assignment_pdfs = find_pdfs_assignments(oc)
#     print(assignment_pdfs)
#     merge_pdfs(assignment_pdfs, oc, 'assignments')

#     merge_key_groups(oc)


def merge_key_groups(oc):

    outline_pdfs = find_pdfs_outlines(oc)
    print(outline_pdfs)
    merge_pdfs(outline_pdfs, oc, 'outlines')

    extra_pdfs = find_pdfs_extras(oc)
    print(extra_pdfs)
    merge_pdfs(extra_pdfs, oc, 'extras')


if __name__ == '__main__':

    for oc in ('ia', 'rm', 'da'):
        merge_key_groups(oc)