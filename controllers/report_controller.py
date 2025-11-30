from bottle import response
from fpdf import FPDF
from .base_controller import BaseController
from services.habit_service import HabitService
from utils.session import get_session_user
from datetime import datetime

class ReportController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.habit_service = HabitService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/relatorio/pdf', method='GET', callback=self.generate_pdf)

    def generate_pdf(self):
        user = self.get_logged_user()
        if not user:
            return self.redirect('/login')

        habits = self.habit_service.get_by_user(user.id)

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        
        pdf.cell(190, 10, f"Relatório de Hábitos - {user.username}", ln=1, align='C')
        pdf.ln(10)

        pdf.set_font("Arial", size=10)
        pdf.cell(190, 10, f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M')}", ln=1, align='R')
        pdf.ln(10)

        pdf.set_font("Arial", 'B', 12)
        pdf.cell(60, 10, "Hábito", 1)
        pdf.cell(90, 10, "Descrição", 1)
        pdf.cell(40, 10, "Frequência", 1)
        pdf.ln()

        pdf.set_font("Arial", size=12)
        for habit in habits:
            name = habit.name.encode('latin-1', 'replace').decode('latin-1')
            desc = habit.description.encode('latin-1', 'replace').decode('latin-1')
            freq = habit.frequency.encode('latin-1', 'replace').decode('latin-1')

            pdf.cell(60, 10, name, 1)
            pdf.cell(90, 10, desc, 1)
            pdf.cell(40, 10, freq, 1)
            pdf.ln()

        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'attachment; filename="meus_habitos.pdf"'
        
        return pdf.output(dest='S').encode('latin-1')