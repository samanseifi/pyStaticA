import os

from pylatex import *
from pylatex.utils import bold, NoEscape


def generate_unique():
    geometry_options = {
        "head": "40pt",
        "margin": "0.5in",
        "bottom": "0.6in",
        "includeheadfoot": True
    }
    doc = Document(geometry_options=geometry_options)

    # Generating first page style
    first_page = PageStyle("firstpage")

    # Header image
    with first_page.create(Head("L")) as header_left:
        with header_left.create(MiniPage(width=NoEscape(r"0.49\textwidth"),
                                         pos='c', align='l')) as title_wrapper:
            title_wrapper.append(LargeText(bold("CM&S Simulation Results Report")))
            title_wrapper.append(LineBreak())
            title_wrapper.append(SmallText(bold("by pyStaticA v 1.0")))

    # Add document title
    with first_page.create(Head("R")) as right_header:
        with right_header.create(MiniPage(width=NoEscape(r"0.49\textwidth"),
                                          pos='c', align='r')) as logo_wrapper:
            logo_file = os.path.join(os.path.dirname(__file__),
                                     'logo/depuy.png')
            logo_wrapper.append(StandAloneGraphic(image_options="width=100px",
                                                  filename=logo_file))


    with doc.create(Section('Analysis Information')):
        with doc.create(Tabular('|l|l|l|l|')) as table1:
            table1.add_hline()
            table1.add_row(('Operator:', MultiColumn(3, align='|l|', data='Saman Seifi'),))
            table1.add_hline()
            table1.add_row(('Test Description:', MultiColumn(3, align='|l|', data='Torque to Failure'),))
            table1.add_hline()
            table1.add_row(('Part Description:', MultiColumn(3, align='|l|', data='Cornerstone Polyaxial Screw Build 1'),))
            table1.add_hline()
            table1.add_row(('Test Date:', MultiColumn(3, align='|l|', data='24 Dec, 2020'),))
            table1.add_hline()
            table1.add_row(('CMR:', MultiColumn(3, align='|l|', data='n/a'),))
            table1.add_hline()

            row_cells = ('Test Mode:', 'Compression', 'Total #:', '5')
            table1.add_row(row_cells)
            table1.add_hline()

    with doc.create(Section('Table of results')):
        with doc.create(Tabular('|l|l|l|l|')) as table2:
            table2.add_hline()
            table2.add_row(('Line Fit', 'start', 'end', 'R^2',))
            table2.add_hline()
            for i in range(0, 4):
                table2.add_row(('Sample1', '0.1', '0.2', '0.999'))
                table2.add_hline()

        doc.append(LineBreak())
        doc.append(LineBreak())


        with doc.create(Tabular('|l|l|l|l|')) as table2:
            table2.add_hline()
            table2.add_row(('Results', 'Force(N)', 'Max Force (N)', 'Stiffness (N/mm)',))
            table2.add_hline()
            for i in range(0, 4):
                table2.add_row(('Sample1', '45', '45', '123'))
                table2.add_hline()

    doc.preamble.append(first_page)
    # End first page style

    doc.change_document_style("firstpage")
    doc.add_color(name="lightgray", model="gray", description="0.80")

    doc.append(NewPage())

    # Add cheque images
    with doc.create(LongTabu("X[c] X[c]")) as cheque_table:
        cheque_file = os.path.join(os.path.dirname(__file__),
                                   'plot0.png')
        cheque = StandAloneGraphic(cheque_file, image_options="width=200px")
        for i in range(0, 5):
            cheque_table.add_row([cheque, cheque])

    doc.generate_pdf("testing_report", clean_tex=False)


generate_unique()
