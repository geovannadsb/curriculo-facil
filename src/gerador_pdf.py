from fpdf import FPDF


def gerar_pdf(curriculo, caminho_saida="curriculo.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_margins(20, 20, 20)

    dados = curriculo.dados_pessoais

    # Nome
    pdf.set_font("Helvetica", "B", 22)
    pdf.set_text_color(30, 30, 30)
    pdf.cell(0, 12, dados["nome"], ln=True, align="C")

    # Contato
    pdf.set_font("Helvetica", size=10)
    pdf.set_text_color(80, 80, 80)
    contato = f'{dados["email"]}  |  {dados["telefone"]}  |  {dados["cidade"]}'
    pdf.cell(0, 7, contato, ln=True, align="C")
    pdf.ln(4)

    # Linha divisória
    pdf.set_draw_color(100, 100, 200)
    pdf.set_line_width(0.8)
    pdf.line(20, pdf.get_y(), 190, pdf.get_y())
    pdf.ln(6)

    # Experiência Profissional
    if curriculo.experiencias:
        pdf.set_font("Helvetica", "B", 13)
        pdf.set_text_color(60, 60, 180)
        pdf.cell(0, 8, "Experiência Profissional", ln=True)
        pdf.set_line_width(0.3)
        pdf.line(20, pdf.get_y(), 190, pdf.get_y())
        pdf.ln(3)

        for exp in curriculo.experiencias:
            pdf.set_font("Helvetica", "B", 11)
            pdf.set_text_color(30, 30, 30)
            pdf.cell(0, 7, exp["cargo"], ln=True)
            pdf.set_font("Helvetica", size=10)
            pdf.set_text_color(80, 80, 80)
            pdf.cell(0, 6, f'{exp["empresa"]}  —  {exp["periodo"]}', ln=True)
            pdf.ln(2)

        pdf.ln(2)

    # Formação Acadêmica
    if curriculo.formacoes:
        pdf.set_font("Helvetica", "B", 13)
        pdf.set_text_color(60, 60, 180)
        pdf.cell(0, 8, "Formação Acadêmica", ln=True)
        pdf.set_line_width(0.3)
        pdf.line(20, pdf.get_y(), 190, pdf.get_y())
        pdf.ln(3)

        for form in curriculo.formacoes:
            pdf.set_font("Helvetica", "B", 11)
            pdf.set_text_color(30, 30, 30)
            pdf.cell(0, 7, form["curso"], ln=True)
            pdf.set_font("Helvetica", size=10)
            pdf.set_text_color(80, 80, 80)
            pdf.cell(0, 6, f'{form["instituicao"]}  —  {form["ano"]}', ln=True)
            pdf.ln(2)

    pdf.output(caminho_saida)
    return caminho_saida
